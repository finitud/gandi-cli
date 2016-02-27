import click
import xmlrpclib


class Config:

    def __init__(self, key):
        self.api_key = key


pass_config = click.make_pass_decorator(Config)


@click.group()
@click.option('--key', envvar='GANDI_API_KEY',
              help='User API key (overrides GANDI_API_KEY variable)')
@click.option('--url', envvar='GANDI_API_URL',
              help='Remote API endpoint (overrides GANDI_API_URL variable)')
@click.pass_context
def cli(context, key, url):
    """
    A command-line interface to manage Gandi domain configuration
    """
    context.obj = Config(key)
    context.obj.api = xmlrpclib.ServerProxy(url)


@cli.command()
@pass_config
def version(config):
    """Display API version info"""
    click.echo(config.api.version.info(config.api_key))


@cli.group()
@pass_config
def domain(config):
    pass


@domain.command()
@pass_config
def list(config):
    result = config.api.domain.list(config.api_key)
    click.echo(result)
