#!/usr/bin/python3
# function to generate a tar file
""" generates a tar file """
from fabric.api import *
from datetime import datetime
import os.path
env.hosts = ['104.196.60.146','35.196.4.21'] 

def do_pack():
    """ This Generate a tar of /web_static """
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file = local("tar -czvf versions/web_static_%s.tgz web_static" % time)
    if file:
        return "versions/web_static_{}.tgz".format(time)
    else:
        return None

def do_deploy(archive_path):
    if os.path.exists(archive_path):
        temporal_path = '/tmp/'
        file_with_ext = archive_path.replace('versions/', '')
        file_name = file_with_ext[:-4]
        path_remote = "/data/web_static/releases/{}".format(file_name)
        put(archive_path, temporal_path + file_with_ext)
        run('mkdir -p %s' % path_remote)
        run('tar -xzf %s%s -C %s' % (temporal_path + file_with_ext, path_remote))
        run('rm %s%s' % (temporal_path, file_with_ext))
        run('mv %s %s' % (path_remote + '/web_static/*', path_remote))
        run('rm -rf %s' % path_remote + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s %s /data/web_static/current' % path_remote)
        return True
    else:
        return False
