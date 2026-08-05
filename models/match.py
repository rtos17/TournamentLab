from models.participant import Participant


class Match:
    def __init__(
        self,
        participant1: Participant,
        participant2: Participant | None,
        table: int | None = None,
    ):
        self.participant1 = participant1
        self.participant2 = participant2

        self.table = table

        self.score1 = None
        self.score2 = None

        self.winner = None

    def set_result(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

        if self.is_bye:
            self.winner = self.participant1
            return

        if score1 > score2:
            self.winner = self.participant1
        elif score2 > score1:
            self.winner = self.participant2
        else:
            self.winner = None

    @property
    def finished(self):
        return self.is_bye or self.winner is not None

    @property
    def is_bye(self):
        return self.participant2 is None

    @property
    def loser(self):
        if not self.finished:
            return None

        if self.is_bye:
            return None

        if self.winner == self.participant1:
            return self.participant2

        if self.winner == self.participant2:
            return self.participant1

        return None