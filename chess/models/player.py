from tinydb import TinyDB, Query

player_database = TinyDB("chess/models/player_database.json")


class Player:
    """Player description"""

    def __init__(self, last_name=None, first_name=None, birthdate=None, player_id=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.player_id = player_id

    def serialize_player(self):
        serialized_player = {
            "Player ID": self.player_id,
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Date of Birth": self.birthdate,
        }
        return serialized_player

    def update_player_database(self, serialized_player):
        """Add a player to the list"""
        player_database.insert(serialized_player)

    def find_player(self, player_id):
        return player_database.get(doc_id=player_id)

    def modify_player(self, serialized_player, id):
        """Modify a player in the list"""
        player_database.update(serialized_player, doc_ids=id)
