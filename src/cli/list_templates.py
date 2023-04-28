import click

from registry import Registry


@click.group(name="list")
def list_entity():
    pass


@click.command(name="templates")
@click.pass_obj
def list_templates(registry: Registry):
    templates = registry.list()

    if len(templates) > 0:
        click.echo("{padding}Templates{padding}".format(
            padding=" " * int((80 - len("Templates"))/2)))
        click.echo("-"*80)
        for template in templates:
            click.secho(f"{template.name}", bold=True, fg="magenta")
            click.echo("{padding}Source: {source}".format(
                padding=" " * 2, source=template.source.type))
            click.echo("{padding}Description: {description}".format(
                padding=" " * 2, description=template.description
            ))
            click.echo("{padding}Tags: {tags}".format(
                padding=" " * 2, tags=template.tags
            ))
            click.echo("")
    else:
        click.echo("Your Template Registry is empty.")


list_entity.add_command(list_templates)
