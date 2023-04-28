from pydantic import BaseModel, Field, validator, root_validator
from pathlib import Path
from typing import List, Dict, Literal, Optional


class Source(BaseModel):
    type: Literal["local", "git"]
    path: str
    ref: Optional[str] = None

    @root_validator(pre=True)
    def alter_object_if_path_is_local(cls, values):
        if values["type"] == "local":
            values["ref"] = None
            values["path"] = str(Path(values["path"]).resolve())
        return values


class Template(BaseModel):
    source: Source
    name: str
    description: str = Field(default="")
    tags: List[str] = Field(default_factory=list)


class TemplatesFile(BaseModel):
    templates: Dict[str, Template] = Field(default_factory=dict)

    @validator("templates", pre=True)
    def format_templates_by_appending_key_as_name(cls, templates):
        if not templates:
            return {}
        return {
            name: {
                **template,
                "name": name
            }
            for name, template in templates.items()
        }
