"""Define the CLI subcommand group `add`."""


from pathlib import Path
from typing import List

import typer
from models import Source

app = typer.Typer()

# TODO: Do this right ;P
def _resolve_source(path: str, ref: str) -> Source:
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


@app.callback(invoke_without_command=True, no_args_is_help=True)
def add_help():
    """Add a new entity."""


@app.command(name="template")
def template(
    ctx: typer.Context,
    name: str = typer.Option(
        ...,
        "--name", "-n",
        prompt="Template name",
        help="Name of the template to add."),
    path: str = typer.Option(
        ...,
        "--path", "-p",
        prompt="Template path",
        help="Path of the template to add."),
    vcs_ref: str = typer.Option(
        "main",
        "--vcs-ref", "-r",
        help="Reference for the VCS. Example: branch, tag"),
    description: str = typer.Option(
        "",
        "--description", "-d",
        prompt="Template description",
        help="Small description to explain what this template is about."),
    tags: List[str] = typer.Option(
        [],
        "--tag", "-t",
        help="Any tags that you'd like to add to the template.")
    ):
    """Add a template."""
    source: Source = _resolve_source(path=path, ref=vcs_ref)
    ctx.obj.add(
        name,
        source,
        description,
        tags)
    ctx.obj.save()
