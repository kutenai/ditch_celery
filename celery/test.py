#!/usr/bin/env python

from dbtasks.tasks import onstatus
from ditchtasks.tasks import status

if __name__ == "__main__":

    s = '{"Sump": "653", "P": "0", "NC": "0", "STen": "0", "N": "0", "PC": "0", "S": "0", "ST": "0", "SC": "0", "Ditch": "765"}'

    print("Calling task named %s" % onstatus.name)

    r = status.delay()
    stat = r.get(timeout=10)

    print("Status:%s" % stat)

    r = onstatus.delay(s)

    result = r.get(timeout=10)

    print("Result:%s" % result)



