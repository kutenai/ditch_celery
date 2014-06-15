#!/bin/bash

envname=ditch
envbase=/mnt/myebs/www/virtualenvs
logdir=/home/ec2-user/django/logs/celery

source $envbase/$envname/bin/activate

celery worker -A ditchapp -Q db --loglevel=INFO --logfile=$logdir/worker_db.log --autoreload



