from __future__ import annotations
from pathlib import Path
from typing import  List, Dict, Optional
import json
import yaml

from models import Settings, Source, Template, TemplatesFile


class Registry:
    def __init__(self, templates: Dict[str, Template], templates_file: Path):
        self.templates: Dict[str, Template] = templates
        self.templates_file: Path = templates_file

    @classmethod
    def from_templates_file(cls, templates_file: Optional[Path]) -> Registry:
        if not templates_file:
            default_settings = Settings()
            templates_file = Path(default_settings.root_dir) / Path(default_settings.templates_file)

        templates_file.parent.mkdir(exist_ok=True, parents=True)
        templates_file.touch(exist_ok=True)

        with open(templates_file, "r") as f:
            templates = TemplatesFile.parse_obj(yaml.safe_load(f) or {}).templates

        return Registry(
            templates=templates,
            templates_file=templates_file.resolve()
        )

    def list(self) -> List[Template]:
        return list(self.templates.values())

    def add(self, name: str, source: Source, description: str, tags: List[str]):
        if name in self.templates:
            print(f"Warning, overriding template {name}.")

        self.templates[name] = Template(
            source=source,
            name=name,
            description=description,
            tags=tags
        )
        self.save()

    def remove(self, name: str):
        if name in self.templates:
            del self.templates[name]
            self.save()
            print(f"Template {name} removed.")
        else:
            print(f"Template {name} not found.")

    def save(self):
        templates = {
            template_dict.pop("name"): template_dict
            for template_dict
            in [json.loads(template.json()) for template in self.templates.values()]
        }
        with open(self.templates_file, "w") as f:
            yaml.safe_dump({"templates": templates}, f)
