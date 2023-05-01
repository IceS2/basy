"""Define the CLI subcommand group `add`."""


from pathlib import Path

import core
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True, no_args_is_help=True)
def use_help():
    """Use an entity."""


# TODO: Instead of passing kwargs, split the left over arguments after `--`.
# How to avoid collision between what's after -- and any Option?
# How to actually call copier from CLI instead of programatically? Subprocess?
# Typer context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
@app.command(name="template")
def use_template(
    ctx: typer.Context,
    name: str = typer.Option(
        ...,
        "--name", "-n",
        prompt="Template to use",
        help="Template to use in the project."),
    path: str = typer.Option(
        ".",
        "--path", "-p",
        exists=True,
        help="Where to use the template at."),
    kwargs: str = typer.Option(
        "{}",
        "--kwargs",
        help="Kwargs to pass to copier.")
    ):
    """Use a template."""
    core.use_template(ctx.obj, name, Path(path), kwargs)
