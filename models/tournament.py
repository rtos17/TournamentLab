from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from models.participant import Participant
from models.round import Round


@dataclass
class Tournament:
    name: str
    system: str
    participant_count: int
    created_at: datetime

    participants: List[Participant] = field(default_factory=list)
    rounds: List[Round] = field(default_factory=list)

    def add_round(self, round_: Round):
        self.rounds.append(round_)

    @property
    def current_round(self):
        if not self.rounds:
            return None

        return self.rounds[-1]

    @property
    def round_count(self):
        return len(self.rounds)