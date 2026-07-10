from dataclasses import dataclass

from intalentasia.domain.value_objects.document_metadata import DocumentMetadata


@dataclass
class Document:
    id: str
    title: str
    content: str
    metadata: DocumentMetadata
