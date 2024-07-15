#!/usr/bin/python3
"""

Module defining a Fabric script that cleans out-of-date archives

"""

from fabric.api import run, env, local
from fabric.api import env
from fabric.decorators import runs_once

env.hosts = ["34.203.75.0", "18.233.67.166"]


@runs_once
def clean_local(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    number += 1
    local("cd versions; ls -t1 | tail -n +{} | xargs rm -rf".format(number))


def clean_remote(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    number += 1
    run("cd /data/web_static/releases; ls -t1 | tail -n +{} | xargs rm -rf".format(number))


def do_clean(number=0):
    """Deletes out-of-date archives"""
    clean_local(number)
    clean_remote(number)
