from typing import List

from adventure.Character import Character
from adventure.Skill import Skill


class Turn:
    def __init__(self, turn_number: int, attacker: Character, defender: Character, skills_used: List[Skill],
                 damage: float):
        self.turn_number = turn_number
        self.attacker = attacker
        self.defender = defender
        self.skills_used = skills_used
        self.damage = damage

    def __str__(self):
        message = '-> Turn ' + str(self.turn_number) + ':\n'

        if self.damage == 0:
            message += self.attacker.name + ' missed the attack.'
        else:
            message += self.attacker.name + ' attacked with ' + str(self.damage) + ' damage.'

        message += '\n' + self.defender.name + ' has ' + str(self.defender.health) + ' health left.'

        if self.skills_used:
            message += '\nWere used the skill/s : '
            # TODO come back after learning lambda functions in python and make it nicer
            for skill in self.skills_used:
                message += skill.name + ', '
            size = len(message)
            message = message[:size - 2]

        message += '\n'

        return message
