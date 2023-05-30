import re


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

    def get_user_entries(self, data, data_type):
        """Interface to get a input from user"""
        if data_type == "string":
            user_entry = input(f"{data} : ")
            user_entry_check = "".join(user_entry.split())
            print(user_entry_check)
            while not user_entry_check.isalpha():
                print(f"{data} must be a string")
                user_entry = input(f"{data} : ")
                user_entry_check = "".join(user_entry.split())
        if data_type == "int":
            user_entry = input(f"{data} : ")
            while not user_entry.isdigit():
                print(f"{data} must be a number")
                user_entry = input(f"{data} : ")
        if data_type == "date":
            user_entry = input(f"{data} : ")
            while True:
                try:
                    day, month, year = user_entry.split("/")
                    if not (
                        1 <= int(day) <= 31 and 1 <= int(month) <= 12 and len(year) == 4
                    ):
                        raise ValueError
                    break
                except ValueError:
                    print(f"{data} must be in the format DD/MM/YYYY")
                    user_entry = input(f"{data} (DD/MM/YYYY): ")
        if data_type == "INE":
            user_entry = input(f"{data} : ")
            while not re.match(r"[A-Z]{2}\d{5}", user_entry):
                print(f"{data} must be in the format 2 letters then 5 numbers")
                user_entry = input(f"{data} : ")
        if data_type == "result":
            user_entry = input(f"{data} : ")
            while not (user_entry == "1" or user_entry == "2" or user_entry == "N"):
                print(f"{data} must be a 1/N/2")
                user_entry = input(f"{data} : ")
        return user_entry


if __name__ == "__main__":
    views = Views()
    data = "test string"
    data_type = "result"
    print(views.get_user_entries(data, data_type))
