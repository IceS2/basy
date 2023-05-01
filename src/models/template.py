"""Models related to the Template."""
from pathlib import Path
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field, root_validator, validator


class Source(BaseModel):
    """Source of the Template.

    It stores the Source information:
        - kind: Either 'local' or 'git'.
        - path:
            If kind='local', points to a local file.
            If kind='git', points to a git repository.
        - ref:
            If kind='local', it is None.
            If kind='git', points to the default git reference
                example: main
    """
    kind: Literal["local", "git"] = Field(alias="type")
    path: str
    ref: Optional[str] = None

    @root_validator(pre=True)
    def _alter_object_if_path_is_local(cls, values):
        if values["type"] == "local":
            values["ref"] = None
            values["path"] = str(Path(values["path"]).resolve())
        return values


class Template(BaseModel):
    """Template.

    It stores the Template information:
        - source: Source information.
            Check the Source class for more information.
        - name: Template name. It should be a simple string.
        - description: Small description about the Template.
    - tags: Any relevant tag that it is attached to the Template.
    """
    source: Source
    name: str
    description: str = Field(default="")
    tags: List[str] = Field(default_factory=list)


class TemplatesFile(BaseModel):
    """TemplatesFile.

    It is used to parse the templates_file and load the templates.
    """
    templates: Dict[str, Template] = Field(default_factory=dict)

    @validator("templates", pre=True)
    def _format_templates_by_appending_key_as_name(cls, templates):
        if not templates:
            return {}
        return {
            name: {
                **template,
                "name": name
            }
            for name, template in templates.items()
        }
