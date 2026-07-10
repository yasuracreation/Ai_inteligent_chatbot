from dataclasses import dataclass


@dataclass
class Citation:
    source_file: str
    title: str
    snippet: str
    score: float
