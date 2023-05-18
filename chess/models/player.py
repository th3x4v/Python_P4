from tinydb import TinyDB, Query

# player_database = TinyDB("chess/models/player_database.json")
# player_table = player_database.all()
# sorted_player = sorted(player_table, key=lambda x: x["Last Name"])


class Player:
    """Player description"""

    def __init__(self, last_name, first_name, birthdate, player_id, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.player_id = player_id
        self.score = score

        self.player_db = TinyDB("chess/models/player_database.json")

    def serialize_player(self):
        serialized_player = {
            "Last Name": self.last_name,
            "First Name": self.first_name,
            "Date of Birth": self.birthdate,
            "Player ID": self.player_id,
            "Score": self.score,
        }
        return serialized_player

    def add_player_database(self, serialized_player):
        """Add a player to the list"""
        self.player_db.insert(serialized_player)

    def find_player(self, id):
        return self.player_db.get(doc_id=id)

    def modify_player(self, serialized_player, id):
        """Modify a player in the list"""
        self.player_db.update(serialized_player, doc_ids=id)

    @staticmethod
    def load_player_db():
        """Load player database

        @return: list of players
        """
        players_db = TinyDB("chess/models/player_database.json")
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
