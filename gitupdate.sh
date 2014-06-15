#!/bin/bash

git pull

envname=ditch
envbase=/mnt/myebs/www/virtualenvs
logdir=/home/ec2-user/django/logs/celery

source $envbase/$envname/bin/activate

pip install -r requirements.txt

