from chess.views.view_menu import Views
from chess.views.view_player import ViewsPlayer
from chess.controllers.player import PlayerController


class AppController:
    """Menu management"""

    def __init__(self):
        self.views = Views()
        self.playerviews = ViewsPlayer()

    def start(self):
        """Display main menu and user choice"""
        player = PlayerController()
        exit_requested = False

        while not exit_requested:
            choice = self.views.display_main_menu()

            if choice == "1":
                # Player management
                print("Player Management")
                print("")
                player.start()

            if choice == "2":
                # Tournament management
                print("Tournament management")

            if choice == "3":
                # exit
                exit_requested = True
                print("exit")
                break
