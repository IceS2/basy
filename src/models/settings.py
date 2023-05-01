"""Basy Settings. Any configuration needed for basy to work."""
from pathlib import Path

from pydantic import BaseSettings, Field


class BasyBaseSettings(BaseSettings):
    """Base class to set some common configuration."""
    class Config:
        """Configures the env_prefix and env_nested_delimiter.

        Refer to pydantic documentation here:
        https://docs.pydantic.dev/latest/usage/settings/
        """
        env_prefix = "basy_"
        env_nested_delimiter = "__"


class Settings(BasyBaseSettings):
    """Basy Settings.

    We need to set the following settings:
        - root_dir: Directory to store the Basy files at.
        - templates_file: File to store the templates at.
    It will be created inside the root_dir.
    """
    root_dir: Path = Field(default=f"{Path.home()}/.basy")
    templates_file: str = Field(default="templates.yaml")
