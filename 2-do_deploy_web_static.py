#!/usr/bin/python3
"""fabric script"""
from fabric.api import *
import os
import datetime
env.hosts = ['104.196.60.146', '35.196.4.21']


def do_deploy(archive_path):
    """function that distributes an archive to a server"""
    if os.path.isfile('{}'.format(archive_path)) is False:
        return False
    tgz_file = archive_path.split('/')[-1]
    storage_location = '/tmp/'
    new_location = '/data/web_static/releases/'
    upload = put('{}'.format(archive_path), storage_location)
    if upload is False:
        return False
    create_dir = run('mkdir -p {}'.format(new_location +
                                          tgz_file.replace('.tgz', '')))
    if create_dir is False:
        return False
    uncompress = run('tar -xzvf {} -C {}'.format(storage_location +
                                                 tgz_file, new_location +
                                                 tgz_file.replace('.tgz', '')))
    if uncompress is False:
        return False
    delete_file = run('rm -f {}'.format(storage_location + tgz_file))
    if delete_file is False:
        return False
    new_route = "{}".format(new_location + tgz_file.replace('.tgz', ''))
    move_files = run('mv {}/web_static/* {}'.format(new_route, new_route))
    if move_files is False:
        return False
    delete_folder = run('rm -rf {}/web_static'.format(new_route))
    if delete_folder is False:
        return False
    sym_link_name = '/data/web_static/current'
    delete_sym = run('rm -f {}'.format(sym_link_name))
    if delete_sym is False:
        return False
    create_sym = run('ln -sT {} {}'.format(new_location +
                                           tgz_file.replace('.tgz', ''),
                                           sym_link_name))
    if create_sym is False:
        return False
    return True


def do_pack():
    """ This Generate a tar of /web_static """
    local("mkdir -p versions")
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file = local("tar -czvf versions/web_static_%s.tgz web_static" % time)
    if file:
        return "versions/web_static_{}.tgz".format(time)
    else:
        return None
