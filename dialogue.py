# Dialogue objects contain multiple questions/statements.
# A dialogue flows based on the 4 choices that are made.
# Each dialogue part is 4 bits, based on the choice the player made.
# All dialogue parts are strewn together, creating a series of bits. (choice path)

class Dialogue():

    def __init__(self):        
        self.choice_path = 0
        self.dialogues = []

