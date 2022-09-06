#!/usr/bin/python3
"""This script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using
the function do_deploy"""
from fabric.api import *
from os import path

env.hosts = ['54.89.191.220', '23.20.55.144']


def do_deploy(archive_path):
    """Uncompress the archive"""
    if not path.exists(archive_path):
        return False
    else:
        # versions/web_static_20170315003959.tgz
        with_tgz = archive_path.split("/")
        with_tgz = with_tgz[1]

        no_tgz = with_tgz.split(".")
        no_tgz = no_tgz[0]

        # /tmp/web_static_20170315003959.tgz
        path_tmp = "/tmp/{}".format(with_tgz)
        print("PATH_TMP")
        # /data/web_static/releases/web_static_20170315003959/
        path_data = "/data/web_static/releases/{}/".format(no_tgz)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_data))
        run("tar -xzf {} -C {}".format(path_tmp, path_data))
        run("rm {}".format(path_tmp))
        run("mv {}web_static/* {}".format(path_data, path_data))
        run("rm -rf {}web_static".format(path_data))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_data))
        return True
