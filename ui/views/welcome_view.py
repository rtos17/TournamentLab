from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WelcomeView(QWidget):
    """Home screen displayed when no tournament is open."""

    new_tournament_requested = Signal()
    open_tournament_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("🏆 Tournament Lab")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("A laboratory for competitive systems")
        subtitle.setAlignment(Qt.AlignCenter)

        new_button = QPushButton("New Tournament")
        open_button = QPushButton("Open Tournament")

        new_button.setFixedWidth(220)
        open_button.setFixedWidth(220)

        new_button.clicked.connect(self.new_tournament_requested)
        open_button.clicked.connect(self.open_tournament_requested)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(new_button, alignment=Qt.AlignCenter)
        layout.addWidget(open_button, alignment=Qt.AlignCenter)