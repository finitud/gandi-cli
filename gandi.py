import click
import click_config
import xmlrpclib


class Config:

    def __init__(self, key):
        self.api_key = key


pass_config = click.make_pass_decorator(Config)


@click.group()
@click_config.wrap(module=Config)
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
    """Domain API interface"""
    pass


@domain.command()
@pass_config
def list(config):
    result = config.api.domain.list(config.api_key)
    click.echo(result)


@cli.group()
@click.option('--domain', required=True, help='Domain to be edited')
@pass_config
def forward(config, domain):
    """Mail forwarding API interface"""
    config.target_domain = domain


@forward.command()
@pass_config
def count(config):
    """Add forwarding address to specified domain"""
    result = config.api.domain.forward.count(config.api_key,
                                             config.target_domain)
    click.echo(result)


@forward.command()
@click.argument('source')
@click.argument('destination')
@pass_config
def create(config, source, destination):
    """Add forwarding address to specified domain"""
    parameters = {'destinations': [destination]}
    result = config.api.domain.forward.create(config.api_key,
                                              config.target_domain,
                                              source,
                                              parameters)
    click.echo(result)
