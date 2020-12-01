import random
from adventure.Character import Character


class Villain(Character):
    def __init__(self):
        super().__init__(random.choice(['Bahamut Prime', 'Alexander Prime', 'Omega', 'Ifrit', 'Garuda', 'Titan']))
        self.health = self.assign_status_value(60, 90)
        self.strength = self.assign_status_value(60, 90)
        self.defence = self.assign_status_value(40, 60)
        self.speed = self.assign_status_value(40, 60)
        self.luck = self.assign_status_value(25, 40)
