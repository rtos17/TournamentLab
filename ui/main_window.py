from PySide6.QtWidgets import QLabel, QMainWindow
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tournament Lab")
        self.resize(1000, 700)

        label = QLabel("Welcome to Tournament Lab!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)