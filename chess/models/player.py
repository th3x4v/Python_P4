from tinydb import TinyDB

player_database = TinyDB("chess/models/player_database.json")


class Player:
    """Player description"""

    def __init__(self, last_name=None, first_name=None, birthdate=None, player_id=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.player_id = player_id
