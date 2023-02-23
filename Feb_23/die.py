import random
class Die:
    def __init__(self, number_of_sides) -> None:
        super().__init__()
        self.numberofsides=number_of_sides

    def role_die(self):
        return random.randint(1,self.numberofsides)
