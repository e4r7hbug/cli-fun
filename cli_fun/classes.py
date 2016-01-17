"""FunCLI classes."""
import importlib
import logging
import os
import sys

import click


class Context(object):
    """Shared context object for passing information between commands."""

    def __init__(self):
        self.verbose = False

    def log(self, msg, *args):
        """Logs a message to stderr."""

        if args:
            msg %= args

        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""

        if self.verbose:
            self.log(msg, *args)


class FunCLI(click.MultiCommand):
    """Click class for gathering commands."""
    log = logging.getLogger(__name__)

    def list_commands(self, ctx):
        """Search through the _commands_ directory for modules to use."""
        command_list = []
        cmd_folder = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'commands'))

        for filename in os.listdir(cmd_folder):
            self.log.debug('Found file in command directory: %s', filename)

            if filename.endswith('.py'):
                if not filename.startswith('__'):
                    command_name = filename[0:-3]

                    self.log.debug('Adding command to list: %s', command_name)
                    command_list.append(command_name)

        command_list.sort()
        self.log.debug('Sorted command list: %s', command_list)
        return command_list

    def get_command(self, ctx, name):
        """Dynamically import modules in the _commands_ directory."""
        try:
            if sys.version_info[0] == 2:
                self.log.debug('Python 2 detected, encoding "%s" in ascii.',
                               name)
                name = name.encode('ascii', 'replace')

            mod = importlib.import_module('.commands.{0}'.format(name),
                                          __package__)
            self.log.debug('Imported module: %s', mod)

            return mod.cli
        except ImportError as error:
            self.log.warning('Failed to import: %s', name)
            self.log.warning('Error information:\n%s', error)
            return
        except SyntaxError:
            self.log.warning('Failed to import: %s', name)
            self.log.warning('Might be a Python %s incompatible module.',
                             sys.version_info[0])
            return
