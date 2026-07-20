from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
)


class NewTournamentDialog(QDialog):
    """
    Dialog used to collect the basic information required
    to create a new tournament.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New Tournament")
        self.setMinimumWidth(450)

        self._create_ui()

    def _create_ui(self):
        """Create the dialog interface."""

        layout = QFormLayout()

        # Tournament name
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Example: Summer Chess Open")

        # Tournament system
        self.system_combo = QComboBox()
        self.system_combo.addItems([
            "Swiss",
            "Round Robin",
            "Single Elimination",
            "Double Elimination",
        ])

        # Number of participants
        self.participants_spin = QSpinBox()
        self.participants_spin.setMinimum(2)
        self.participants_spin.setMaximum(10000)
        self.participants_spin.setValue(8)

        # Add fields
        layout.addRow("Tournament Name:", self.name_edit)
        layout.addRow("Tournament System:", self.system_combo)
        layout.addRow("Participants:", self.participants_spin)

        # OK / Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_tournament_data(self):
        """Return the data entered by the user."""

        return {
            "name": self.name_edit.text().strip(),
            "system": self.system_combo.currentText(),
            "participants": self.participants_spin.value(),
        }