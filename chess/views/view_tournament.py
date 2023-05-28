from tabulate import tabulate
from chess.models.tournament import Tournament
from chess.models.round import Round, Match
from chess.database.database import player_database


class ViewsTournament:
    """
    Display of the tournament menu
    """

    def __init__(self):
        pass

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
        player_tournament["name"] = input("Name of the tournament: ")
        player_tournament["location"] = input("Location: ")
        player_tournament["start_date"] = input(
            "Tournament starting date (DD/MM/YYYY): "
        )
        player_tournament["end_date"] = input("Tournament ending date (DD/MM/YYYY): ")
        player_tournament["num_rounds"] = input("Number of rounds: ")
        player_tournament["director_notes"] = input("Director description : ")
        return player_tournament

    def get_player_tournament_info(self) -> list:
        player_list: list = []
        print("Put the id of the player who will participate to the tournament ")
        add_player = input("press enter when the list is complete ")
        while add_player != "":
            player_list.append(int(add_player))
            add_player = input("press enter when the list is complete ")
        return player_list

    def get_current_tournament(self):
        """resume a tournament"""
        id = int(
            input(
                "what is the position in the list of the tournament you want to resume ? "
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
        print(player_database.all()[match.player1-1])
        print("vs")
        print(player_database.all()[match.player2-1])
        match_result = input("Enter the player id ")
        return match_result


if __name__ == "__main__":
    match: Match = Match(1, 2)
    views = ViewsTournament()
    views.get_match_result(match)
