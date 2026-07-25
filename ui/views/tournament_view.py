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

        layout.addStretch()

    def _create_header(self, layout):
        title = QLabel(self.tournament.name)
        title.setAlignment(Qt.AlignCenter)

        system = QLabel(f"System: {self.tournament.system}")

        participant_count = QLabel(
            f"Expected participants: {self.tournament.participant_count}"
        )

        layout.addWidget(title)
        layout.addWidget(system)
        layout.addWidget(participant_count)

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

        self.refresh_participants()

    def refresh_participants(self):
        self.participant_list.clear()

        if not self.tournament.participants:
            self.participant_list.addItem("(No participants yet)")
            return

        for participant in self.tournament.participants:
            self.participant_list.addItem(participant.name)