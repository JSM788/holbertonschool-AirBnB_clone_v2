#!/usr/bin/python3
"""This script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import *
import pathlib

env.hosts = ['54.89.191.220', '23.20.55.144']


def do_deploy(archive_path):
    """Uncompress the archive"""
    if pathlib.Path(archive_path).exists() == False:
        return False
    else:
        path_tmp = "/tmp/web_static_{}.tgz"
        path_data = "/data/web_static/releases/web_static_{}/"
    
        put(archive_path, "/tmp")
        run("mkdir -p {}".format(path_data))
        run("tar -xzf {} -C {}".format(path_tmp, path_data))
        run("rm {}".format(path_tmp))
        run("mv {}/web_static/* {}".format(path_data, path_data))
        run("rm -rf {}/web_static".format(path_data))
        run("rm -rf /data/web_static/current")
        run("ls -s {} /data/web_static/current".format(path_data))


