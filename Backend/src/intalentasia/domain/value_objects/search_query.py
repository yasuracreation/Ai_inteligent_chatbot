from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(frozen=True)
class SearchQuery:
    text: str
    filters: Dict[str, Any] = field(default_factory=dict)
    top_k: int = 5
    alpha: float = 0.5
