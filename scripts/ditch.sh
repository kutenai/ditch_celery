#!/bin/bash

source $WORKON_HOME/ditch/bin/activate

export PYTHONPATH=/Volumes/bnpraid/Users/kutenai/proj/bondiproj/ditch_celery/scripts


pushd /Volumes/bnpraid/Users/kutenai/proj/bondiproj/ditch_celery/scripts

python ditch.py "$@"

popd

