#!/usr/bin/python3
"""This script generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo"""
from fabric.api import local
from datetime import datetime


def do_pack():
    local("mkdir -p versions")

    fil = "versions/web_static_{}.tgz web_static"
    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), capture=True)
    validation = local("tar -cvzf" + fil)

    if validation.failed:
        return None
    else:
        return validation
