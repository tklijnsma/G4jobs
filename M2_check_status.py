#!/usr/bin/env python
"""
Thomas:

"""

########################################
# Imports
########################################

import subprocess
import datetime
import time


########################################
# Main
########################################

def check_status():

    n_checks = 100
    for i_check in range(n_checks):

        timestamp = str(datetime.datetime.now())
        output = subprocess.Popen( [ 'bjobs' ], stdout=subprocess.PIPE ).communicate()[0]

        if 'PEND' in output:
            print 'Status check #{0} at {1}'.format( i_check, timestamp )
            print output
        else:
            print 'Run finished at ' + timestamp
            break

        time.sleep(36)


########################################
# Functions
########################################

# Reads lines from the status check and turns it into a dict
def output_to_dict( output ):

    lines = output.split('\n')[:-1]
    heading = lines.pop(0)

    # Determine boundaries based on first line
    scanning_word = True
    bounds = []
    for i_c, c in enumerate(heading):
        # Recognize end of word
        if scanning_word and c == ' ':
            scanning_word = False
        # Recognize end of spaces
        if not scanning_word and c != ' ':
            scanning_word = True
            bounds.append(i_c)
    # Manually enter last bound:
    bounds.append(len(heading))

    # Turn into dict
    outdict = {}

    prev_bound = 0
    for bound in bounds:
        key = heading[prev_bound:bound].strip()
        outdict[key] = []
        for line in lines:
            outdict[key].append( line[prev_bound:bound].strip() )
        prev_bound = bound

    return outdict


########################################
# End of Main
########################################
if __name__ == "__main__":
    check_status()
