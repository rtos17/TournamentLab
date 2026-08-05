from PySide6.QtWidgets import QPushButton

from ui.components.theme import Theme


class PrimaryButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setMinimumHeight(30)

        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {Theme.PRIMARY};
                color: white;
                border: none;
                border-radius: {Theme.RADIUS_MD}px;
                padding: 6px 12px;
                font-weight: 600;
            }}

            QPushButton:hover {{
                background-color: #1D4ED8;
            }}

            QPushButton:pressed {{
                background-color: #1E40AF;
            }}
            """
        )


class SecondaryButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setMinimumHeight(30)

        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {Theme.SURFACE};
                color: {Theme.TEXT};
                border: 1px solid {Theme.BORDER};
                border-radius: {Theme.RADIUS_MD}px;
                padding: 6px 12px;
            }}

            QPushButton:hover {{
                background-color: {Theme.BACKGROUND};
            }}
            """
        )