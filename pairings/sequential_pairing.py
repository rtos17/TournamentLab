from models.match import Match
from models.round import Round


class SequentialPairingEngine:
    def generate_round(self, tournament):
        round_ = Round(tournament.round_count + 1)

        participants = tournament.participants

        for i in range(0, len(participants), 2):

            player1 = participants[i]

            if i + 1 < len(participants):
                player2 = participants[i + 1]
            else:
                player2 = None

            match = Match(
                participant1=player1,
                participant2=player2,
                table=(i // 2) + 1,
            )

            round_.add_match(match)

        return round_