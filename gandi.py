import click


class Config:
    def __init__(self):
        self.api_key = ''
        self.api_url = ''


pass_config = click.make_pass_decorator(Config)


@click.group()
@click.option('--key', envvar='GANDI_API_KEY',
              help='User API key (overrides GANDI_API_KEY variable)')
@click.option('--url', envvar='GANDI_API_URL',
              help='Remote API endpoint (overrides GANDI_API_URL variable)')
@pass_config
def cli(config, key, url):
    """
    A command-line interface to manage Gandi domain configuration
    """
    config.api_key = key
    config.api_url = url


@cli.group()
@click.option('--domain', help='Target domain')
@pass_config
def mail(config):
    pass
