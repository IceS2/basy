import typer


app = typer.Typer(name="remove")


# TODO: Prompt with rich
@app.command(name="template")
def remove_template(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", "-n", help="Name of the template to remove."),
    ):
    if name in ctx.obj.templates:
        typer.confirm(f"Are you sure you want to delete the template {name}?", abort=True)
    ctx.obj.remove(name)
