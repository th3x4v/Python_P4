from tabulate import tabulate
from chess.models.tournament import Tournament
from chess.models.round import Round, Match
from chess.database.database import player_database
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
        print("\n*** tournament manager ***\n".upper())
        self.display_tournament(tournament)
        print("0 - Tournament reports ")
        print("1 - Next round ")
        print("2 - ")
        print("3 - Back")
        choice_tournament_manager = input("choice: ")
        return choice_tournament_manager

    def display_tournament(self, tournament: Tournament):
        """Display of current tournament"""
        tournament_table = [
            [
                tournament.name,
                tournament.location,
                tournament.start_date,
                tournament.end_date,
                tournament.num_rounds,
                tournament.current_round_num,
            ]
        ]
        header = [
            "Name",
            "Location",
            "Starting date",
            "Ending date",
            "number of rounds",
            "Current round",
        ]
        print(tabulate(tournament_table, header, tablefmt="grid"))

    def get_match_result(self, match: Match):
        """Get the match result"""
        print("Please, who is the winner of this match")
        player1 = Player.get_player_info(match.player1 - 1)
        player1_data = list((player1.serialize()).values())
        player1_data.pop(-1)
        print(player1_data)
        player2 = Player.get_player_info(match.player2 - 1)
        player2_data = list((player2.serialize()).values())
        player2_data.pop(-1)
        neutral_info = ["", "", "VS", "", ""]
        player_data = zip(player1_data, neutral_info, player2_data)
        table = tabulate(player_data, headers=["1", "N", "2"], tablefmt="fancy_grid")
        print(table)
        match_result = self.view_menu.get_user_entries("Result", "result")
        return match_result


if __name__ == "__main__":
    match: Match = Match(1, 2)
    views = ViewsTournament()
    views.get_match_result(match)
