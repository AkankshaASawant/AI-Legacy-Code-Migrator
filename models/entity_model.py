from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Entity:
    name: str
    fields: List[Dict] = field(default_factory=list)
    methods: List[Dict] = field(default_factory=list)
    relationships: Dict[str, str] = field(default_factory=dict)
    business_rules: List[str] = field(default_factory=list)
