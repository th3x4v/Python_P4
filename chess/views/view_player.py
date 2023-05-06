class ViewsPlayer:
    """
    Display of the Player menu
    """

    def __init__(self):
        pass

    def display_player_menu(self):
        print("\n*** player menu ***\n".upper())
        print("1 - Upload players list")
        print("2 - Add players")
        print("3 - Save players list")
        print("4 - Back")
        choice_player_menu = input("choice: ")
        return choice_player_menu