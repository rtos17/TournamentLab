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
from ui.widgets.tournament_header import TournamentHeader
from ui.widgets.participants_panel import ParticipantsPanel
from ui.widgets.rounds_panel import RoundsPanel


class TournamentView(QWidget):
    """Workspace for an opened tournament."""
    add_participant_requested = Signal()
    edit_participant_requested = Signal(object)
    remove_participant_requested = Signal(object)
    import_csv_requested = Signal()
    generate_round_requested = Signal()
    result_requested = Signal(object)

    def __init__(self, tournament: Tournament, parent=None):
        super().__init__(parent)

        self.tournament = tournament

        self._create_ui()

    def _create_ui(self):
        layout = QVBoxLayout(self)

        self._build_header(layout)
        self._build_participants(layout)
        self._build_rounds(layout)
        self._build_standings(layout)

        layout.addStretch()

        self.refresh()

    def _build_header(self, layout):
        self.header = TournamentHeader(self.tournament)
        layout.addWidget(self.header)

    def _build_participants(self, layout):
        self.participants_panel = ParticipantsPanel(self.tournament)

        self.participants_panel.add_participant_requested.connect(
            self.add_participant_requested
        )

        self.participants_panel.edit_participant_requested.connect(
            self.edit_participant_requested
        )

        self.participants_panel.remove_participant_requested.connect(
            self.remove_participant_requested
        )

        self.participants_panel.import_csv_requested.connect(
            self.import_csv_requested
        )

        self.participants_panel.generate_round_requested.connect(
            self.generate_round_requested
        )

        layout.addWidget(self.participants_panel)

    def _build_rounds(self, layout):
        self.rounds_panel = RoundsPanel(self.tournament)

        self.rounds_panel.result_requested.connect(
            self.result_requested.emit
        )

        layout.addWidget(self.rounds_panel)

    def _build_standings(self, layout):
        group = QGroupBox("Standings")

        group_layout = QVBoxLayout(group)

        group_layout.addWidget(
            QLabel("No standings available.")
        )

        layout.addWidget(group)

    def refresh(self):
        self.header.refresh()
        self.participants_panel.refresh()
        self.rounds_panel.refresh()