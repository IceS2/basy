import click
from pathlib import Path
from typing import Optional

from registry import Registry

from cli.list_templates import list_entity
from cli.use_template import use_entity
from cli.add_template import add_entity
from cli.remove_template import remove_entity


@click.group()
@click.option(
    "-t", "--templates-file",
    default=None,
    help="Templates file path.",
    type=click.Path(exists=True, path_type=Path)
)
@click.pass_context
def cli(ctx: click.Context, templates_file: Optional[Path]):
    ctx.obj = Registry.from_templates_file(templates_file)


cli.add_command(list_entity)
cli.add_command(use_entity)
cli.add_command(add_entity)
cli.add_command(remove_entity)
