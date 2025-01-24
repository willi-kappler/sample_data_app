#!/usr/bin/env bash

# Only build base container if needed:
if [ ! -f buildozer_base.sif ]; then
    singularity build --fakeroot buildozer_base.sif buildozer_base.def
fi

# Only build main container if needed:
if [ ! -f buildozer.sif ]; then
    singularity build --fakeroot buildozer.sif buildozer.def
fi

#
