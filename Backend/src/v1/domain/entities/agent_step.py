from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class AgentStep:
    node_name: str
    status: str
    timestamp: datetime
    details: Dict[str, Any] = field(default_factory=dict)
