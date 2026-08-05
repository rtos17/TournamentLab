from models.match import Match


class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []

    def add_match(self, match: Match):
        self.matches.append(match)

    @property
    def finished(self):
        return all(match.finished for match in self.matches)

    def __len__(self):
        return len(self.matches)