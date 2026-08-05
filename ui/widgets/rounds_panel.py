from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QTreeWidget,
    QTreeWidgetItem,
)

from models.tournament import Tournament
from ui.widgets.match_widget import MatchWidget


class RoundsPanel(QWidget):

    result_requested = Signal(object)
    def __init__(self, tournament: Tournament, parent=None):
        super().__init__(parent)

        self.tournament = tournament

        layout = QVBoxLayout(self)

        group = QGroupBox("Rounds")
        group_layout = QVBoxLayout(group)

        self.tree = QTreeWidget()

        self.tree.setHeaderLabels(
            ["Round / Match"]
        )

        self.tree.setRootIsDecorated(True)
        self.tree.setAlternatingRowColors(True)

        group_layout.addWidget(self.tree)

        layout.addWidget(group)

        self.refresh()

    def refresh(self):
        self.tree.clear()

        if not self.tournament.rounds:
            item = QTreeWidgetItem(
                ["No rounds generated yet."]
            )

            self.tree.addTopLevelItem(item)
            return

        for round_ in self.tournament.rounds:

            round_item = QTreeWidgetItem(
                [f"Round {round_.number}"]
            )

            self.tree.addTopLevelItem(round_item)

            for match in round_.matches:

                if match.is_bye:
                    text = (
                        f"Table {match.table} — "
                        f"{match.participant1.name} (BYE)"
                    )
                else:
                    text = (
                        f"Table {match.table} — "
                        f"{match.participant1.name}"
                        f" vs "
                        f"{match.participant2.name}"
                    )

                match_item = QTreeWidgetItem()

                round_item.addChild(match_item)

                widget = MatchWidget(match)

                widget.result_requested.connect(
                    self.result_requested.emit
                )

                self.tree.setItemWidget(
                    match_item,
                    0,
                    widget,
                )

            round_item.setExpanded(True)