import click

from registry import Registry


@click.group(name="remove")
def remove_entity():
    pass


@click.command(name="template")
@click.option(
    "-n", "--name",
    type=str,
    help="Name of the source to remove"
)
@click.pass_obj
def remove_template(
        registry: Registry,
        name: str):
    registry.remove(name)


remove_entity.add_command(remove_template)
