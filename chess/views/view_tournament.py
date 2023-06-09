from tabulate import tabulate
from chess.models.round import Match
from chess.views.view_menu import Views


class ViewsTournament:
    """
    Display of the tournament menu
    """

    def __init__(self):
        self.view_menu = Views()

    def get_tournament_info(self) -> dict:
        """Interface to get tournament information"""
        player_tournament = {}
        player_tournament["name"] = self.view_menu.get_user_entries(
            "name of tournament", "string"
        )
        player_tournament["location"] = self.view_menu.get_user_entries(
            "Location", "string"
        )
        player_tournament["start_date"] = self.view_menu.get_user_entries(
            "Tournament starting date (DD/MM/YYYY): ", "date"
        )
        player_tournament["end_date"] = self.view_menu.get_user_entries(
            "Tournament ending date (DD/MM/YYYY): ", "date"
        )
        player_tournament["num_rounds"] = self.view_menu.get_user_entries(
            "Number of rounds: ", "int"
        )
        player_tournament["director_notes"] = self.view_menu.get_user_entries(
            "Director description : ", "string"
        )
        return player_tournament

    def get_player_tournament_info(self) -> list:
        """tournament selection"""
        player_list: list = []
        print("Put the id of the player who will participate to the tournament ")
        add_player = self.view_menu.get_user_entries(
            "press enter when the list is complete ", "int"
        )
        while add_player != "":
            player_list.append(int(add_player))
            add_player = input("press enter when the list is complete ")
        return player_list

    def get_current_tournament(self):
        """resume a tournament"""
        id = int(
            self.view_menu.get_user_entries(
                "what is the 'id' in the list of the tournament you want to resume ? ",
                "int",
            )
        )
        return id

    def get_round_number(self):
        """Select a round"""
        id = int(
            self.view_menu.get_user_entries(
                "what is the number of the round you want to get ? (press 0 to go back)",
                "int",
            )
        )
        return id

    def display_tournament_list(self, tournament_data):
        table = tabulate(tournament_data, tablefmt="grid", showindex="always")
        print(table)

    def get_match_result(self, match: Match):
        """Get the match result"""
        print("Please, who is the winner of this match")
        # Match display
        player_data = match.match_table()
        self.view_menu.display_list(player_data, ["1", "N", "2"], (0, 1, 3))
        match_result = self.view_menu.get_user_entries("Result", "result")
        return match_result


if __name__ == "__main__":
    match: Match = Match(1, 2)
    views = ViewsTournament()
    views.get_match_result(match)
