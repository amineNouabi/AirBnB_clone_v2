#!/usr/bin/python3
"""
Module defining a Fabric script that deploys
    a .tgz archive to the web servers
"""

from fabric.api import put, run, env

env.hosts = ["34.203.75.0", "18.233.67.166"]


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
