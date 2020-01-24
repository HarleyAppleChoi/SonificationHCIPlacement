#!/bin/sh
BASEDIR=$(dirname $0)
WORKDIR=${BASEDIR}/Puredata_sound_UI
PATH=$PATH:/bin:/bin/sh
export PATH
pd -nogui ${WORKDIR}/musicDemo.pd &
python3 ${WORKDIR}/SoundSelectionUi.py & 