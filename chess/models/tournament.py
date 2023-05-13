from chess.models.player import Player
from tinydb import TinyDB, Query

tournament_database = TinyDB("chess/models/tournament_database.json")

class Tournament:
    """tournament description"""

    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        num_rounds=4,
        current_round_num=1,
        rounds=None,
        players=None,
        director_notes="",
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round_num = current_round_num
        self.rounds = []
        self.players = []
        self.director_notes = director_notes
        self.player = Player()

    def add_player(self, player):
        self.players.append(self.player)

    def start_tournament(self):
        """Tournament start"""
        pass

    def end_round(self):
        pass

    def end_tournament(self):
        self.end_round()
        pass

    def serialize_tournament(self):
        serialized_tournament = {
            "name" = self.name,
            "location" : self.location,
            "start_date" : self.start_date,
            "end_date" : self.end_date,
            "num_rounds" : self.num_rounds,
            "current_round_num" : self.current_round_num,
            "rounds" : self.rounds,
            "players" : self.players,
            "director_notes" : self.director_notes
        }
        return serialized_tournament
    
    def update_toutnament_database(self, serialized_tournament):
        """Add a tournament to the list"""
        tournament_database.insert(serialized_tournament)


class Round:
    """Description d'un tour"""

    def __init__(self, name, start_date, end_date):
        """Round initialization"""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.match_list = ()

    def add_match(self):
        pass


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = ()

    def set_result(self):
        pass
