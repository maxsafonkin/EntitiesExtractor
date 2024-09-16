from dataclasses import dataclass, asdict

from .tags import Tag


@dataclass
class NamedEntity:
    tag: Tag
    text: str

    def to_dict(self) -> dict:
        return asdict(self)
