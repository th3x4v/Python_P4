from tabulate import tabulate
from chess.views.view_tournament import ViewsTournament
from chess.models.player import Player
from chess.views.view_player import ViewsPlayer
from chess.views.view_menu import Views
from chess.models.tournament import Tournament
from chess.models.round import Round, Match
from chess.database.database import (
    player_database,
    tournament_database,
)
import random
from datetime import date, datetime


class TournamentController:
    """Player management"""

    def __init__(self):
        self.views = ViewsTournament()
        self.playerviews = ViewsPlayer()
        self.views_menu = Views()

    def start(self):
        """Display tournament menu and user choice"""

        choice = self.views.display_tournament_menu()

        if choice == "0":
            # Reports
            print("Reports")
            self.reports()
            self.start()

        if choice == "1":
            # create a tournaments
            print("Create a tournament")
            self.create_tournament()

        if choice == "2":
            # resume tournament
            print("Resume tournament")
            tournaments = tournament_database.all()
            tournament_list = []
            # filtering ongoing tournament only
            for tournament in tournaments:
                current_round_num = int(tournament["current_round_num"])
                if int(tournament["current_round_num"]) < int(
                    tournament["num_rounds"]
                ) or (
                    int(tournament["current_round_num"])
                    == int(tournament["num_rounds"])
                    and tournament["rounds"][current_round_num - 1]["status"] == "0"
                ):
                    tournament_list.append(tournament)

            self.views_menu.display_list(
                self.tournament_list(tournament_list)[0],
                header=self.tournament_list(tournament_list)[1],
            )
            id = self.views.get_current_tournament()
            tournament: Tournament = Tournament.unserialize(tournaments[id - 1])
            self.start_tournament_manager(tournament, id)

        if choice == "3":
            # exit
            print("exit")

    def create_tournament(self):
        """Tournament creation"""
        tournament_data: dict = self.views.get_tournament_info()
        tournament: Tournament = Tournament(**tournament_data)
        self.add_player_tournament(tournament)
        self.start_tournament_manager(tournament, tournament.id)

    def add_player_tournament(self, tournament: Tournament):
        """Add player to a tournament"""
        self.views_menu.display_list(player_database.all(), header="keys")
        player_tournament_list: list = self.views.get_player_tournament_info()
        random.shuffle(player_tournament_list)
        player_tournament_data = []
        for player in player_tournament_list:
            player_data: dict = {"player": Player.get_player_info(player), "score": 0}
            player_tournament_data.append(player_data)
        tournament.players = player_tournament_data
        tournament.rounds = []
        id = tournament.add_tournament_database()
        tournament.id = id
        tournament.update_tournament_database([id])

    def start_tournament_manager(self, tournament: Tournament, id):
        """Tournament manager"""

        choice = self.views.display_tournament_manager(tournament)

        if choice == "0":
            # Tournament reports
            print("Display tournament reports")
            self.tournament_report(tournament)

        if choice == "1":
            # Continue the tournament
            print("debug")
            print(tournament.id)
            print(id)
            if tournament.rounds == []:
                print("next round")
                self.next_round(tournament, id)
            else:
                current_round = tournament.rounds[-1]
                if current_round.status == 1:
                    print("next round")
                    self.next_round(tournament, id)
                else:
                    print("round ending")
                    self.end_round(current_round, tournament.players)
                    tournament.players = sorted(
                        tournament.players, key=lambda x: x.get("score"), reverse=True
                    )
                    tournament.rounds[-1] = current_round
                    tournament.update_tournament_database([id])
            self.start_tournament_manager(tournament, id)

        if choice == "2":
            #
            print("test")

        if choice == "3":
            # exit
            print("exit")
            self.start()

    def next_round(self, tournament: Tournament, id):
        tournament.current_round_num = tournament.current_round_num + 1
        name = "Round" + str(tournament.current_round_num)
        start_date = ""
        match = self.set_match(tournament)
        round: Round = Round(
            name=name, start_date=start_date, match_list=match[0], match_played=match[1]
        )
        tournament.rounds.append(round)
        tournament.update_tournament_database([id])

    def set_match(self, tournament: Tournament):
        """Match creation"""
        print("The matches of the round will be: ")
        l = len(tournament.players)
        if tournament.current_round_num == 1:
            match_played = []
        else:
            match_played = tournament.rounds[
                tournament.current_round_num - 2
            ].match_played

        match_list = []
        for i in range(0, l, 2):
            player_pairs = [
                tournament.players[i]["player"],
                tournament.players[i + 1]["player"],
            ]
            if i != l - 2:  # check if it's not the last match to be set
                if (player_pairs in match_played) or (
                    list(reversed(player_pairs)) in match_played
                ):
                    print("match already played")
                    player_pairs = [
                        tournament.players[i]["player"],
                        tournament.players[i + 2]["player"],
                    ]
                    (
                        tournament.players[i + 1],
                        tournament.players[i + 2],
                    ) = (
                        tournament.players[i + 2],
                        tournament.players[i + 1],
                    )
            match: Match = Match(player1=player_pairs[0], player2=player_pairs[1])
            # display match
            player_data = match.match_table()
            self.views_menu.display_list(player_data, data_select=(0, 1, 3))
            match_list.append(match)
            if not (player_pairs in match_played) or not (
                list(reversed(player_pairs)) in match_played
            ):
                match_played.append(player_pairs)
        return match_list, match_played

    def end_round(self, round: Round, player_list):
        """Finalize a round with updating match result and end date"""
        for match in round.match_list:
            result = self.views.get_match_result(match)
            match.match_result = result
            if result == "1":
                # add result to global score
                match.player1.score = match.player1.score + 1
                match.player1.modify_player(int(match.player1.id))
                # add result to tournament
                for player in player_list:
                    if player["player"] == match.player1:
                        player["score"] = player["score"] + 1
            elif result == "2":
                match.player2.score = match.player2.score + 1
                match.player2.modify_player(int(match.player2.id))
                # add result to tournament
                for player in player_list:
                    if player["player"] == match.player2:
                        player["score"] = player["score"] + 1
            else:
                match.player1.score = match.player1.score + 0.5
                match.player2.score = match.player2.score + 0.5
                match.player1.modify_player(int(match.player1.id))
                match.player2.modify_player(int(match.player2.id))
                # add result to tournament
                for player in player_list:
                    if player["player"] == match.player1:
                        player["score"] = player["score"] + 0.5
                    if player["player"] == match.player2:
                        player["score"] = player["score"] + 0.5
        round.end_date = "test"
        round.status = 1

    def reports(self):
        """report choice"""

        choice = self.views_menu.display_menu(
            title1="reports",
            choice0="1 - Tournament reports",
            choice1="2 - Player list",
            choice2="3 - Quit the application",
        )
        if choice == "1":
            # tournament
            self.tournament_report()

        if choice == "2":
            # Report of a specific tournament
            print("Tournament information")
            id = self.views.get_current_tournament()
            tournament: Tournament = Tournament.get_tournament_info(id)

        if choice == "3":
            # exit
            pass

    def tournament_report(self):
        """tournament reports"""

        choice = self.views_menu.display_menu(
            title1="reports",
            choice0="1 - Tournament list",
            choice1="2 - Tournament information",
            choice2="3 - Quit the application",
        )

        if choice == "1":
            # tournament list
            self.views_menu.display_list(
                self.tournament_list(tournament_database.all())[0],
                header=self.tournament_list(tournament_database.all())[1],
            )

        if choice == "2":
            # Report of a specific tournament
            print("Tournament information")
            id = self.views.get_current_tournament()
            tournament: Tournament = Tournament.get_tournament_info(id)
            self.tournament_information(tournament)

        if choice == "3":
            # exit
            pass

    def tournament_information(self, tournament):
        """tournament information"""

        choice = self.views_menu.display_menu(
            title1="Tournament information",
            choice0="1 - Tournament rounds",
            choice1="2 - Tournament players",
            choice2="3 - Quit the application",
        )

        if choice == "1":
            # tournament rounds
            pass

        if choice == "2":
            # Tournament players
            pass

        if choice == "3":
            # exit
            pass

    def tournament_list(self, tournament_data_list):
        tournament_list = []
        tournament_data_list
        tournament_header = list(tournament_data_list[0].keys())
        tournament_header_filer = [
            tournament_header[i]
            for i in range(len(tournament_header))
            if i in (0, 1, 2, 3, 4, 5, 8, 9)
        ]
        for tournament in tournament_data_list:
            tournament_data = list(tournament.values())
            tournament_data_filer = [
                tournament_data[i]
                for i in range(len(tournament_data))
                if i in (0, 1, 2, 3, 4, 5, 8, 9)
            ]
            tournament_list.append(tournament_data_filer)

        return tournament_list, tournament_header_filer


if __name__ == "__main__":
    self = TournamentController()
    # tournament: Tournament = Tournament.get_tournament_info(0)
    # self.tournament_report(tournament)
    my_list = [
        ("Gabrielle", "", "Garcia"),
        ("Jessica", "VS", "Miguel"),
        ("03/02/2001", "", "15/12/1990"),
        ("JG00001", "", "CD67890"),
        (10.0, "", 22.0),
        (10, "", 3),
    ]
    self.views_menu.display_list(
        self.tournament_list()[0], header=self.tournament_list()[1]
    )
