from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QToolBar,
    QMessageBox,
    QFileDialog
)
from ui.views.welcome_view import WelcomeView
from ui.views.tournament_view import TournamentView
from ui.dialogs.new_tournament_dialog import NewTournamentDialog
from services.tournament_service import TournamentService
from ui.dialogs.add_participant_dialog import AddParticipantDialog
from services.import_service import ImportService
from ui.dialogs.result_dialog import ResultDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Services
        self.tournament_service = TournamentService()
        self.import_service = ImportService()

        # Application state
        self.current_tournament = None

        # Window
        self.setWindowTitle("Tournament Lab — v0.1.0-alpha")
        self.resize(1000, 700)

        # UI
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
        self.tournament_view.edit_participant_requested.connect(
            self.on_edit_participant
        )
        self.tournament_view.remove_participant_requested.connect(
            self.on_remove_participant
        )
        self.tournament_view.import_csv_requested.connect(
            self.on_import_csv
        )
        self.tournament_view.generate_round_requested.connect(
            self.generate_round
        )
        self.tournament_view.result_requested.connect(
            self.enter_result
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

    def _refresh_tournament_view(self):
        """Refresh the current tournament workspace."""
        self.tournament_view.refresh()


    def _open_participant_dialog(self, participant=None):
        """
        Open the participant dialog.

        Returns the participant data dictionary or None if cancelled.
        """
        dialog = AddParticipantDialog(
            self,
            participant=participant
        )

        if dialog.exec():
            return dialog.get_participant_data()

        return None

    def open_add_participant_dialog(self):
        participant_data = self._open_participant_dialog()

        if participant_data is None:
            return

        self.tournament_service.add_participant(
            self.current_tournament,
            participant_data["name"],
            participant_data["seed"],
        )

        self._refresh_tournament_view()

    def on_edit_participant(self, participant):
        participant_data = self._open_participant_dialog(participant)

        if participant_data is None:
            return

        self.tournament_service.update_participant(
            participant,
            participant_data["name"],
            participant_data["seed"],
        )

        self._refresh_tournament_view()

    def on_remove_participant(self, participant):
        reply = QMessageBox.question(
            self,
            "Remove Participant",
            f"Are you sure you want to remove '{participant.name}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        self.tournament_service.remove_participant(
            self.current_tournament,
            participant
        )

        self._refresh_tournament_view()

    def on_import_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import Participants",
            "",
            "CSV Files (*.csv)"
        )

        if not file_path:
            return

        try:
            participants = self.import_service.import_participants(file_path)

            self.tournament_service.import_participants(
                self.current_tournament,
                participants
            )

            self._refresh_tournament_view()

            QMessageBox.information(
                self,
                "Import Complete",
                f"Imported {len(participants)} participants."
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Import Failed",
                str(e)
            )

    def generate_round(self):
        if self.current_tournament is None:
            return

        self.tournament_service.generate_round(
            self.current_tournament
        )

        self.tournament_view.refresh()

    def enter_result(self, match):

        dialog = ResultDialog(match, self)

        if dialog.exec():

            score1, score2 = dialog.get_result()

            match.set_result(score1, score2)

            self.tournament_view.refresh()