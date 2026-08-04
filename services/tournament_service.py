from datetime import datetime
from models.tournament import Tournament
from models.participant import Participant


class TournamentService:

    def create_tournament(self, name: str, system: str, participant_count: int) -> Tournament:
        return Tournament(
            name=name,
            system=system,
            participant_count=participant_count,
            created_at=datetime.now(),
        )

    def add_participant(self, tournament: Tournament, name: str, seed: int = 0) -> Participant:
        participant = Participant.create(name, seed)
        tournament.participants.append(participant)
        return participant

    def remove_participant(self, tournament: Tournament, participant_id: str) -> bool:
        for participant in tournament.participants:
            if participant.id == participant_id:
                tournament.participants.remove(participant)
                return True
        return False

    def get_participants(self, tournament: Tournament):
        return list(tournament.participants)

    def update_participant(self, participant, name):
        """
        Update an existing participant.
        """
        participant.name = name.strip()

        return participant