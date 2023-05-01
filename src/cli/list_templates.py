import typer

app = typer.Typer(name="list")


@app.command(name="templates")
def list_templates(ctx: typer.Context):
    templates = ctx.obj.list()

    # TODO: Change to use rich
    if len(templates) > 0:
        typer.echo("{padding}Templates{padding}".format(
            padding=" " * int((80 - len("Templates"))/2)))
        typer.echo("-"*80)
        for template in templates:
            typer.secho(f"{template.name}", bold=True, fg="magenta")
            typer.echo("{padding}Source: {source}".format(
                padding=" " * 2, source=template.source.type))
            typer.echo("{padding}Description: {description}".format(
                padding=" " * 2, description=template.description
            ))
            typer.echo("{padding}Tags: {tags}".format(
                padding=" " * 2, tags=template.tags
            ))
            typer.echo("")
    else:
        typer.echo("Your Template Registry is empty.")
