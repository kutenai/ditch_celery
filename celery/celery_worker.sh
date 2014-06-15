#!/bin/bash

envname=ditch
envbase=/Users/kutenai/Envs
#logdir=/home/ec2-user/django/logs/celery

source $envbase/$envname/bin/activate

celery worker -A ditchapp -l info --autoreload



