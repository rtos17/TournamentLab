from models.tournament import Tournament


class TournamentService:
    """Business logic related to tournaments."""

    @staticmethod
    def create_tournament(data: dict) -> Tournament:
        """
        Create a Tournament from dialog data.
        """

        return Tournament(
            name=data["name"],
            system=data["system"],
            participant_count=data["participants"],
        )