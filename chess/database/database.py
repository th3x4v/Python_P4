from tinydb import TinyDB


class TinyTableManager:
    """Helper class to Implement the tinyDB method"""

    def __init__(self, table: TinyDB) -> None:
        self.table = table

    def save_db(self, data: dict) -> int:
        """Inserts a row in the table and return an id"""
        id: int = self.table.insert(data)
        return id

    def update_db(self, serialized_data: dict, id: int) -> None:
        """update a table"""
        self.table.update(serialized_data, doc_ids=id)

    def find(self, id):
        return self.table.get(doc_id=id)

    def all(self) -> list:
        """Return all records of the table"""
        records = self.table.all()
        # add the id to the record
        for record in records:
            record["id"] = record.doc_id
        return records

    def sort_players_by_name(self):
        """Sort players by name"""
        return sorted(self.table, key=lambda x: x["Last Name"])


db_p = TinyDB("chess/database/player_database.json")
player_database: TinyTableManager = TinyTableManager(db_p.table("Players"))


db_t = TinyDB("chess/database/tournament_database.json")
tournament_database: TinyTableManager = TinyTableManager(db_t.table("Tournaments"))


"""
    @staticmethod
    def load_tournament_db():
       # Load tournament database

        @return: list of tournaments
        
        db = TinyDB("chess/models/tournament_database.json")
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return tournaments_list

    @staticmethod
    def load_player_db():
        Load player database

        @return: list of players
        
        db = TinyDB("chess/database/player_database.json")
        player_database = db.table("Players")

        # player_database : TinyTableManager = TinyTableManager(db.table("Players"))
                db.all()
        players = []
        for item in players_db:
            players.append(item
        return player_database
"""
