#!/usr/bin/python3
"""This script generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """All files in the folder web_static must be added to the final archive"""
    local("mkdir -p versions")
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    fil = "versions/web_static_{}.tgz web_static ".format(time)
    validation = local("tar -cvzf" + fil)

    if validation.failed:
        return None
    else:
        return validation
