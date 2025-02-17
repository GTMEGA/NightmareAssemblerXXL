from datetime import datetime
from functools import cached_property
from typing import Dict, List, Optional

from defs import UNKNOWN, Side
from pydantic import BaseModel, Field


class ModInfo(BaseModel):
    name: str
    version: str
    tagged_at: Optional[datetime] = Field(default=None)
    repo_url: Optional[str] = Field(default=None)
    filename: Optional[str] = Field(default=None)
    download_url: Optional[str] = Field(default=None)
    browser_download_url: Optional[str] = Field(default=None)
    license: str = Field(default=UNKNOWN)
    side: Side = Field(default=Side.BOTH)
    maven: Optional[str] = Field(default=None)


class GTNHModpack(BaseModel):
    github_mods: List[ModInfo]

    @cached_property
    def _github_modmap(self) -> Dict[str, ModInfo]:
        return {mod.name: mod for mod in self.github_mods}

    def has_github_mod(self, mod_name: str):
        return mod_name in self._github_modmap

    def get_github_mod(self, mod_name: str):
        return self._github_modmap.get(mod_name)
