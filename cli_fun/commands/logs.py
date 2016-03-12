"""Test out some logging concepts."""
import logging

import click

LOG = logging.getLogger(__name__)


@click.group()
def cli():
    """Demonstrate logging concepts."""
    root_log = logging.root
    root_log.setLevel(logging.DEBUG)

    format_dict = {
        'name': 's',
        'levelno': 's',
        'pathname': 's',
        'filename': 's',
        'module': 's',
        'lineno': 'd',
        'funcName': 's',
        'created': 'f',
        'asctime': 's',
        'msecs': 'd',
        'relativeCreated': 'd',
        'thread': 'd',
        'threadName': 's',
        'process': 'd',
        'message': 's'
    }
    format_string = '\t'.join(['%({0}){1}'.format(item, type)
                               for item, type in format_dict.items()])

    root_handler = logging.StreamHandler()
    root_formatter = logging.Formatter(format_string)
    root_handler.setFormatter(root_formatter)

    root_log.addHandler(root_handler)


@cli.command("func")
def function_level():
    """Function level logging."""
    log = logging.getLogger(__name__)

    # Using the function level logger
    log.info('This thing.')

    # Using the module level logger
    LOG.info('That global.')
