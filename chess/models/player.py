from tinydb import TinyDB, Query
from chess.database.database import TinyTableManager, player_database


class Player:
    """Player description"""

    table: TinyTableManager = player_database

    def __init__(self, last_name, first_name, birthdate, player_id, id=0, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.player_id = player_id
        self.score = score
        self.id = id

        # self.player_db = TinyDB("chess/models/player_database.json")

    def serialize(self):
        serialized_player = {
            "Last Name": self.last_name,
            "First Name": self.first_name,
            "Date of Birth": self.birthdate,
            "Player ID": self.player_id,
            "Score": self.score,
            "id": self.id,
        }
        return serialized_player

    def unserialize(self, serialized_player):
        self.last_name = serialized_player["Last Name"]
        self.first_name = serialized_player["First Name"]
        self.birthdate = serialized_player["Date of Birth"]
        self.player_id = serialized_player["Player ID"]
        self.score = serialized_player["Score"]
        self.id = serialized_player["id"]

    def add_player_database(self):
        """Add a player to the list"""
        serialized_player: dict = self.serialize()
        id = self.table.save_db(serialized_player)
        return id

    def find_player(self, id):
        return self.table.find(doc_id=id)

    def modify_player(self, id):
        """Modify a player in the list"""
        serialized_player: dict = self.serialize()
        self.table.update_db(serialized_player, doc_ids=id)
