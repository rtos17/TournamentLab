from dataclasses import dataclass
import uuid


@dataclass
class Participant:
    id: str
    name: str
    seed: int = 0

    @staticmethod
    def create(name: str, seed: int = 0) -> "Participant":
        return Participant(
            id=str(uuid.uuid4()),
            name=name.strip(),
            seed=seed,
        )