"""The Registry stores all the Templates information in memory."""
from __future__ import annotations

import json
from pathlib import Path

import yaml
from models import Settings, Source, Template, TemplatesFile


class Registry:
    """Handles how to interact with the saved templates information.

    Attributes:
        templates: Dict containing all the templates information, using the name as key.
        templates_file: File where the templates information is stored.
    """
    def __init__(self, templates: dict[str, Template], templates_file: Path):
        """Instantiates a new Registry.

        Args:
            templates: Dict containing all the templates information,
                using the name as key
            templates_file: File where the templates information is stored.
        """
        self.templates: dict[str, Template] = templates
        self.templates_file: Path = templates_file

    @classmethod
    def from_templates_file(cls, templates_file: Path | None) -> Registry:
        """Instantiates a new Registry from a template_file.

        Args:
            templates_file: File where the templates information is stored.

        Returns:
            Registry
        """
        if not templates_file:
            default_settings = Settings()
            templates_file = (
                Path(default_settings.root_dir) /
                Path(default_settings.templates_file)
            )

        templates_file.parent.mkdir(exist_ok=True, parents=True)
        templates_file.touch(exist_ok=True)

        with Path.open(templates_file) as f:
            templates = TemplatesFile.parse_obj(yaml.safe_load(f) or {}).templates

        return Registry(
            templates=templates,
            templates_file=templates_file.resolve()
        )

    def to_list(self) -> list[Template]:
        """Lists all the templates.

        Returns:
            list[Template]
        """
        return list(self.templates.values())

    def add(self, name: str, source: Source, description: str, tags: list[str]):
        """Add a new Template to the Registry.

        Args:
            name: Name of the Template to add.
            source: Source of the Template to add.
            description: Small description to explain what the template is about.
            tags: Any relevant tag to attach to the template.
        """
        if name in self.templates:
            print(f"Warning, overriding template {name}.")

        self.templates[name] = Template(
            source=source,
            name=name,
            description=description,
            tags=tags
        )

    def remove(self, name: str):
        """Remove a Template from the Registry.

        Args:
            name: Name of the Template to remove.
        """
        if name in self.templates:
            del self.templates[name]
            self.save()
            print(f"Template {name} removed.")
        else:
            print(f"Template {name} not found.")

    def save(self):
        """Save the Registry information to the templates_file. It overrides it."""
        templates = {
            template_dict.pop("name"): template_dict
            for template_dict
            in [json.loads(template.json()) for template in self.templates.values()]
        }
        with Path.open(self.templates_file, "w") as f:
            yaml.safe_dump({"templates": templates}, f)
