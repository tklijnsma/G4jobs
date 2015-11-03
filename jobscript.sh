# Print some specifics in stdout
echo "PWD:"
echo $PWD
echo "TMPDIR:"
echo $TMPDIR
echo "USER:"
echo $USER

# Set the environment for geant4
source /afs/cern.ch/sw/lcg/contrib/gcc/4.7/x86_64-slc6/setup.sh
source /afs/cern.ch/sw/lcg/external/geant4/10.0.p01/x86_64-slc6-gcc47-opt/CMake-setup.sh
export CXX=/afs/cern.ch/sw/lcg/contrib/gcc/4.7/x86_64-slc6/bin/g++
export CC=/afs/cern.ch/sw/lcg/contrib/gcc/4.7/x86_64-slc6/bin/gcc

# Get JOBID and JOBOUTDIR, create out directory
export JOBID=$(basename $PWD)
echo "JOBID:"
echo $JOBID

export JOBOUTDIR=/afs/cern.ch/user/t/tklijnsm/Work/joboutput/$RUNNAME/$JOBID/
mkdir -p $JOBOUTDIR
echo "JOBOUTDIR:"
echo $JOBOUTDIR

# Go to project directory and execute
cd /afs/cern.ch/user/t/tklijnsm/Work/geant4/EEShashlikSimulation/H4OpticalSmall/cmake
./runEEShashlik -m runJob.mac
