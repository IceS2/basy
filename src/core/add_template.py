# TODO: Think better how to actually structure this module.
import copier
import json
from pathlib import Path
from typing import Optional, Tuple

from models import Template, Source
from registry import Registry


def resolve_source(source: Source) -> Tuple[str, dict]:
    if source.type == "local":
        return (source.path, {})
    else:
        return (source.path, {"vcs_ref": source.ref})


def execute(registry: Registry, name: str, path: Path, kwargs: str):
    template: Optional[Template] = registry.templates.get(name, None)

    if template:
        template_path, params = resolve_source(template.source)
        params = {
            **params,
            **json.loads(kwargs)
        }
        copier.run_auto(
            template_path,
            str(path.resolve()),
            **params)
    else:
        print("Template not found.")
