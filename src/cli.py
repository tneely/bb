import click

@click.command()
@click.option("--name", prompt="Your name", help="The name to say hello to.")
def entry(name: str):
    print(f"Hello, {name}!")
