import typer
from pathlib import Path

import core


app = typer.Typer()


# @app.command(name="template", context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
@app.command(name="template")
def use_template(
    ctx: typer.Context,
    name: str = typer.Option(..., "--name", "-n", prompt="Template to use", help="Template to use in the project."),
    path: str = typer.Option(".", "--path", "-p", help="Where to use the template at.", exists=True),
    kwargs: str = typer.Option("{}", "--kwargs", help="Kwargs to pass to copier.")
    ):
    core.add_template(ctx.obj, name, Path(path), kwargs)
