#!/usr/bin/env python
"""FunCLI root execution function."""
import logging

import click

from .constants import CONTEXT_SETTINGS, PASS_CONTEXT
from .classes import FunCLI


@click.command(cls=FunCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', is_flag=True, help='Enable DEBUG mode.')
@click.option('-v', '--verbose', is_flag=True, help='Enabled VERBOSE mode.')
@PASS_CONTEXT
def main(ctx, debug, verbose):
    """A playful command line interface."""
    ctx.verbose = verbose

    if debug:
        logging.root.setLevel(logging.DEBUG)
    elif verbose:
        logging.root.setLevel(logging.INFO)


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] %(module)s:%(funcName)s - %(message)s')

    main()  # pylint: disable=E1120
