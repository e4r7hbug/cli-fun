"""FunCLI classes."""
import importlib
import logging
import os
import sys

import click


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

            # Add package name to start of import if running CLI from installed
            # package
            module_path = [module
                           for module in [__package__, 'commands', name]
                           if module is not None]
            mod = importlib.import_module('.'.join(module_path))

            return mod.cli
        except ImportError as e:
            logging.critical(e)
            return
