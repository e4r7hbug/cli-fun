import logging

import click
from fabric.api import env, execute, parallel, run, runs_once, settings, task
from fabric.colors import blue, green, red


@parallel
def uname():
    with settings(warn_only=True):
        returned = run('unam')

        if returned.succeeded:
            print green('%s succeeded' % (env.host))
        else:
            print red('%s failed:\nRAN: %s\nERROR: %s' %
                      (env.host, returned.real_command, returned))


@click.command('home')
@task
@runs_once
def cli():
    logging.debug(blue('HOME'))
    with settings(hosts=['e4r7hbug.com'], user='pi', port=2347):
        execute(uname)
