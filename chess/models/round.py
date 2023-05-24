class Round:
    """Round description"""

    def __init__(self, name, start_date, match_list, end_date="", match_played=""):
        """Round initialization"""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.match_list = match_list
        self.match_played = match_played

    def serialize(self) -> dict:
        """return a dict with the attribute of this object Round"""
        match_list = [match.serialize() for match in self.match_list]

        serialize_round = {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "match_list": match_list,
            "match_played": self.match_played,
        }
        return serialize_round


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
