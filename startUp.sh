#!/bin/sh
BASEDIR=$(dirname $0)
WORKDIR=${BASEDIR}/Puredata_sound_UI
PATH=$PATH:/bin:/bin/sh
export PATH
echo $PATH
echo $ROOT
echo "Script location: $BASEDIR"
echo $WORKDIR
pd -nogui ${WORKDIR}/*.pd &
python3 ${WORKDIR}/SoundSelectionUi.py & 
echo "load ToutToPd.py"
#python3 ${WORKDIR}/ToutToPd.py &
