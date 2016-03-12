"""Test out some logging concepts."""
import collections
import logging

import click

LOG = logging.getLogger(__name__)


@click.group()
def cli():
    """Demonstrate logging concepts."""
    root_log = logging.root
    root_log.setLevel(logging.DEBUG)

    format_dict = collections.OrderedDict()
    format_dict['name'] = 's'
    format_dict['levelno'] = 's'
    format_dict['levelname'] = 's'
    format_dict['pathname'] = 's'
    format_dict['filename'] = 's'
    format_dict['module'] = 's'
    format_dict['lineno'] = 'd'
    format_dict['funcName'] = 's'
    format_dict['created'] = 'f'
    format_dict['asctime'] = 's'
    format_dict['msecs'] = 'd'
    format_dict['relativeCreated'] = 'd'
    format_dict['thread'] = 'd'
    format_dict['threadName'] = 's'
    format_dict['process'] = 'd'
    format_dict['message'] = 's'

    format_string = '\n'.join(['{0} = %({0}){1}'.format(item, type)
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
