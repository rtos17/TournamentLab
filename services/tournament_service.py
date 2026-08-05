from datetime import datetime
from models.tournament import Tournament
from models.participant import Participant
from pairings.sequential_pairing import SequentialPairingEngine


class TournamentService:

    def __init__(self):
        self.pairing_engine = SequentialPairingEngine()

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

    def update_participant(self, participant, name, seed):
        """
        Update an existing participant.
        """
        participant.name = name.strip()
        participant.seed = seed

        return participant

    def remove_participant(self, tournament, participant):
        """
        Remove a participant from a tournament.
        """
        if participant in tournament.participants:
            tournament.participants.remove(participant)
            return True

        return False

    def import_participants(self, tournament, participants):
        """
        Import multiple participants into a tournament.
        Missing seeds are assigned automatically.
        """
        next_seed = len(tournament.participants) + 1

        for participant_data in participants:
            seed = participant_data.get("seed", next_seed)

            self.add_participant(
                tournament,
                participant_data["name"],
                seed,
            )

            next_seed += 1

    def generate_round(self, tournament):
        round_ = self.pairing_engine.generate_round(tournament)

        tournament.add_round(round_)

        return round_