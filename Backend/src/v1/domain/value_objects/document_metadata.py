from dataclasses import dataclass
from datetime import date

from intalentasia.domain.value_objects.access_level import AccessLevel


@dataclass(frozen=True)
class DocumentMetadata:
    department: str
    document_type: str
    access_level: AccessLevel
    created_date: date
    title: str
