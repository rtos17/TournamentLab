from services.standings.standing import Standing


class StandingsCalculator:

    @staticmethod
    def calculate(tournament):

        standings = {
            participant.id: Standing(participant)
            for participant in tournament.participants
        }

        for round_ in tournament.rounds:

            for match in round_.matches:

                if not match.finished:
                    continue

                p1 = standings[match.participant1.id]

                p1.played += 1

                if match.is_bye:
                    p1.points += 1
                    p1.wins += 1
                    p1.byes += 1
                    continue

                p2 = standings[match.participant2.id]

                p2.played += 1

                if match.is_draw:

                    p1.points += 0.5
                    p2.points += 0.5

                    p1.draws += 1
                    p2.draws += 1

                elif match.winner == match.participant1:

                    p1.points += 1

                    p1.wins += 1
                    p2.losses += 1

                else:

                    p2.points += 1

                    p2.wins += 1
                    p1.losses += 1

        return sorted(
            standings.values(),
            key=lambda s: (-s.points, s.participant.seed)
        )