from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
    QGroupBox,
    QHBoxLayout,
    QListWidget,
    QPushButton,
)

from models.tournament import Tournament


class TournamentView(QWidget):
    """Workspace for an opened tournament."""
    add_participant_requested = Signal()

    def __init__(self, tournament: Tournament, parent=None):
        super().__init__(parent)

        self.tournament = tournament

        self._create_ui()

    def _create_ui(self):
        layout = QVBoxLayout(self)

        self._create_header(layout)
        self._create_participants_section(layout)
        self._create_rounds_section(layout)
        self._create_standings_section(layout)

        layout.addStretch()

        self.refresh()

    def _create_header(self, layout):
        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignCenter)

        self.system_label = QLabel()

        self.participant_count_label = QLabel()

        layout.addWidget(self.title_label)
        layout.addWidget(self.system_label)
        layout.addWidget(self.participant_count_label)

        self.refresh_header()

    def refresh_header(self):
        self.title_label.setText(self.tournament.name)

        self.system_label.setText(
            f"System: {self.tournament.system}"
        )

        current = len(self.tournament.participants)
        expected = self.tournament.participant_count

        self.participant_count_label.setText(
            f"Participants: {current} / {expected}"
        )

    def _create_participants_section(self, layout):
        group = QGroupBox("Participants")

        group_layout = QVBoxLayout(group)

        self.participant_list = QListWidget()

        group_layout.addWidget(self.participant_list)

        button_layout = QHBoxLayout()

        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.remove_button = QPushButton("Remove")
        self.import_button = QPushButton("Import")

        self.add_button.clicked.connect(
            self.add_participant_requested.emit
        )

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.import_button)

        group_layout.addLayout(button_layout)

        layout.addWidget(group)

    def refresh_participants(self):
        self.participant_list.clear()

        if not self.tournament.participants:
            self.participant_list.addItem("(No participants yet)")
            return
        
        for participant in self.tournament.participants:
            self.participant_list.addItem(participant.name)


    def _create_rounds_section(self, layout):
        group = QGroupBox("Rounds")

        group_layout = QVBoxLayout(group)

        group_layout.addWidget(
            QLabel("No rounds generated yet.")
        )

        layout.addWidget(group)

    def _create_standings_section(self, layout):
        group = QGroupBox("Standings")

        group_layout = QVBoxLayout(group)

        group_layout.addWidget(
            QLabel("No standings available.")
        )

        layout.addWidget(group)

    def refresh(self):
        self.refresh_header()
        self.refresh_participants()