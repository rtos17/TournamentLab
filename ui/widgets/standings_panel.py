from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

from services.standings.standings_calculator import StandingsCalculator
from models.tournament import Tournament
from ui.widgets.base.panel import Panel


class StandingsPanel(Panel):

    def __init__(self, tournament: Tournament, parent=None):
        super().__init__("Standings", parent)

        self.tournament = tournament

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Rank",
            "Participant",
            "Pts",
            "W",
            "D",
            "L",
        ])

        self.layout.addWidget(self.table)

        self.refresh()

    def refresh(self):

        standings = StandingsCalculator.calculate(
            self.tournament
        )

        self.table.setRowCount(len(standings))

        for row, standing in enumerate(standings):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(str(row + 1))
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    standing.participant.name
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(standing.points)
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    str(standing.wins)
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    str(standing.draws)
                )
            )

            self.table.setItem(
                row,
                5,
                QTableWidgetItem(
                    str(standing.losses)
                )
            )