from chess.views.view_player import ViewsPlayer
from chess.models.player import Player
from chess.models import player


class PlayerController:
    """Player management"""

    def __init__(self):
        self.views = ViewsPlayer()
        self.player = Player()

    def start(self):
        """Display player menu and user choice"""

        print("The player database is : ")
        players_database = player.player_database
        self.views.display_player_list(players_database)

        choice = self.views.display_player_menu()

        if choice == "1":
            # Upload players list
            print("Upload players list")

        if choice == "2":
            # Add players
            print("Add players")
            self.add_player()

        if choice == "3":
            # Save players list
            print("Save players list")

        if choice == "4":
            # exit
            print("exit")

    def add_player(self):
        """add a player to the player list"""
        newplayer = self.views.display_add_player()
        print(newplayer)
        self.start()
