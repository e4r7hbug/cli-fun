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
@click.option('-h', '--hosts',
              multiple=True,
              required=True,
              help='Hostnames to run on')
@click.option('-u', '--user', help='User to run as')
@click.option('-p', '--port', default=22, help='Port to use')
@task
@runs_once
def cli(hosts, user, port):
    logging.debug(blue(locals()))
    with settings(hosts=hosts, user=user, port=port):
        execute(uname)
