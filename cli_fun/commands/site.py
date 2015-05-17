import click
from jinja2 import FileSystemLoader


@click.command()
@click.argument('file', type=FileSystemLoader)
def cli(file):
    """Using Jinja2 to render website HTML."""
    click.echo(dir(file))
    click.echo(file.list_templates())
    # [click.echo(line.strip('\n')) for line in file]


if __name__ == '__main__':
    cli()
