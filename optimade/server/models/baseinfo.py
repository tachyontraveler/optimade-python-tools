from typing import Dict, List

from pydantic import BaseModel, UrlStr


class BaseInfoAttributes(BaseModel):
    api_version: str
    available_api_versions: Dict[str, UrlStr]
    formats: List[str] = ["json"]
    entry_types_by_format: Dict[str, List[str]]
    available_endpoints: List[str] = ["structure", "all", "info"]


class BaseInfoResource(BaseModel):
    id: str = "/"
    type: str = "info"
    attributes: BaseInfoAttributes