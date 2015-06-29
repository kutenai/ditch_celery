#!/bin/bash

envname=ditch
envbase=/Users/kutenai/Envs
logdir=/Users/kutenai/django/logs/celery

LOGFILE=$logdir/celery_worker.log

source $envbase/$envname/bin/activate

celery worker -A ditchapp -l info --logfile=$LOGFILE --autoreload



