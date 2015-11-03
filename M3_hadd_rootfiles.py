#!/usr/bin/env python
"""
Thomas:

"""

########################################
# Imports
########################################

import sys
import subprocess
import os


########################################
# Main
########################################

def hadd_rootfiles(runname):

    # Path to job output root files
    base_outdir = '/afs/cern.ch/user/t/tklijnsm/Work/joboutput/'
    joboutdir = base_outdir + runname + '/'

    if not os.path.isdir(joboutdir):
        print joboutdir + ' is not a directory.'
        return 0

    dirlist = os.listdir( joboutdir )

    if len(dirlist) == 0:
        print 'No output found in ' + joboutdir
        return 0

    # Filename for combined root file
    out_root_file = runname + '.root'

    # Parse the command
    arg_list = [ '-f', out_root_file ]
    for odir in dirlist:
        arg_list.append( joboutdir + odir + '/out.root' )

    print 'Passing the following arguments to hadd:'
    for arg in arg_list: print arg

    cmd = ' '.join( [ 'hadd' ] + arg_list )
    print '\nGiven command:'
    print cmd

    print '\nExecuting:'
    subprocess.call( [cmd], shell=True )


########################################
# End of Main
########################################
if __name__ == "__main__":

    if len(sys.argv) == 1 and "RUNNAME" in os.environ:
        runname = os.environ["RUNNAME"]
    elif len(sys.argv) == 2:
        runname = sys.argv[1]
    else:
        print 'Need a runname to determine which ROOT files to combine.'
        print 'Use "python M3_hadd_rootfiles.py YYMMDD_HHMMSS", or make sure the runname is defined in the environment under $RUNNAME.'
        sys.exit()

    hadd_rootfiles(runname)
