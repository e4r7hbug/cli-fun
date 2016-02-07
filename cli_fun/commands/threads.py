"""Try using threads in Python."""
import logging
import threading

import click


@click.group()
def cli():
    """Example multithreading functions."""
    pass


def worker(num):
    """Thread worker."""
    print('Worker #{0}'.format(num))
    return True


@cli.command()
def spawn():
    """Create threads and do stuff."""
    log = logging.getLogger(__name__)

    threads = []
    for num in range(5):
        thread = threading.Thread(target=worker, args=(num, ))
        log.info('Created thread #%d: %s', num, thread)
        threads.append(thread)

        log.info('Starting thread #%d', num)
        thread.start()

    log.info('Threads array: %s', threads)
