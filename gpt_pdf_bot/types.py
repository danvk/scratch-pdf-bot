from dataclasses import dataclass, field
from typing import Any, List, Dict

from dataclasses_jsonschema import JsonSchemaMixin

@dataclass
class Chunk(JsonSchemaMixin):
    text: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Page(JsonSchemaMixin):
    text: str
    page_num: int


@dataclass
class Document(JsonSchemaMixin):
    source: str
    metadata: Dict[str, Any]
    pages: List[Page] = field(default_factory=list)
