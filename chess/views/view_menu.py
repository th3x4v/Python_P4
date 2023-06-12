import re
from tabulate import tabulate


class Views:
    """
    Display of the menu
    """

    def __init__(self):
        pass

    def display_menu(
        self,
        title1,
        title2="",
        choice0="",
        choice1="",
        choice2="",
        choice3="",
        choice4="",
        table=None,
    ):
        print(f"\n*** {title1} ***\n".upper())
        if table is not None:
            self.display_list(table[0], header=table[1])
        print(f"{title2}\n".upper())
        print(choice0)
        print(choice1)
        print(choice2)
        print(choice3)
        print(choice4)
        choice_menu = input("choice: ")
        return choice_menu

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

    def display_list(self, data, header=[], data_select=None):
        """Display a list selecting data"""
        lengh = len(data)
        if data_select is None:
            data_select = range(lengh)
        data_filter = [data[i] for i in range(lengh) if i in data_select]
        table = tabulate(data_filter, headers=header, tablefmt="grid")
        print(table)

    def display_message(self, message):
        """Simple display"""
        print(message)


if __name__ == "__main__":
    views = Views()
    data = "test string"
    data_type = "result"
    print(views.get_user_entries(data, data_type))
    data = [
        ("Kim", "", "Chene"),
        ("Jae", "VS", "Lin"),
        ("29/09/1995", "", "17/08/1994"),
        ("TY56432", "", "BF85325"),
        (24.0, "", 21.5),
        (5, "", 6),
    ]
    header = ["1", "N", "2"]
    views.display_list(data)
    views.display_list(data, header)
    views.display_list(data, header, (0, 1, 3))
