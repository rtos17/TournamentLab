from dataclasses import dataclass

from models.participant import Participant


@dataclass
class Standing:
    participant: Participant

    points: float = 0.0

    wins: int = 0
    draws: int = 0
    losses: int = 0

    byes: int = 0

    played: int = 0