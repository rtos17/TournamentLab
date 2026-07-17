from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class NewTournamentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New Tournament")
        self.setMinimumWidth(400)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Tournament creation is coming soon."))

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)

        layout.addWidget(ok_button)

        self.setLayout(layout)