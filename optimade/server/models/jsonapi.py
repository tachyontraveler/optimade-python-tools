"""
This module should reproduce https://jsonapi.org/schema
"""
from typing import Optional, List, Union

from pydantic import BaseModel, UrlStr


class Link(BaseModel):
    href: UrlStr
    meta: Optional[dict]

class Links(BaseModel):
    next: Optional[Link]

class Resource(BaseModel):
    id: str
    type: str
    links: Optional[Links]
    meta: Optional[dict]

class Jsonapi(BaseModel):
    version: str
    meta: Optional[dict]

class Pagination(BaseModel):
    first: Optional[Union[UrlStr, None]]
    last: Optional[Union[UrlStr, None]]
    prev: Optional[Union[UrlStr, None]]
    next: Optional[Union[UrlStr, None]]

class Error(BaseModel):
    id: str
    status: str
    code: str
    title: str
    detail: str
    meta: dict

class Success(BaseModel):
    data: Union[None, Resource, List[Resource]]
    included: Optional[List[Resource]]
    uniqueItems: bool = True
    meta: Optional[dict]
    links: Optional[Union[Links, Pagination]]
    jsonapi: Optional[Jsonapi]

class Failure(BaseModel):
    errors: List[Error]
    meta: Optional[dict]
    jsonapi: Optional[Jsonapi]
    links: Optional[Links]

class Info(BaseModel):
    meta: dict
    jsonapi: Optional[Jsonapi]
    links: Optional[Links]

class RelationshipLinks(BaseModel):
    self: Optional[Link]
    related: Optional[Link]

class Linkage(BaseModel):
    type: str
    id: str
    meta: Optional[dict]
