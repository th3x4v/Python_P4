from chess.models.player import Player
from tinydb import TinyDB


class Tournament:
    """tournament description"""

    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        num_rounds=4,
        current_round_num=0,
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

        self.tournament_db = TinyDB("chess/models/tournament_database.json")

    def serialize_tournament(self):
        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "num_rounds": self.num_rounds,
            "current_round_num": self.current_round_num,
            "rounds": self.rounds,
            "players": self.players,
            "director_notes": self.director_notes,
        }
        return serialized_tournament

    def update_tournament_database(self, serialized_tournament, id):
        """Add a tournament to the list"""
        self.tournament_db.update(serialized_tournament, doc_ids=id)

    def find_tournament(self, id):
        return self.tournament_db.get(doc_id=id)

    def sort_players_by_score(self):
        """Sort players by score (descending)"""
        self.players = sorted(self.players, key=lambda x: x.get("score"), reverse=True)

    def sort_players_by_name(self):
        """Sort players by score (descending)"""
        self.players = sorted(self.players, key=lambda x: x["Last Name"])

    @staticmethod
    def load_tournament_db():
        """Load tournament database

        @return: list of tournaments
        """
        db = TinyDB("chess/models/tournament_database.json")
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return tournaments_list


class Round:
    """Round description"""

    def __init__(self, name, start_date, match_list, end_date=""):
        """Round initialization"""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.match_list = match_list


class Match:
    def __init__(self, player1: Player, player2: Player, match_result=None):
        self.player1 = player1
        self.player2 = player2
        self.match_result = match_result
