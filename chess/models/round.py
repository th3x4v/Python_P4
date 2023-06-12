from chess.models.player import Player


class Round:
    """Round description"""

    def __init__(
        self, name, start_date, match_list, end_date="", match_played="", status="0"
    ):
        """Round initialization"""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.match_list: list[Match] = match_list
        self.match_played = match_played
        self.status = status

    def serialize(self) -> dict:
        """return a dict with the attribute of this object Round"""
        match_list = [match.serialize() for match in self.match_list]
        match_played = [(player[0].id, player[1].id) for player in self.match_played]

        serialize_round = {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "match_list": match_list,
            "match_played": match_played,
            "status": self.status,
        }
        return serialize_round

    @classmethod
    def unserialize(cls, data: dict):
        """create a Round object from a dict"""
        match_list = [
            Match.unserialize(match_data) for match_data in data["match_list"]
        ]
        match_played = [
            (
                Player.get_player_info(match_data[0]),
                Player.get_player_info(match_data[1]),
            )
            for match_data in data["match_played"]
        ]
        return cls(
            name=data["name"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            match_list=match_list,
            match_played=match_played,
            status=data["status"],
        )

    def round_table(self):
        """return a table for display purpose"""
        round_table = [self.name, self.start_date, self.end_date, self.status]
        header = ["Name", "Start date", "End date", "Status(1=ended)"]
        return round_table, header


class Match:
    def __init__(self, player1: Player, player2: Player, match_result=None):
        self.player1 = player1
        self.player2 = player2
        self.match_result = match_result

    def serialize(self):
        """return a dict with the attribute of this object Match"""
        serialize_match = {
            "player1": self.player1.id,
            "player2": self.player2.id,
            "match_result": self.match_result,
        }
        return serialize_match

    @classmethod
    def unserialize(cls, data: dict):
        """create a Match object from a dict"""
        return cls(
            player1=Player.get_player_info(data["player1"]),
            player2=Player.get_player_info(data["player2"]),
            match_result=data["match_result"],
        )

    def match_table(self):
        """return a table for display purpose"""
        player1_data = list(((self.player1).serialize()).values())
        player2_data = list(((self.player2).serialize()).values())
        neutral_info = ["", "VS", "", "", "", ""]
        player_data = list(zip(player1_data, neutral_info, player2_data))
        return player_data
