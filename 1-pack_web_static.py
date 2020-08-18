#!/usr/bin/python3
# function to generate a tar file 
from fabric.api import local
from datetime import datetime

def do_pack():
    """ This Generate a tar of /web_static """
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czvf versions/web_static_%s.tgz" % time)
