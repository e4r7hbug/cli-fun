#!/usr/bin/env python
"""FunCLI root execution function."""
import logging
import os
import pprint
import sys

import click

logging.basicConfig(
    format='[%(levelname)s] %(module)s - %(funcName)s: %(message)s')

CONTEXT_SETTINGS = dict(auto_envvar_prefix='PLAY')


class Context(object):
    def __init__(self):
        self.verbose = False

    def log(self, msg, *args):
        """
        Logs a message to stderr.
        """

        if args:
            msg %= args

        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """
        Logs a message to stderr only if verbose is enabled.
        """

        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)


class FunCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        cmd_folder = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'commands'))

        for filename in os.listdir(cmd_folder):

            if filename.endswith('.py') and not \
               filename.startswith('__'):
                rv.append(filename[0:-3])

        rv.sort()
        logging.debug(rv)
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')

            mod = __import__('cli_fun.commands.' + name, None, None, ['cli'])
            return mod.cli
        except ImportError as e:
            logging.critical(e)
            return


@click.command(cls=FunCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', is_flag=True, help='Enable DEBUG mode.')
@click.option('-v', '--verbose', is_flag=True, help='Enabled VERBOSE mode.')
@pass_context
def main(ctx, debug, verbose):
    """A playful command line interface."""
    ctx.verbose = verbose

    if debug:
        logging.root.setLevel(logging.DEBUG)
    elif verbose:
        logging.root.setLevel(logging.INFO)


logging.basicConfig(
    format='[%(levelname)s] %(module)s - %(funcName)s: %(message)s')

main()
