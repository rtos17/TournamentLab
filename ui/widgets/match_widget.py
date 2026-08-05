from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
)

from models.match import Match


class MatchWidget(QWidget):

    result_requested = Signal(object)

    def __init__(self, match: Match, parent=None):
        super().__init__(parent)

        self.match = match

        layout = QHBoxLayout(self)

        table = QLabel(f"Table {match.table}")

        if match.is_bye:
            players = QLabel(
                f"{match.participant1.name} (BYE)"
            )
        else:
            players = QLabel(
                f"{match.participant1.name}  vs  {match.participant2.name}"
            )

        self.result_button = QPushButton("Enter Result")

        self.result_button.clicked.connect(
            self._emit_result_requested
        )

        layout.addWidget(table)
        layout.addStretch()
        layout.addWidget(players)
        layout.addStretch()
        layout.addWidget(self.result_button)

    def _emit_result_requested(self):
        self.result_requested.emit(self.match)