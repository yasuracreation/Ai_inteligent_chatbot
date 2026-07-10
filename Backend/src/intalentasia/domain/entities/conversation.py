from dataclasses import dataclass, field
from typing import List

from intalentasia.domain.entities.message import Message


@dataclass
class Conversation:
    thread_id: str
    messages: List[Message] = field(default_factory=list)
