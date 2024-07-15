#!/usr/bin/python3
"""

Module defining a Fabric script that cleans out-of-date archives

"""

from fabric.api import local


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    number += 1
    local("cd versions; ls -t1 | tail -n +{} | xargs rm -rf".format(number))
