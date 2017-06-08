#!/usr/bin/env python

from celery import chain

from dbtasks.tasks import onstatus
from ditchtasks.tasks import update_database

if __name__ == "__main__":
    update_database.apply_async()
