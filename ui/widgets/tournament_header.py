from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from models.tournament import Tournament


class TournamentHeader(QWidget):
    def __init__(self, tournament: Tournament, parent=None):
        super().__init__(parent)

        self.tournament = tournament

        layout = QVBoxLayout(self)

        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet(
            "font-size:22px; font-weight:bold;"
        )

        self.system_label = QLabel()
        self.system_label.setStyleSheet(
            "color: gray;"
        )

        self.participant_count_label = QLabel()
        self.participant_count_label.setStyleSheet(
            "font-weight:bold;"
        )

        layout.addWidget(self.title_label)
        layout.addWidget(self.system_label)
        layout.addWidget(self.participant_count_label)

        self.refresh()

    def refresh(self):
        self.title_label.setText(self.tournament.name)

        self.system_label.setText(
            f"System: {self.tournament.system}"
        )

        current = len(self.tournament.participants)
        expected = self.tournament.participant_count

        self.participant_count_label.setText(
            f"Participants: {current} / {expected}"
        )