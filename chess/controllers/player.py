from chess.views.view_player import ViewsPlayer
from chess.views.view_menu import Views
from chess.models.player import Player
from chess.database.database import player_database


class PlayerController:
    """Player management"""

    def __init__(self):
        self.views = ViewsPlayer()
        self.views_menu = Views()

    def start(self):
        """Display player menu and user choice"""

        choice = self.views_menu.display_menu(
            title1="player menu",
            choice0="0 - Player list",
            choice1="1 - Add a player",
            choice2="2 - Modify a player",
            choice3="3 - Back",
        )

        if choice == "0":
            # view players
            print("Player list")
            sorted_player = player_database.sort_players_by_name()

            self.views_menu.display_list(sorted_player, header="keys")
            self.start()

        if choice == "1":
            # Add players
            print("Add players")
            self.add_player()
            self.start()

        if choice == "2":
            # modifiy player
            print("modifiy player")
            self.views_menu.display_list(player_database.all(), header="keys")
            self.modify_player(player_database)
            self.start()

        if choice == "3":
            # exit
            print("exit")

    def add_player(self):
        """add a player to the player list"""
        player_data: dict = self.views.get_info_player()
        player: Player = Player(**player_data)
        player.id = player.add_player_database()
        player.modify_player(player.id)
        self.start()

    def modify_player(self, player_table):
        """modify a player in the player list"""
        id = self.views.get_modify_player()
        if id is None:
            print("you didn't validate the player you want to change")
            self.start()
        else:
            player_to_modify: Player = Player.get_player_info(id)
            player_to_modify_serialize = player_to_modify.serialize()
            player_data = self.views.get_info_player(player_to_modify_serialize)
            player_to_modify = Player(**player_data)
            player_to_modify.modify_player(id)
            self.start()
