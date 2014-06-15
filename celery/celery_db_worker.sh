#!/bin/bash

envname=ditch
envbase=/mnt/myebs/www/virtualenvs
logdir=/home/ec2-user/django/logs/celery

source $envbase/$envname/bin/activate

python celery -A ditchapp -Q db --loglevel=INFO --logfile=$logdir/worker.log --autoreload


