import random
from typing import Tuple, List

from adventure.Skill import Skill
from adventure.Hero import Hero
from adventure.Character import Character
from adventure.Turn import Turn


class Resilience(Skill):
    def __init__(self, user: Character):
        super().__init__('Resilience', user)

    def apply_effect(self, damage: float, battle_log: List[Turn]) -> Tuple[float, bool]:
        if isinstance(self.user, Hero):
            off_cooldown = True
            if len(battle_log):
                skills_last_turn = battle_log[-1].skills_used
                for skill in skills_last_turn:
                    if skill.name == 'Resilience':
                        off_cooldown = False
            skill_chance = random.randint(0, 101)
            if skill_chance <= 20 and off_cooldown:
                return damage / 2, True
        return damage, False
