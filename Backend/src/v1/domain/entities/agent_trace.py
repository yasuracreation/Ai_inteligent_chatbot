from dataclasses import dataclass, field
from typing import Any, Dict, List

from intalentasia.domain.entities.agent_step import AgentStep


@dataclass
class AgentTrace:
    steps: List[AgentStep] = field(default_factory=list)
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
