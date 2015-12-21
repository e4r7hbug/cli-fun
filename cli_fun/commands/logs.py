"""Test out some logging concepts."""
import logging

import click

LOG = logging.getLogger(__name__)


@click.group()
def cli():
    """Demonstrate logging concepts."""
    root_log = logging.root
    root_log.setLevel(logging.DEBUG)

    root_handler = logging.StreamHandler()
    root_formatter = logging.Formatter(
        '%(name)s\t%(levelno)s\t%(pathname)s\t%(filename)s\t%(module)s\t'
        '%(lineno)d\t%(funcName)s\t%(created)f\t%(asctime)s\t%(msecs)d\t'
        '%(relativeCreated)d\t%(thread)d\t%(threadName)s\t%(process)d\t'
        '%(message)s')
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
