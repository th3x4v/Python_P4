from chess.views.view_player import ViewsPlayer
from chess.models.player import Player
from chess.database.database import TinyTableManager, player_database


class PlayerController:
    """Player management"""

    def __init__(self):
        self.views = ViewsPlayer()

    def start(self):
        """Display player menu and user choice"""

        # player_table = TinyTableManager.load_player_db()

        choice = self.views.display_player_menu()

        if choice == "0":
            # view players
            print("Player list")
            sorted_player = player_database.sort_players_by_name()
            self.views.display_player_list(sorted_player)

        if choice == "1":
            # Add players
            print("Add players")
            self.add_player()

        if choice == "2":
            # modifiy player
            print("modifiy player")
            self.views.display_player_list(player_database)
            self.modify_player(player_database)

        if choice == "3":
            # exit
            print("exit")

    def add_player(self):
        """add a player to the player list"""
        player_data: dict = self.views.get_info_player()
        player: Player = Player(**player_data)
        player.add_player_database()
        self.start()

    def modify_player(self, player_table):
        """modify a player in the player list"""
        id = self.views.get_modify_player()
        if id == None:
            print("you didn't validate the player you want to change")
            self.start()
        else:
            player_to_modify: dict = player_table[id]
            print(player_to_modify)
            id = [id + 1]
            player_data = self.views.get_info_player(player_to_modify)
            player: Player = Player(**player_data)
            player.modify_player(id)
            self.start()
