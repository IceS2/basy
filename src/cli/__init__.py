import typer
from pathlib import Path

from cli.add_template import app as add_group
from cli.use_template import app as use_group
from cli.remove_template import app as remove_group
from cli.list_templates import app as list_group
from registry import Registry


app = typer.Typer()
app.add_typer(add_group, name="add")
app.add_typer(list_group, name="list")
app.add_typer(remove_group, name="remove")
app.add_typer(use_group, name="use")


@app.callback(invoke_without_command=True, no_args_is_help=True)
def entrypoint(
    ctx: typer.Context,
    templates_file: Path = typer.Option(None, "--templates-file", "-t", help="Templates file path.")
    ):
    ctx.obj = Registry.from_templates_file(templates_file)
