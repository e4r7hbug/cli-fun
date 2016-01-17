"""Remote Server control with Fabric."""
import logging

import click
from fabric.api import execute, parallel, run, runs_once, settings, task
from fabric.colors import blue, green, red


def _colourize_output(output):
    """Colourize the Fabric run output.

    Form a nice colourized footer to which hosts succedded running commands and
    which hosts failed with error output.
    """

    good = {}
    bad = {}
    for host, result in output.iteritems():
        if result.succeeded:
            good[host] = result
        else:
            bad[host] = result

    print(green('hosts succedded\n==============='.title()))
    for host in good.keys():
        print(green('%s succeeded' % (host)))
    print(green('===============\n'))

    print(red('hosts failed\n============'.title()))
    for host, result in bad.items():
        logging.fatal('FAILED! Command: %s Code: %-5s ERROR: %s',
                      blue(result.command), red(result.return_code),
                      red(result))
    print(red('============\n'))


@parallel
def uname():
    """Run `uname` command."""
    with settings(warn_only=True):
        return run('unam')


@click.command('home')
@click.option('-h',
              '--hosts',
              multiple=True,
              required=True,
              help='Hostnames to run on')
@click.option('-u', '--user', help='User to run as')
@click.option('-p', '--port', default=22, help='Port to use')
@task
@runs_once
def cli(hosts, user, port):
    """Try using Fabric to run commands on remote machines."""
    logging.debug(blue(locals()))
    with settings(hosts=hosts, user=user, port=port):
        _colourize_output(execute(uname))
