#!/usr/bin/env python
"""
Thomas:

Examples of job submission:

bsub -q 8nm -J job1 < jobscript.sh
bsub -q 1nh -J job2 < jobscript.sh
bsub -q test -J job3 < jobscript.sh

"""

########################################
# Imports
########################################

import subprocess
import datetime
import time
import os
import re
import json
import shutil


########################################
# Main
########################################

def submit_jobs( runname = None ):

    if (not runname) or (not "RUNNAME" in os.environ):
        # Generate the runname (format: YYMMDD-HHMMSS)
        timestamp = datetime.datetime.now()
        runname = timestamp.strftime( '%y%m%d_%H%M%S' )
        os.environ["RUNNAME"] = runname

    # Copy runJob.mac into the directory from which to run
    shutil.copyfile( 'runJob.mac', '/afs/cern.ch/user/t/tklijnsm/Work/geant4/EEShashlikSimulation/H4OpticalSmall/cmake/runJob.mac')

    # Some run settings - number of jobs, which queue, script to run
    n_jobs = 3
    queue = '8nm'
    script = 'jobscript.sh'

    # Submit the jobs
    JOBIDs = []
    for i_job in range(n_jobs):

        cmd = "bsub -q {0} -J job{1} < {2}".format( queue, i_job+1, script )

        output = subprocess.Popen( [cmd], stdout=subprocess.PIPE, shell=True ).communicate()[0]
        JOBID = re.search( r'Job <([0-9]*)>', output ).group(1)
        JOBIDs.append( JOBID )

    # Write list of JOBIDs to json file (may be convenient for hadding later)
    with open( runname + '.json' , 'w' ) as json_file:
        json.dump( JOBIDs , json_file, indent=2, sort_keys=True )


########################################
# End of Main
########################################
if __name__ == "__main__":
    submit_jobs()
