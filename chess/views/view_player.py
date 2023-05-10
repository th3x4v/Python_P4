from tabulate import tabulate
from chess.models.player import Player


class ViewsPlayer:
    """
    Display of the Player menu
    """

    def __init__(self):
        self.player = Player()

    def display_player_menu(self):
        print("\n*** player menu ***\n".upper())
        print("1 - Add a player to the global player list")
        print("2 - Modify a player")
        print("3 - Back")
        choice_player_menu = input("choice: ")
        return choice_player_menu

    def display_player_list(self, player_data):
        table = tabulate(
            player_data, headers="keys", tablefmt="grid", showindex="always"
        )
        print(table)

    def display_add_player(self):
        """Interface to add a player"""
        self.player.last_name = input("Last name: ")
        self.player.first_name = input("First name: ")
        self.player.birthdate = input("Date of birthday (DD/MM/YYYY): ")
        return self.player

    def display_modify_player(self):
        """Modify a player"""
        id = input("what is the position in the list of the player you want to modify ? ")
        print ("Enter the new information: ")
        return id
