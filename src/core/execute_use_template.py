"""How to actually execute the `use template` command."""
# TODO: Think better how to actually structure this module.
import json
from pathlib import Path
from typing import Optional, Tuple

import copier
import copier.cli
from models import Source, Template
from registry import Registry


def _resolve_source(source: Source) -> Tuple[str, dict]:
    if source.kind == "local":
        return (source.path, {})
    else:
        return (source.path, {"vcs_ref": source.ref})


def execute(registry: Registry, name: str, path: Path, kwargs: str):
    """Executes the `use template` command by calling Copier underneath.

    Args:
        registry: Basy Registry
        name: Name of the template to use
        path: Where to use the template at
        kwargs: Any type of kwarg to be passed to `copier.run_auto`
    """
    template: Optional[Template] = registry.templates.get(name, None)

    if template:
        template_path, params = _resolve_source(template.source)
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
