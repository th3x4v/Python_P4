from chess.views.view_tournament import ViewsTournament
from chess.views.view_player import ViewsPlayer
from chess.models.tournament import Tournament, Round, Match
from chess.models.player import Player
from chess.models import player
from chess.models import tournament
import random
from datetime import date, datetime


class TournamentController:
    """Player management"""

    def __init__(self):
        self.views = ViewsTournament()
        self.playerviews = ViewsPlayer()

    def start(self):
        """Display tournament menu and user choice"""

        tournament_table = Tournament.load_tournament_db()
        player_table = Player.load_player_db()
        choice = self.views.display_tournament_menu()

        if choice == "0":
            # Tournament list
            print("Tournament list")

        if choice == "1":
            # create a tournament
            print("Create a tournament")
            self.create_tournament(player_table)

        if choice == "2":
            # resume tournament
            print("Resume tournament")
            tournament_list = []
            for tournament in tournament_table:
                print(tournament["name"])
                tournament_list.append([tournament["name"]])
            self.views.display_tournament_list(tournament_list)
            id = self.views.get_current_tournament()
            tournament_data: dict = tournament_table[id]
            tournament: Tournament = Tournament(**tournament_data)
            tournament.players = tournament_data[
                "players"
            ]  # il y a un soucis sur le unpacking des tables
            tournament.rounds = tournament_data["rounds"]
            self.start_tournament_manager(tournament, id)

        if choice == "3":
            # exit
            print("exit")

    def create_tournament(self, player_table):
        """Tournament creation"""
        tournament_data: dict = self.views.get_tournament_info()
        tournament: Tournament = Tournament(**tournament_data)
        self.add_player_tournament(player_table, tournament)
        self.start()

    def add_player_tournament(self, player_table, tournament: Tournament):
        """Add player to a tournament"""
        self.playerviews.display_player_list(player_table)
        player_list: list = self.views.get_player_tournament_info()
        player_tournament_data: list = []
        for i in player_list:
            player_tournament_data.append(player_table[i])
        random.shuffle(player_tournament_data)
        tournament.players = player_tournament_data
        serialized_tournament = tournament.serialize_tournament()
        tournament.update_tournament_database(serialized_tournament)

    def start_tournament_manager(self, tournament: Tournament, id):
        """Tournament manager"""

        choice = self.views.display_tournament_manager(tournament)

        if choice == "0":
            # Tournament reports
            print("Display tournament reports")
            tournament.sort_players_by_name()
            self.playerviews.display_player_list(tournament.players)

        if choice == "1":
            # Next round
            print("next round")
            self.next_round(tournament, id)

        if choice == "2":
            # resume tournament
            print("test")

        if choice == "3":
            # exit
            print("exit")

    def next_round(self, tournament: Tournament, id):
        tournament.current_round_num = tournament.current_round_num + 1
        name = "Round" + str(tournament.current_round_num)
        start_date = ""
        match = self.set_match(tournament)
        round: Round = Round(
            name=name, start_date=start_date, match_list=match[0], match_played=match[1]
        )
        tournament.rounds.append(round.__dict__)
        serialized_tournament = tournament.serialize_tournament()
        tournament.update_tournament_database(serialized_tournament, [id + 1])

    def set_match(self, tournament: Tournament):
        """Match creation"""
        l = len(tournament.players)
        if tournament.current_round_num == 1:
            match_played = []
        else:
            match_played = tournament.rounds[tournament.current_round_num - 2][
                "match_played"
            ]
        match_list = []
        # for round in tournament.rounds:
        #    match_played.append(round["match_list"])
        for i in range(0, l, 2):
            player_pairs = [(tournament.players[i], tournament.players[l - i - 1])]
            n = i
            while player_pairs in match_played:
                print("match already played")
                tournament_temp = tournament
                player_pairs = [
                    (tournament_temp.players[i], tournament_temp.players[l - n - 2])
                ]
                (
                    tournament_temp.players[l - n - 2],
                    tournament_temp.players[l - i - 1],
                ) = (
                    tournament_temp.players[l - i - 1],
                    tournament_temp.players[l - n - 2],
                )
                n += 1
                if n == l - i:
                    break
                tournament = tournament_temp

            match_list.append(player_pairs)
            match_played.append(player_pairs)
            print(len(match_played))

        return match_list, match_played
