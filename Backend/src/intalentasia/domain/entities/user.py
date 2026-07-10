from dataclasses import dataclass

from intalentasia.domain.value_objects.role import Role


@dataclass
class User:
    email: str
    role: Role
