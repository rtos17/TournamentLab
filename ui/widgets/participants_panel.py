from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QPushButton,
)

from models.tournament import Tournament
from ui.widgets.base.panel import Panel


class ParticipantsPanel(Panel):

    add_participant_requested = Signal()
    edit_participant_requested = Signal(object)
    remove_participant_requested = Signal(object)
    import_csv_requested = Signal()
    generate_round_requested = Signal()

    def __init__(self, tournament: Tournament, parent=None):
        super().__init__("Participants", parent)

        self.tournament = tournament

        self.participant_list = QListWidget()

        self.participant_list.itemSelectionChanged.connect(
            self._on_participant_selected
        )

        self.layout.addWidget(self.participant_list)

        button_layout = QHBoxLayout()

        self.add_button = QPushButton("Add Participant")
        self.edit_button = QPushButton("Edit Participant")
        self.remove_button = QPushButton("Remove Participant")
        self.import_csv_button = QPushButton("Import CSV")
        self.generate_round_button = QPushButton("Generate Round")

        self.edit_button.setEnabled(False)
        self.remove_button.setEnabled(False)

        self.add_button.clicked.connect(
            self.add_participant_requested.emit
        )

        self.edit_button.clicked.connect(
            self._emit_edit_participant
        )

        self.remove_button.clicked.connect(
            self._emit_remove_participant
        )

        self.import_csv_button.clicked.connect(
            self.import_csv_requested.emit
        )

        self.generate_round_button.clicked.connect(
            self.generate_round_requested.emit
        )

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.import_csv_button)
        button_layout.addWidget(self.generate_round_button)

        self.layout.addLayout(button_layout)

        self.refresh()

    def refresh(self):
        self.participant_list.clear()

        if not self.tournament.participants:
            self.participant_list.addItem("(No participants yet)")
            return

        for participant in self.tournament.participants:
            self.participant_list.addItem(participant.name)

    def _on_participant_selected(self):
        has_selection = len(self.participant_list.selectedItems()) > 0

        self.edit_button.setEnabled(has_selection)
        self.remove_button.setEnabled(has_selection)

    def _emit_edit_participant(self):
        row = self.participant_list.currentRow()

        if row < 0:
            return

        participant = self.tournament.participants[row]

        self.edit_participant_requested.emit(participant)

    def _emit_remove_participant(self):
        row = self.participant_list.currentRow()

        if row < 0:
            return

        participant = self.tournament.participants[row]

        self.remove_participant_requested.emit(participant)