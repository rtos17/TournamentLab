from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
)


class AddParticipantDialog(QDialog):
    def __init__(self, parent=None, participant=None):
        super().__init__(parent)

        self.participant = participant

        layout = QFormLayout(self)

        self.name_edit = QLineEdit()

        self.seed_spin = QSpinBox()
        self.seed_spin.setMinimum(0)
        self.seed_spin.setMaximum(9999)

        if self.participant is not None:
            self.setWindowTitle("Edit Participant")

            self.name_edit.setText(self.participant.name)
            self.seed_spin.setValue(self.participant.seed)

        else:
            self.setWindowTitle("Add Participant")

        layout.addRow("Name", self.name_edit)
        layout.addRow("Seed", self.seed_spin)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def get_participant_data(self):
        return {
            "name": self.name_edit.text().strip(),
            "seed": self.seed_spin.value(),
        }