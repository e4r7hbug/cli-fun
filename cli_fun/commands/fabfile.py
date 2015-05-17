import logging

import click
import fabric
from fabric.api import env, execute, parallel, run, runs_once, settings, task
from fabric.colors import blue, green, red, yellow


def _colourize_output(output):
    """
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

    print green('hosts succedded\n==============='.title())
    for host in good.keys():
        print green('%s succeeded' % (host))
    print green('===============\n')

    print red('hosts failed\n============'.title())
    for host, result in bad.iteritems():
        logging.fatal('FAILED! Command: %s Code: %-5s ERROR: %s',
                      blue(result.command), red(result.return_code),
                      red(result))
    print red('============\n')


@parallel
def _executor(command):
    with settings(warn_only=True):
        return run(command)


@task
@runs_once
def runner(command):
    """
    Run any arbitrary command on Hosts.
    """

    returned = execute(_executor, command)
    _colourize_output(returned)


@task
@runs_once
def home():
    """
    Run commands on home machine.
    """

    env.hosts = ['e4r7hbug.com']
    env.user = 'pi'
    env.port = 2347


def main():
    logging.basicConfig(format='[%(levelname)s] %(funcName)s - %(message)s')
    pass


@click.command()
def cli():
    print yellow(__name__)
    main()


if __name__ == '__main__' or '__fabfile__':
    main()
