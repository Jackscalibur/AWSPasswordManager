import click
from secrets_manager.secrets_manager import SecretsManager

secrets_manager = SecretsManager()


@click.group
def cli():
    """Password Manager CLI"""
    pass
