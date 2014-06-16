from __future__ import absolute_import

import sys
from unipath import Path
import json
import redis

BASE_PATH = Path(__file__).ancestor(2)
SCRIPT_PATH = BASE_PATH.ancestor(1).child('scripts')
print("BasePath:%s" % BASE_PATH)

sys.path.append(SCRIPT_PATH)
print("Appended script path:%s" % SCRIPT_PATH)

from celery import task
from celery.utils.log import get_task_logger

logger = get_task_logger('ditch')

from Ditch.IrrigationAPIAT import IrrigationAPI

api = IrrigationAPI()

@task()
def status():
    logger.info("Getting system status..")
    stat = api.getSystemStatus()
    r = redis.StrictRedis(host='gardenbuzz.com', port=6379, db=3)
    r.set('ditch_status',json.dumps(stat))

    return json.dumps(stat)


@task()
def read_sensors():
    d = api.getSensorData()
    return json.dumps(d)


@task()
def pump_enable(bEnable):
    logger.info("Set Pump Enable to %s" % bEnable)
    api.pumpEnable(bEnable)
    logger.info("Done")


@task()
def south_enable(bEnable):
    logger.info("Set South Enable to %s" % bEnable)
    api.southEnable(bEnable)
    logger.info("Done")


@task()
def north_enable(bEnable):
    logger.info("Set North Enable to %s" % bEnable)
    api.northEnable(bEnable)
    logger.info("Done")




