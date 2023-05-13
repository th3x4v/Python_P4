from chess.views.view_player import ViewsPlayer
from chess.models.player import Player
from chess.models import player

player_database = player.player_database
player_table = player_database.all()
sorted_player = sorted(player_table, key=lambda x: x["Last Name"])


class PlayerController:
    """Player management"""

    def __init__(self):
        self.views = ViewsPlayer()

    def start(self):
        """Display player menu and user choice"""

        choice = self.views.display_player_menu()

        if choice == "0":
            # view players
            print("Player list")
            self.views.display_player_list(sorted_player)

        if choice == "1":
            # Add players
            print("Add players")
            self.add_player()

        if choice == "2":
            # modifiy player
            print("modifiy player")
            self.views.display_player_list(player_database)
            self.modify_player()

        if choice == "3":
            # exit
            print("exit")

    def add_player(self):
        """add a player to the player list"""
        player_data: dict = self.views.get_info_player()
        player: Player = Player(**player_data)
        serialized_player = player.serialize_player()
        player.update_player_database(serialized_player)
        self.start()

    def modify_player(self):
        """modify a player in the player list"""
        id = self.views.display_modify_player()
        if id == None:
            print("you didn't validate the player you want to change")
            self.start()
        else:
            player_to_modify: dict = player_table[id]
            print(player_to_modify)
            id = [id]
            player_data = self.views.get_info_player(player_to_modify)
            player: Player = Player(**player_data)
            serialized_player = player.serialize_player()
            player.modify_player(serialized_player, id)
            self.start()
