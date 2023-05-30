from chess.views.view_tournament import ViewsTournament
from chess.models.player import Player
from chess.views.view_player import ViewsPlayer
from chess.models.tournament import Tournament
from chess.models.round import Round, Match
from chess.database.database import (
    TinyTableManager,
    player_database,
    tournament_database,
)
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

        choice = self.views.display_tournament_menu()

        if choice == "0":
            # Tournament list
            print("Tournament list")

        if choice == "1":
            # create a tournament
            print("Create a tournament")
            # player_table = TinyTableManager.load_player_db()
            self.create_tournament(player_database.all())

        if choice == "2":
            # resume tournament
            print("Resume tournament")
            tournament_list = []
            for tournament in tournament_database.all():
                print(tournament["name"])
                tournament_list.append([tournament["name"]])
            self.views.display_tournament_list(tournament_list)
            id = self.views.get_current_tournament()
            tournaments = tournament_database.all()
            tournament: Tournament = Tournament.unserialize(tournaments[id])
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
        player_tournament_list: list = self.views.get_player_tournament_info()
        random.shuffle(player_tournament_list)
        player_tournament_data = []
        for player in player_tournament_list:
            player_data: dict = {"player": player, "score": 0}
            player_tournament_data.append(player_data)
        tournament.players = player_tournament_data
        tournament.rounds = []
        tournament.add_tournament_database()

    def start_tournament_manager(self, tournament: Tournament, id):
        """Tournament manager"""

        choice = self.views.display_tournament_manager(tournament)

        if choice == "0":
            # Tournament reports
            print("Display tournament reports")
            tournament.sort_players_by_name()
            self.playerviews.display_player_list(tournament.players)

        if choice == "1":
            # Continue the tournament
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
                    print("player_list")
                    print(tournament.players)
                    tournament.players = sorted(
                        tournament.players, key=lambda x: x.get("score"), reverse=True
                    )
                    print("player_list")
                    print(tournament.players)
                    tournament.rounds[-1] = current_round
                    tournament.update_tournament_database([id + 1])
            self.start_tournament_manager(tournament, id)

        if choice == "2":
            # resume tournament
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
        tournament.update_tournament_database([id + 1])

    def set_match(self, tournament: Tournament):
        """Match creation"""
        print("enter the set match")
        l = len(tournament.players)
        print("tournament.players")
        print(tournament.players)
        if tournament.current_round_num == 1:
            match_played = []
        else:
            print("tournament.roundstournament.current_round_num - 2.match_played1")
            print(tournament.rounds[tournament.current_round_num - 2].match_played)
            match_played = tournament.rounds[
                tournament.current_round_num - 2
            ].match_played

        match_list = []
        for i in range(0, int(l / 2), 1):
            print("i")
            print(i)
            print(l)
            print("debug0")
            print(tournament.players)
            player_pairs = [
                tournament.players[i]["player"],
                tournament.players[l - i - 1]["player"],
            ]
            n = i
            if i != l / 2 - 1:  # check if it's not the last match to be set
                while (player_pairs in match_played) or (
                    list(reversed(player_pairs)) in match_played
                ):
                    print("match already played")
                    tournament_temp = tournament
                    print("debug1")
                    print("pair")
                    print(player_pairs)
                    print("reversepair")
                    print(list(reversed(player_pairs)))
                    print(tournament_temp.players)
                    player_pairs = [
                        tournament_temp.players[i]["player"],
                        tournament_temp.players[l - n - 2]["player"],
                    ]
                    print("pair")
                    print(player_pairs)
                    (
                        tournament_temp.players[l - n - 2]["player"],
                        tournament_temp.players[l - i - 1]["player"],
                    ) = (
                        tournament_temp.players[l - i - 1]["player"],
                        tournament_temp.players[l - n - 2]["player"],
                    )
                    n += 1
                    if n == int(l / 2) - i:
                        print("break")
                        break
                    tournament = tournament_temp
                    print("debug2")
                    print(n)
                    print(tournament_temp.players)
            # print("tournament.roundstournament.current_round_num - 2.match_played2")
            # print(tournament.rounds[tournament.current_round_num - 2].match_played)
            match: Match = Match(player1=player_pairs[0], player2=player_pairs[1])
            match_list.append(match)
            if not (player_pairs in match_played) or not (
                list(reversed(player_pairs)) in match_played
            ):
                match_played.append(player_pairs)
            # print("tournament.roundstournament.current_round_num - 2.match_played3")
            # print(tournament.rounds[tournament.current_round_num - 2].match_played)
            print("match_played")
            print(match_played)
            # display match
            for match in match_list:
                pass

        return match_list, match_played

    def end_round(self, round: Round, player_list):
        """Finalize a round with updating match result and end date"""
        for match in round.match_list:
            result = self.views.get_match_result(match)
            match.match_result = result
            player1 = Player.get_player_info(match.player1 - 1)
            player2 = Player.get_player_info(match.player2 - 1)
            if result == "1":
                # add result to global score
                player1.score = player1.score + 1
                player1.modify_player(int(player1.id))
                # add result to tournament
                for player in player_list:
                    if player["player"] == player1.id:
                        player["score"] = player["score"] + 1
            elif result == "2":
                player2.score = player2.score + 1
                player2.modify_player(int(player2.id))
                # add result to tournament
                for player in player_list:
                    if player["player"] == player2.id:
                        player["score"] = player["score"] + 1
            else:
                player1.score = player1.score + 0.5
                player2.score = player2.score + 0.5
                player1.modify_player(int(player1.id))
                player2.modify_player(int(player2.id))
                # add result to tournament
                for player in player_list:
                    if player["player"] == player1.id:
                        player["score"] = player["score"] + 0.5
                    if player["player"] == player2.id:
                        player["score"] = player["score"] + 0.5
        round.end_date = "test"
        round.status = 1
