#!/usr/bin/python3
# module with Fabric script that creates and distributes an archive to server

from fabric.api import *
import os.path
import datetime

def deploy():
    """ start deploy """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
