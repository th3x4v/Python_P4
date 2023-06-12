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

    def get(self, id):
        """return one record of the table"""
        record = self.table.get(doc_id=id)
        if record is not None:
            record["id"] = record.doc_id
        return record


db_p = TinyDB("chess/database/player_database.json")
player_database: TinyTableManager = TinyTableManager(db_p.table("Players"))


db_t = TinyDB("chess/database/tournament_database.json")
tournament_database: TinyTableManager = TinyTableManager(db_t.table("Tournaments"))
