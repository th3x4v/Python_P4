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
        exit_requested = False
        while not exit_requested:
            choice = self.views_menu.display_menu(
                title1="player menu",
                choice0="0 - Player list",
                choice1="1 - Add a player",
                choice2="2 - Modify a player",
                choice3="3 - Back",
            )
            if choice == "0":
                # view players
                sorted_player = player_database.sort_players_by_name()
                self.views_menu.display_list(sorted_player, header="keys")

            elif choice == "1":
                # Add players
                self.add_player()

            elif choice == "2":
                # modifiy player
                self.views_menu.display_list(player_database.all(), header="keys")
                self.modify_player(player_database)

            elif choice == "3":
                # exit
                exit_requested = True

    def add_player(self):
        """add a player to the player list"""
        player_data: dict = self.views.entry_info_player()
        player: Player = Player(**player_data)
        player.add_player_database()

    def modify_player(self, player_table):
        """modify a player in the player list"""
        id = self.views.entry_modify_player()
        if id is None:
            self.views_menu.display_message(
                "you didn't validate the player you want to change"
            )
        else:
            player_to_modify: Player = Player.get_player_info(id)
            player_to_modify_serialize = player_to_modify.serialize()
            player_data = self.views.entry_info_player(player_to_modify_serialize)
            player_to_modify = Player(**player_data)
            player_to_modify.update_player(id)
