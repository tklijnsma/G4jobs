#!/usr/bin/env python
"""
Thomas:

"""

########################################
# Imports
########################################

import os
import datetime
from time import sleep

from M1_submit_jobs import submit_jobs
from M2_check_status import check_status
from M3_hadd_rootfiles import hadd_rootfiles


########################################
# Main
########################################

def main():

    # Generate the runname (format: YYMMDD_HHMMSS)
    timestamp = datetime.datetime.now()
    runname = timestamp.strftime( '%y%m%d_%H%M%S' )
    os.environ["RUNNAME"] = runname

    print 'Started run ' + runname

    submit_jobs( runname )
    check_status()

    print 'Waiting 10 seconds before attempting hadd...'
    sleep(10)
    hadd_rootfiles( runname )

    print 'Ended run ' + runname


########################################
# End of Main
########################################
if __name__ == "__main__":
    main()
