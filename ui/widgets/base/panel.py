from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QVBoxLayout,
)


class Panel(QWidget):
    """
    Base class for all panels in Tournament Lab.
    """

    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        root_layout = QVBoxLayout(self)

        self.group = QGroupBox(title)

        self.layout = QVBoxLayout(self.group)

        root_layout.addWidget(self.group)

    def refresh(self):
        """
        Override in subclasses.
        """
        pass