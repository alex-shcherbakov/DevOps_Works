import click

@click.group()
def cli():
    """Набір CLI-команд на основі click."""
    pass


@cli.command()
@click.option('--name', required=True, help='Вкажіть ім’я для перевірки.')
def say(name):
    """Виводить ім’я, якщо воно не починається з p/P."""
    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()