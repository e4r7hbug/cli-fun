import click

from .classes import Context

CONTEXT_SETTINGS = dict(auto_envvar_prefix='PLAY')
PASS_CONTEXT = click.make_pass_decorator(Context, ensure=True)
