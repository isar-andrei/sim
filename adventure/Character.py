import random


class Character:
    health = 0
    strength = 0
    defence = 0
    speed = 0
    luck = 0

    def __init__(self, name: str):
        if not type(name) is str:
            raise TypeError("Character name needs to be a string")
        if not len(name):
            raise TypeError("Character name can't be blank")
        else:
            self.name = name

    def __str__(self):
        return self.name + '\n' + \
               'Health: ' + str(self.health) + '\n' + \
               'Strength: ' + str(self.strength) + '\n' + \
               'Defence: ' + str(self.defence) + '\n' + \
               'Speed: ' + str(self.speed) + '\n' + \
               'Luck: ' + str(self.luck) + '\n'

    def assign_status_value(self, min_value: int, max_value: int):
        if not type(min_value) is int or not type(max_value) is int:
            raise TypeError("Status values need to be integers")
        if min_value > max_value:
            raise TypeError("The minimum value can't be higher that the maximum value")
        if min_value < 0 or min_value > 100 or max_value < 0 or max_value > 100:
            raise TypeError("Status values need to be between 0 and 100")

        return random.randint(min_value, max_value + 1)
