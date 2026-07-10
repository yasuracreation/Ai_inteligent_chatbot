from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class DocumentChunk:
    id: str
    document_id: str
    text: str
    metadata: Dict[str, Any] = field(default_factory=dict)
