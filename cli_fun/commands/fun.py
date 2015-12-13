"""Fun section of CLI command."""
import json
import logging
import time
from pprint import pformat, pprint

import click
from fabric.colors import red


@click.group()
def cli():
    """My fun program!"""
    pass


@cli.command()
def progress():
    """Sample progress bar."""
    i = range(0, 200)
    logging.debug('%s -> %s', i[0], i[-1])
    with click.progressbar(i, width=0, fill_char=red('#')) as items:
        for _ in items:
            time.sleep(.01)


@cli.command('open')
def fun_open():
    """Trying out click.launch."""
    sites = {
        'Google': 'https://google.com',
        'The Verge': 'https://theverge.com',
        'Liliputing': 'https://liliputing.com'
    }

    sites_keys = sites.keys()
    for index, site in enumerate(sites_keys):
        click.echo('%i %s' % (index, site))

    choice = click.prompt('Which site to open?', default=0, type=int)
    click.launch(sites[sites_keys[choice]])


@cli.command()
def party():
    """Get this party started!"""
    for i in range(10):
        click.echo('Wub wub wub')
        logging.debug(i)


@cli.command('to')
@click.option('-d', '--destination', prompt=True)
def fun_to(destination):
    """Connecting fun to stuffs!"""
    click.echo('Apparently you are going to ' + destination)


@cli.command('max')
def fun_max():
    """Maximum levels achieved."""
    click.echo('You found the highest peak!')


@cli.command()
def hop():
    """The hopping function."""
    click.echo('Hop hop hop, \'til you just can stop!')


@cli.command()
def j():
    """Example JSON."""
    test_object = {'this': 'that', 'up': 'down', 'sub': {'can': 'do'}}
    print json.dumps(test_object, indent=2)
    pprint(test_object, indent=2)
    print pformat(test_object, indent=2)
    print pformat(test_object, indent=2, depth=1)
    print test_object.viewitems()
    print test_object.values()
    print test_object.viewvalues()
