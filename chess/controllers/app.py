from chess.views.view_menu import Views
from chess.views.view_player import ViewsPlayer
from chess.controllers.player import PlayerController
from chess.controllers.tournament import TournamentController


class AppController:
    """Menu management"""

    def __init__(self):
        self.views = Views()
        self.playerviews = ViewsPlayer()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def start(self):
        """Display main menu and user choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.views.display_main_menu()

            if choice == "1":
                # Player management
                print("Player Management")
                print("")
                self.player_controller.start()

            if choice == "2":
                # Tournament management
                print("Tournament management")
                print("")
                self.tournament_controller.start()

            if choice == "3":
                # exit
                exit_requested = True
                print("exit")
                break
