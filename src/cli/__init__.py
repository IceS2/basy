"""CLI entrypoint.

All the CLI commands are defined in this module. It should have no core logic at all.
"""
from pathlib import Path

import typer
from cli.add_template import app as add_group
from cli.list_templates import app as list_group
from cli.remove_template import app as remove_group
from cli.use_template import app as use_group
from registry import Registry

app = typer.Typer()
app.add_typer(add_group, name="add")
app.add_typer(list_group, name="list")
app.add_typer(remove_group, name="remove")
app.add_typer(use_group, name="use")

# TODO: Improve how the rich text works on help to create different parameter/command
# groups.

@app.callback(invoke_without_command=True, no_args_is_help=True)
def entrypoint(
    ctx: typer.Context,
    templates_file: Path = typer.Option(
        None,
        "--templates-file", "-t",
        help="Templates file path.")
    ):
    """Welcome!

    I was created to help manage multiple scaffoling templates.
    When in doubt please check the documentation here: <TBD>.

    Have fun (=
    """
    ctx.obj = Registry.from_templates_file(templates_file)
