#!/usr/bin/python3
"""
Module defining a Fabric script that compresses
    web_static folder into a .tgz file
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file_name = "versions/web_static_{}.tgz".format(now)

    print("Packing web_static to {}".format(file_name))
    result = local("tar -cvzf {} web_static".format(file_name))

    if result.failed:
        return None
    else:
        print("web_static packed: {} -> {}Bytes".format(file_name,
              os.path.getsize(file_name)))
        return result
