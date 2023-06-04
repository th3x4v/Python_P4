from tabulate import tabulate
from chess.models.tournament import Tournament
from chess.models.round import Round, Match
from chess.database.database import tournament_database
from chess.views.view_menu import Views
from chess.models.player import Player


class ViewsTournament:
    """
    Display of the tournament menu
    """

    def __init__(self):
        self.view_menu = Views()

    def display_tournament_menu(self):
        print("\n*** tournament menu ***\n".upper())
        print("0 - Tournament lists ")
        print("1 - Create a new tournament")
        print("2 - Resume tournament")
        print("3 - Back")
        choice_tournament_menu = input("choice: ")
        return choice_tournament_menu

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
                "what is the position in the list of the tournament you want to resume ? ",
                "int",
            )
        )
        return id

    def display_tournament_list(self, tournament_data):
        table = tabulate(tournament_data, tablefmt="grid", showindex="always")
        print(table)

    def display_tournament_manager(self, tournament: Tournament):
        """Display of tournament manager"""
        print("\n*** tournament manager ***\n".upper())
        self.view_menu.display_list(
            tournament.tournament_table()[0], header=tournament.tournament_table()[1]
        )
        print("0 - Tournament reports ")
        print("1 - Continue tournament ")
        print("2 - ")
        print("3 - Back")
        choice_tournament_manager = input("choice: ")
        return choice_tournament_manager

    def get_match_result(self, match: Match):
        """Get the match result"""
        print("Please, who is the winner of this match")
        # Match display
        player_data = match.match_table()
        self.view_menu.display_list(player_data, ["1", "N", "2"], (0, 1, 3))
        match_result = self.view_menu.get_user_entries("Result", "result")
        return match_result

    def display_tournament_report(self):
        """Display of tournament reports"""
        print("\n*** tournament reports ***\n".upper())
        print("1 - Tournament lists ")
        print("2 - Tournament info ")
        print("3 - Back")
        choice_tournament_report = input("choice: ")
        return choice_tournament_report


if __name__ == "__main__":
    match: Match = Match(1, 2)
    views = ViewsTournament()
    views.get_match_result(match)
    views.display_tournament_list(views.tournament_table())
