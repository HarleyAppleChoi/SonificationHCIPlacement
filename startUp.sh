#!/bin/sh
BASEDIR=$(dirname $0)
WORKDIR=${BASEDIR}/Puredata_sound_UI
PATH=$PATH:/bin:/bin/sh
export PATH
echo $PATH
echo $ROOT
echo "Script location: $BASEDIR"
echo $WORKDIR
python3 ${WORKDIR}/SoundSelectionUI.py 
#sudo -s python3 ToutToPd.py &
