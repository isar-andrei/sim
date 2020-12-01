import random
from typing import Tuple

from adventure.Skill import Skill
from adventure.Hero import Hero
from adventure.Character import Character


class CriticalStrike(Skill):
    def __init__(self, user: Character):
        super().__init__('Critical Strike', user)

    def apply_effect(self, damage: float) -> Tuple[float, bool]:
        if isinstance(self.user, Hero):
            skill_chance = random.randint(0, 101)
            if skill_chance == 1:
                return damage * 3, True
            elif skill_chance <= 10:
                return damage * 2, True
        return damage, False
