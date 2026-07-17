from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
from ui.dialogs.new_tournament_dialog import NewTournamentDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tournament Lab — v0.1.0-alpha")
        self.resize(1000, 700)

        self._create_ui()

    def _create_ui(self):
        """Create the main window interface."""

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        central_widget.setLayout(layout)

        # Title
        title = QLabel("🏆 Tournament Lab")
        title.setAlignment(Qt.AlignCenter)

        # Subtitle
        subtitle = QLabel("A laboratory for competitive systems")
        subtitle.setAlignment(Qt.AlignCenter)

        # Buttons
        self.new_tournament_button = QPushButton("New Tournament")
        self.open_tournament_button = QPushButton("Open Tournament")

        self.new_tournament_button.clicked.connect(
            self.open_new_tournament_dialog
        )

        self.new_tournament_button.setFixedWidth(220)
        self.open_tournament_button.setFixedWidth(220)

        # Add widgets
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(self.new_tournament_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.open_tournament_button, alignment=Qt.AlignCenter)

        # Toolbar
        self.addToolBar(QToolBar("Main"))

        # Status bar
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")

    def open_new_tournament_dialog(self):
        dialog = NewTournamentDialog(self)
        dialog.exec()