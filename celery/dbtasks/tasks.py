from __future__ import absolute_import

import json
import time

from celery.utils.log import get_task_logger

logger = get_task_logger('ditch')

from celery import task,shared_task,chain
from ditchtasks.tasks import status

@shared_task()
def update_database():
    ch = chain(status.s() | onstatus.s())
    ch.apply_async()


@task()
def onstatus(d):
    """
    Handle the status results
    """

    status = json.loads(d)

    logger.info("Status:%s" % status)
    secs = time.mktime(time.localtime())
    logger.info("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))

    return {"Status" : "Success"}

