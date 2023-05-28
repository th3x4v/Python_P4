class Round:
    """Round description"""

    def __init__(
        self, name, start_date, match_list, end_date="", match_played="", status="0"
    ):
        """Round initialization"""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.match_list = match_list
        self.match_played = match_played
        self.status = status

    def serialize(self) -> dict:
        """return a dict with the attribute of this object Round"""
        match_list = [match.serialize() for match in self.match_list]

        serialize_round = {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "match_list": match_list,
            "match_played": self.match_played,
            "status": self.status,
        }
        """print("serialize_round")
        print(serialize_round)"""
        return serialize_round

    @classmethod
    def unserialize(cls, data: dict):
        """create a Round object from a dict"""
        match_list = [
            Match.unserialize(match_data) for match_data in data["match_list"]
        ]
        return cls(
            name=data["name"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            match_list=match_list,
            match_played=data["match_played"],
            status=data["status"],
        )


class Match:
    def __init__(self, player1, player2, match_result=None):
        self.player1 = player1
        self.player2 = player2
        self.match_result = match_result

    def serialize(self):
        """return a dict with the attribute of this object Match"""
        serialize_match = {
            "player1": self.player1,
            "player2": self.player2,
            "match_result": self.match_result,
        }
        return serialize_match

    @classmethod
    def unserialize(cls, data: dict):
        """create a Match object from a dict"""
        return cls(
            player1=data["player1"],
            player2=data["player2"],
            match_result=data["match_result"],
        )
