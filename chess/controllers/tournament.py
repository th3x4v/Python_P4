from chess.views.view_player import ViewsPlayer
from chess.models.player import Player
from chess.views.view_tournament import ViewsTournament
from chess.models.tournament import Tournament
from chess.models import player


class TournamentController:
    """Player management"""

    def __init__(self):
        self.views = ViewsTournament()


    def start(self):
        """Display tournament menu and user choice"""
        
        choice = self.views.display_tournament_menu()

        if choice == "0":
            # Tournament list
            print("Tournament list")

        if choice == "1":
            # create a tournament
            print("Create a tournament")
            self.create_tournament()

        if choice == "2":
            # resume tournament
            print("resume tournament")


        if choice == "3":
            # exit
            print("exit")
    
    def create_tournament(self): 
        """Tournament creation"""
        tournament_data: dict = self.views.get_info_player()
        tournament : Tournament = Tournament(**tournament_data)
        serialized_tournament= tournament.serialize_tournament()
        tournament.update_tournament_database(serialized_tournament)
        self.start()



