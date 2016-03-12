"""Experiments with docstrings and whatnot."""
import logging

import click


@click.group()
def cli():
    """Docstring experiments."""
    pass


def docstring():
    """The original docstring."""
    pass


@cli.command()
def test():
    """Run test."""
    log = logging.getLogger(__name__)
    log.debug('Changing the docstring.')

    help(docstring)

    docstring.__doc__ = """This is the newly modified docstring.

    We have modified the docstring to include our own information. This can be
    useful when needing to dynamically generate functions or methods.
    """

    help(docstring)
