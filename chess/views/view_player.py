from tabulate import tabulate
from chess.models.player import Player
import json


class ViewsPlayer:
    """
    Display of the Player menu
    """

    def __init__(self):
        pass

    def display_player_menu(self):
        print("\n*** player menu ***\n".upper())
        print("0 - Player list")
        print("1 - Add a player to the global player list")
        print("2 - Modify a player")
        print("3 - Back")
        choice_player_menu = input("choice: ")
        return choice_player_menu

    def display_player_list(self, player_data):
        table = tabulate(player_data, headers="keys", tablefmt="grid")
        print(table)

    def get_info_player(self, player_to_modify: dict = None) -> "dict":
        """Interface to get a player information"""
        if player_to_modify == None:
            player_data = {}
            player_data["last_name"] = input("Last name: ")
            player_data["first_name"] = input("First name: ")
            player_data["birthdate"] = input("Date of birthday (DD/MM/YYYY): ")
            player_data["player_id"] = input("INE identification: ")
        else:
            print("The player name you want to modify is: ")
            print(player_to_modify.get("Last Name"))
            player_data = {}
            player_data["last_name"] = input(
                "Last name: "
                + player_to_modify["Last Name"]
                + " (Press enter to keep) "
            )
            if player_data["last_name"] == "":
                player_data["last_name"] = player_to_modify["Last Name"]

            player_data["first_name"] = input(
                "First name: "
                + player_to_modify["First Name"]
                + "(Press enter to keep) "
            )
            if player_data["first_name"] == "":
                player_data["first_name"] = player_to_modify["First Name"]

            player_data["birthdate"] = input(
                "Date of birthday (DD/MM/YYYY): "
                + player_to_modify["Date of Birth"]
                + " (Press enter to keep) "
            )
            if player_data["birthdate"] == "":
                player_data["birthdate"] = player_to_modify["Date of Birth"]

            player_data["player_id"] = input(
                "INE identification: "
                + player_to_modify["Player ID"]
                + " (Press enter to keep) "
            )
            if player_data["player_id"] == "":
                player_data["player_id"] = player_to_modify["Player ID"]

        return player_data

    def get_modify_player(self):
        """Modify a player"""
        id = int(
            input(
                "what is the position in the list of the player you want to modify ? "
            )
        )
        return id
