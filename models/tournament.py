from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from models.participant import Participant


@dataclass
class Tournament:
    name: str
    system: str
    participant_count: int
    created_at: datetime
    participants: List[Participant] = field(default_factory=list)