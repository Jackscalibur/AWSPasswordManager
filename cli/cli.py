import click
from secrets_manager.secrets_manager import SecretsManager

secrets_manager = SecretsManager()


@click.group
def cli():
    """Password Manager CLI"""
    pass


@click.command
@click.argument('secret_name')
@click.argument('secret_value')
def create(secret_name, secret_value):
    """Create a new secret."""
    response = secrets_manager.create_secret(secret_name, secret_value)
    click.echo(f"Secret created: {response}")


@click.command
@click.argument('secret_name')
def get(secret_name):
    """Retrieve a secret."""
    secret = secrets_manager.get_secret(secret_name)
    click.echo(f"Secret value: {secret}")

# TODO: Add update and delete methods
