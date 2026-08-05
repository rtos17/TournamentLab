from PySide6.QtWidgets import QGroupBox


class SectionGroup(QGroupBox):
    def __init__(self, title="", parent=None):
        super().__init__(title, parent)