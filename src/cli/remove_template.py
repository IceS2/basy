"""Define the CLI subcommand group `add`."""


import typer

app = typer.Typer(name="remove")


@app.callback(invoke_without_command=True, no_args_is_help=True)
def remove_help():
    """Remove an entity."""


# TODO: Prompt with rich
@app.command(name="template")
def remove_template(
    ctx: typer.Context,
    name: str = typer.Option(
        ...,
        "--name", "-n",
        help="Name of the template to remove."),
    ):
    """Remove a template."""
    if name in ctx.obj.templates:
        typer.confirm(
            f"Are you sure you want to delete the template {name}?", abort=True)
    ctx.obj.remove(name)
    ctx.obj.save()
