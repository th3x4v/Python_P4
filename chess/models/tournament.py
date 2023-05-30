from chess.models.player import Player
from chess.models.round import Round
from tinydb import TinyDB
from chess.database.database import TinyTableManager, tournament_database


class Tournament:
    """tournament description"""

    table: TinyTableManager = tournament_database

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
        id=0,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round_num = current_round_num
        self.rounds = rounds
        self.players = players
        self.director_notes = director_notes
        self.id = id

        # self.tournament_db = TinyDB("chess/models/tournament_database.json")

    def serialize(self) -> dict:
        """return a dictionnary"""
        rounds = [round.serialize() for round in self.rounds]

        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "num_rounds": self.num_rounds,
            "current_round_num": self.current_round_num,
            "rounds": rounds,
            "players": self.players,
            "director_notes": self.director_notes,
        }
        return serialized_tournament

    @classmethod
    def unserialize(cls, serialized_tournament):
        """Create a new Tournament object from a serialized dictionary"""
        tournament = cls(
            name=serialized_tournament["name"],
            location=serialized_tournament["location"],
            start_date=serialized_tournament["start_date"],
            end_date=serialized_tournament["end_date"],
            num_rounds=serialized_tournament["num_rounds"],
            current_round_num=serialized_tournament["current_round_num"],
            players=serialized_tournament["players"],
            director_notes=serialized_tournament["director_notes"],
            id=serialized_tournament["id"],
        )
        tournament.rounds = [
            Round.unserialize(round_data)
            for round_data in serialized_tournament["rounds"]
        ]
        print("tournament.players")
        print(tournament.players)
        return tournament

    def add_tournament_database(self):
        """Add a tournament to the list"""
        serialized_tournament: dict = self.serialize()
        id = self.table.save_db(serialized_tournament)
        return id

    def update_tournament_database(self, id):
        """update a tournament to the list"""
        serialized_tournament: dict = self.serialize()
        self.table.update_db(serialized_tournament, id)

    def find_tournament(self, id):
        return self.table.find(doc_id=id)

    def sort_players_by_score(self):
        """Sort players by score (descending)"""
        self.players = sorted(self.players, key=lambda x: x.get("score"), reverse=True)

    def sort_players_by_name(self):
        """Sort players by score (descending)"""
        self.players = sorted(self.players, key=lambda x: x["Last Name"])


if __name__ == "__main__":
    tournament: Tournament = Tournament()
    pass
