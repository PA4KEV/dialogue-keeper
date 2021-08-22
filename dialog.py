import config

class Dialog():

    @staticmethod
    def display(dialog: str, choices: list):                
        print(dialog)
        print()
        choice = Dialog.display_menu(choices)
        print(choice)

    @staticmethod
    def display_menu(choices: list):
        mapped_button = 0
        for choice in choices:
            print(f"{mapped_button}) {choice}")
            mapped_button += 1
        while True:
            try:
                user_input = Dialog.get_user_input()
                if user_input >= len(choices) or user_input < 0:
                    raise ValueError
                return 1 << user_input
            except ValueError:
                pass
    
    @staticmethod
    def get_user_input() -> int:
        user_input = input().upper()

        # convert to mappings
        for mapping, values in config.button_mappings.items():
            if user_input in values["mapped_buttons"]:
                print(mapping)
                return values["value"]
                
        return 99
