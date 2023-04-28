from pydantic import BaseSettings, Field
from pathlib import Path

class BasyBaseSettings(BaseSettings):
    class Config:
        env_prefix = "basy_"
        env_nested_delimiter = "__"


class Settings(BasyBaseSettings):
    root_dir: Path = Field(default=f"{Path.home()}/.basy")
    templates_file: str = Field(default="templates.yaml")
