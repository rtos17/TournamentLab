from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QToolBar
)
from ui.views.welcome_view import WelcomeView
from ui.views.tournament_view import TournamentView
from ui.dialogs.new_tournament_dialog import NewTournamentDialog
from services.tournament_service import TournamentService
from ui.dialogs.add_participant_dialog import AddParticipantDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tournament_service = TournamentService()
        self.current_tournament = None
        self.setWindowTitle("Tournament Lab — v0.1.0-alpha")
        self.resize(1000, 700)

        self._create_ui()

    def _create_ui(self):
        self.welcome_view = WelcomeView()

        self.welcome_view.new_tournament_requested.connect(
            self.open_new_tournament_dialog
        )

        self.setCentralWidget(self.welcome_view)

        self.addToolBar(QToolBar("Main"))

        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")

    def show_tournament_view(self):
        self.tournament_view = TournamentView(self.current_tournament)

        self.tournament_view.add_participant_requested.connect(
            self.open_add_participant_dialog
        )

        self.setCentralWidget(self.tournament_view)

    def open_new_tournament_dialog(self):
        dialog = NewTournamentDialog(self)

        if dialog.exec():
            tournament_data = dialog.get_tournament_data()

            self.current_tournament = self.tournament_service.create_tournament(
                tournament_data["name"],
                tournament_data["system"],
                tournament_data["participant_count"],
            )

            self.show_tournament_view()


    def open_add_participant_dialog(self):
        dialog = AddParticipantDialog(self)

        if dialog.exec():
            participant_data = dialog.get_participant_data()

            self.tournament_service.add_participant(
                self.current_tournament,
                participant_data["name"],
                participant_data["seed"],
            )
            self.tournament_view.refresh()