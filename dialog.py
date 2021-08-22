class Dialog():

    @staticmethod
    def display(dialog: str, choices: list):                
        print(dialog)
        print()
        choice = Dialog.display_menu(choices)
        print(choice)

    @staticmethod
    def display_menu(choices: list):
        index = 0
        for choice in choices:
            print(f"{index}) {choice}")
            index += 1
        while True:
            try:
                user_input = int(input())
                return choices[user_input]
            except ValueError:
                pass
