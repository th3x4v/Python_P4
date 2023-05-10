from chess.views.view_player import ViewsPlayer
from chess.models.player import Player
from chess.models import player


class PlayerController:
    """Player management"""

    def __init__(self):
        self.views = ViewsPlayer()
        self.player = Player()
        self.player_to_modify = Player()

    def start(self):
        """Display player menu and user choice"""

        print("The player database is : ")
        players_database = player.player_database
        print("test")
        print(players_database)
        print("test")
        self.views.display_player_list(players_database)

        choice = self.views.display_player_menu()

        if choice == "1":
            # Add players
            print("Add players")
            self.add_player()

        if choice == "2":
            # modifiy player
            print("modifiy player")
            self.modify_player()

        if choice == "3":
            # exit
            print("exit")

    def add_player(self):
        """add a player to the player list"""
        self.player = self.views.display_add_player()
        print(self.player)
        serialized_player = self.player.serialize_player()
        print(serialized_player)
        self.player.update_player_database(serialized_player)
        self.start()

    def modify_player(self):
        id = [int(self.views.display_modify_player())]
        self.player = self.views.display_add_player()
        serialized_player = self.player.serialize_player()
        self.player.modify_player(serialized_player, id)
        self.start()
