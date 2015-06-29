from __future__ import absolute_import

from celery import task


@task(name='ditchtasks.tasks.status')
def status():
    pass

@task(name='ditchtasks.tasks.read_sensors')
def read_sensors():
    pass


@task(name='ditchtasks.tasks.pump_enable')
def pump_enable(bEnable):
    pass


@task(name='ditchtasks.tasks.south_enable')
def south_enable(bEnable):
    pass

@task(name='ditchtasks.tasks.north_enable')
def north_enable(bEnable):
    pass



