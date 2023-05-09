from tabulate import tabulate


class ViewsPlayer:
    """
    Display of the Player menu
    """

    def __init__(self):
        pass

    def display_player_menu(self):
        print("\n*** player menu ***\n".upper())
        print("1 - Upload players list")
        print("2 - Add players")
        print("3 - Save players list")
        print("4 - Back")
        choice_player_menu = input("choice: ")
        return choice_player_menu

    def display_player_list(self, player_data):
        table = tabulate(player_data, tablefmt="grid")
        print(table)

    def display_add_player(self):
        """Interface to add a player"""
        last_name = input("Last name: ")
        first_name = input("First name: ")
        birthdate = input("Date of birthday (DD/MM/YYYY): ")
        return [last_name, first_name, birthdate]
