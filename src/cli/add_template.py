import click
from pathlib import Path
from typing import List

from models import Source
from registry import Registry


# TODO: Do this right ;P
def resolve_source(path: str, ref: str) -> Source:
    if path.startswith("git"):
        return Source(
            type="git",
            path=path,
            ref=ref
        )
    else:
        return Source(
            type="local",
            path=str(Path(path).resolve()),
            ref=None
        )


@click.group(name="add")
def add_entity():
    pass


@click.command(name="template")
@click.option(
    "-n", "--name",
    prompt="Template name",
    help="Name of the template to add.",
    type=str,
)
@click.option(
    "-p", "--path",
    prompt="Template path",
    help="Path of the template to add.",
    type=str
)
@click.option(
    "-r", "--vcs-ref",
    default="main",
    help="Reference for the VCS. Examples: branch, tag",
    type=str,
)
@click.option(
    "-d", "--description",
    prompt="Template description",
    default="",
    help="Small description to explain what this template is about",
    type=str
)
@click.option(
    "-t", "--tag",
    multiple=True,
    help="Any tags that you'd like to add to the template.",
    type=str
)
@click.pass_obj
def add_template(
        registry: Registry,
        name: str,
        path: str,
        vcs_ref: str,
        description: str,
        tag: List[str]):

    source: Source = resolve_source(path=path, ref=vcs_ref)
    registry.add(
        name,
        source,
        description,
        tag
    )


add_entity.add_command(add_template)
