# See https://pypi.org/project/dataclasses-jsonschema/#below

from dataclasses import dataclass
import sys
import json
from typing import Tuple, TypeVar

from dataclasses_jsonschema import JsonSchemaMixin

from gpt_pdf_bot.types import Document

@dataclass
class DocumentEndpoint(JsonSchemaMixin):
    get: Document
    post: Tuple[Document, Document]

@dataclass
class API(JsonSchemaMixin):
    docs: DocumentEndpoint
    '''/document/:document_id'''

json.dump(API.json_schema(), sys.stdout, indent=2)
