from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

from ui.components.theme import Theme


class VBox(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSpacing(Theme.MD)
        self.setContentsMargins(
            Theme.LG,
            Theme.LG,
            Theme.LG,
            Theme.LG,
        )


class HBox(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSpacing(Theme.MD)