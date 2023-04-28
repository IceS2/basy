import click
from pathlib import Path

import core
from registry import Registry


@click.group(name="use")
def use_entity():
    pass


@click.command(name="template")
@click.option(
    "-n", "--name",
    prompt="Template to add",
    help="Template to add to the project.",
    type=str
)
@click.option(
    "-p", "--path",
    default=".",
    help="Where to add the template.",
    type=click.Path(exists=True, path_type=Path),

)
@click.option(
    "--kwargs",
    default='{}',
    help="Kwargs to pass to copier.",
    type=str)
@click.pass_obj
def use_template(registry: Registry, name: str, path: Path, kwargs: str):
    core.add_template(registry, name, path, kwargs)


use_entity.add_command(use_template)
