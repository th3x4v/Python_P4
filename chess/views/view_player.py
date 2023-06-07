from chess.views.view_menu import Views


class ViewsPlayer:
    """
    Display of the Player menu
    """

    def __init__(self):
        self.view_menu = Views()

    def get_info_player(self, player_to_modify: dict = None) -> "dict":
        """Interface to get a player information"""
        if player_to_modify is None:
            player_data = {}
            player_data["last_name"] = self.view_menu.get_user_entries(
                "Last name: ", "string"
            )
            player_data["first_name"] = self.view_menu.get_user_entries(
                "First name: ", "string"
            )
            player_data["birthdate"] = self.view_menu.get_user_entries(
                "Date of birthday (DD/MM/YYYY): ", "date"
            )
            player_data["player_INE"] = self.view_menu.get_user_entries(
                "INE identification: ", "INE"
            )
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

            player_data["player_INE"] = input(
                "INE identification: "
                + player_to_modify["Player INE"]
                + " (Press enter to keep) "
            )
            if player_data["player_INE"] == "":
                player_data["player_INE"] = player_to_modify["Player INE"]

        return player_data

    def get_modify_player(self):
        """Modify a player"""
        id = int(
            input("what is the 'id' in the list of the player you want to modify ? ")
        )
        return id
