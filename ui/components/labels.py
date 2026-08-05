from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from ui.components.theme import Theme


class TitleLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(
            f"""
            font-size:{Theme.TITLE_SIZE}px;
            font-weight:bold;
            color:{Theme.TEXT};
            """
        )


class InfoLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(
            f"""
            color:{Theme.TEXT_SECONDARY};
            """
        )