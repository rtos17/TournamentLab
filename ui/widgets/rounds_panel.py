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
from ui.widgets.base.panel import Panel


class RoundsPanel(Panel):

    result_requested = Signal(object)
    def __init__(self, tournament: Tournament, parent=None):
        super().__init__("Rounds", parent)

        self.tournament = tournament

        self.tree = QTreeWidget()

        self.tree.setHeaderLabels(
            ["Round / Match"]
        )

        self.tree.setRootIsDecorated(True)
        self.tree.setAlternatingRowColors(True)

        self.layout.addWidget(self.tree)

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