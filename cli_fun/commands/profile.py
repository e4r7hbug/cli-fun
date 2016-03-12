"""Experiments with docstrings and whatnot."""
import logging
import time

import click

import laboratory

LOG = logging.getLogger(__name__)


class MyExperiment(laboratory.Experiment):
    """Run experiments."""

    def compare(self, control, observation):
        """Override the default comparison of control and observation.

        The default comparitor should be good enough for most situations. The
        trick to enabling the comparison is using 'raise_on_mismatch=True'.
        """
        comparison = control.value == observation.value
        LOG.info('Comparison: %s', comparison)
        return comparison

    def publish(self, result):
        """Publish results.

        This runs automatically after all candidates have finished. The idea
        would be to publish the results somewhere for inspection outside of the
        running code.
        """
        LOG.info('Control took %s seconds.', result.control.duration)
        LOG.info('Control value: %s', result.control.value)

        for index, observation in enumerate(result.observations):
            LOG.info('Observation %d took %s seconds.', index,
                     observation.duration)
            LOG.info('Observation %d value: %s', index, observation.value)

        if not result.match:
            LOG.critical('Observation results do not match control result.')
        else:
            LOG.info('Observation results match control result.')

        LOG.debug('Result attributes: %s', dir(result))
        LOG.debug('Observation attributes: %s', dir(result.observations[0]))


@click.group()
def cli():
    """Use Laboratory to test new function algorithms."""
    pass


def code2(arg):
    """New code path."""
    print('Code 2')
    time.sleep(arg / 2)
    return arg / 2


@MyExperiment(candidate=code2, raise_on_mismatch=True)
def code1(arg):
    """Original code path."""
    print('Code 1')
    time.sleep(arg)
    return arg


@cli.command()
def test():
    """Run test."""
    if LOG.getEffectiveLevel() > logging.INFO:
        LOG.setLevel(logging.INFO)

    print('Running original code with experimental code.')
    code1(2)
