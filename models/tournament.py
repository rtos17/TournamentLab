from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Tournament:
    """
    Represents a tournament.

    This class stores the basic information that defines
    a tournament independently of the user interface.
    """

    name: str
    system: str
    participant_count: int

    created_at: datetime = field(default_factory=datetime.now)