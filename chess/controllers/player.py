from chess.views.view_player import ViewsPlayer


class PlayerController:
    """Player management"""

    def __init__(self):
        self.views = ViewsPlayer()

    def start(self):
        """Display player menu and user choice"""

        choice = self.views.display_player_menu()

        if choice == "1":
            # Upload players list
            print("Upload players list")

        if choice == "2":
            # Add players
            print("Add players")

        if choice == "3":
            # Save players list
            print("Save players list")

        if choice == "4":
            # exit
            print("exit")
            
