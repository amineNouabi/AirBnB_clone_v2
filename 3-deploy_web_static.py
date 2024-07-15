#!/usr/bin/python3
"""
Module defining a Fabric script that compresses and deploys to web servers
"""
from fabric.decorators import runs_once
from fabric.api import put, run, env, local
from os.path import getsize
from datetime import datetime

env.hosts = ["web-01.nouabi.tech", "web-02.nouabi.tech"]


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(now)

        print("Packing web_static to {}".format(file_name))
        result = local("tar -cvzf {} web_static".format(file_name))

        if result.failed:
            return None
        else:
            print(
                "web_static packed: {} -> {}Bytes".format(file_name,
                                                          getsize(file_name)))
            return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploys a .tgz archive to the web servers"""
    if not archive_path:
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        path = "/data/web_static/releases/{}/".format(folder_name)

        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path))
        run("rm /tmp/{}".format(file_name))

        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))

        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))

        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Creates and deploys a .tgz archive to the web servers"""
    return do_deploy(do_pack())
