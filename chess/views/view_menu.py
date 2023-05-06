class Views:
    """
    Display of the menu
    """

    def __init__(self):
        pass

    def display_main_menu(self):
        print("\n*** Chess Manager ***\n".upper())
        print("Main menu\n".upper())
        print("1 - Manage players")
        print("2 - Manage tournament")
        print("3 - Quit the application")
        choice_main_menu = input("choice: ")
        return choice_main_menu
