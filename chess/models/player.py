from chess.database.database import TinyTableManager, player_database


class Player:
    """Player description"""

    table: TinyTableManager = player_database

    def __init__(self, last_name, first_name, birthdate, player_INE, id=0, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.player_INE = player_INE
        self.score = score
        self.id = id

    def serialize(self)-> dict:
        """return a dictionnary"""
        serialized_player = {
            "Last Name": self.last_name,
            "First Name": self.first_name,
            "Date of Birth": self.birthdate,
            "Player INE": self.player_INE,
            "Score": self.score,
        }
        return serialized_player

    @classmethod
    def unserialize(cls, serialized_player):
        """Unserialize player data"""
        return cls(
            last_name=serialized_player["Last Name"],
            first_name=serialized_player["First Name"],
            birthdate=serialized_player["Date of Birth"],
            player_INE=serialized_player["Player INE"],
            score=serialized_player["Score"],
        )

    @classmethod
    def get_player_info(self, id):
        """Get the player info from the database"""
        player_data = self.table.get(id)
        player: Player = Player.unserialize(player_data)
        player.id = id
        return player

    def add_player_database(self):
        """Add a player to the list"""
        serialized_player: dict = self.serialize()
        id = self.table.save_db(serialized_player)
        return id

    def update_player(self, id):
        """Modify a player in the list"""
        serialized_player: dict = self.serialize()
        self.table.update_db(serialized_player, [id])


if __name__ == "__main__":
    player = Player.get_player_info(2)
    print(player.first_name)
    print(player.last_name)
    print(player.birthdate)
