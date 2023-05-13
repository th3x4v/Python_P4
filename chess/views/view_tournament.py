from tabulate import tabulate
from chess.models.player import Player
import json


class ViewsTournament:
    """
    Display of the tournament menu
    """

    def __init__(self):
       pass

    def display_tournament_menu(self):
        print("\n*** tournament menu ***\n".upper())
        print("1 - Create a new tournament")
        print("2 - Manage tournament")
        print("3 - Back")
        choice_tournament_menu = input("choice: ")
        return choice_tournament_menu
    
    def get_tournament_info(self) -> dict:
        """Interface to get tournament information """
        player_tournament = {}
        player_tournament["name"] = input("Name of the tournament: ")
        player_tournament["location"] = input("Location: ")
        player_tournament["start_date"] = input("Tournament starting date (DD/MM/YYYY): ")
        player_tournament["end_date"] = input("Tournament ending date (DD/MM/YYYY): ")
        player_tournament["num_rounds"] = input("Number of rounds: ")
        player_tournament["director_notes"] = input("Director description : ")
        return player_tournament

    

