from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QVBoxLayout,
)

from models.match import Match


class ResultDialog(QDialog):

    def __init__(self, match: Match, parent=None):
        super().__init__(parent)

        self.match = match

        self.setWindowTitle("Enter Result")

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel(f"Table {match.table}")
        )

        if match.is_bye:
            layout.addWidget(
                QLabel(
                    f"{match.participant1.name} receives a BYE."
                )
            )
        else:
            form = QFormLayout()

            self.score1 = QDoubleSpinBox()
            self.score2 = QDoubleSpinBox()

            for spin in (self.score1, self.score2):
                spin.setRange(0, 1)
                spin.setSingleStep(0.5)

            form.addRow(
                match.participant1.name,
                self.score1,
            )

            form.addRow(
                match.participant2.name,
                self.score2,
            )

            layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Save |
            QDialogButtonBox.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def get_result(self):
        if self.match.is_bye:
            return (1, 0)

        return (
            self.score1.value(),
            self.score2.value(),
        )