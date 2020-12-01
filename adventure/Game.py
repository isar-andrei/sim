from typing import Tuple, List
from columnar import columnar
from copy import copy
import random

from adventure.Character import Character
from adventure.Hero import Hero
from adventure.Villain import Villain
from adventure.CriticalStrike import CriticalStrike
from adventure.Resilience import Resilience
from adventure.Turn import Turn


class Game:
    __battle_log: List[Turn] = []
    __winner: Character = None

    def __init__(self, hero: Hero, villain: Villain):
        self.__hero = hero
        self.__villain = villain

    def __str__(self):
        message = ''
        for turn in self.__battle_log:
            message += str(turn)
        message += '\n' + self.__winner.name + ' has won !'

        return message

    def play(self):
        """
        Play the game
        """
        print(self.__characters_status())
        attacker, defender = self.__who_starts()
        turn_number = 0

        while turn_number < 20 and attacker.health > 0 and defender.health > 0:
            turn_number += 1
            damage, skills_used = self.__calculate_damage(attacker, defender)
            if defender.health - damage < 0:
                defender.health = 0
            else:
                defender.health -= damage

            self.__battle_log.append(Turn(turn_number, copy(attacker), copy(defender), skills_used, damage))
            attacker, defender = defender, attacker  # at the end of the turn swap attack and defender

        self.__winner = self.__who_won(attacker, defender)

    def __calculate_damage(self, attacker: Character, defender: Character) -> Tuple[float, List]:
        """
        Based on the attackers and defenders statuses and skills determine the damage dealt
        """
        damage = max(0, attacker.strength - defender.defence)

        # is the defender lucky?
        miss_chance = random.randint(0, 101 + defender.luck)
        if miss_chance < attacker.luck:
            damage = 0

        # use skills
        skills_used = []

        # critical strike
        skill = CriticalStrike(attacker)
        damage, did_activate = skill.apply_effect(damage)
        if did_activate:
            skills_used.append(skill)

        # resilience
        skill = Resilience(defender)
        damage, did_activate = skill.apply_effect(damage, self.__battle_log)
        if did_activate:
            skills_used.append(skill)

        return damage, skills_used

    def __who_starts(self) -> Tuple[Character, Character]:
        """
        Determine who starts based on speed and then on luck, if both are equal the hero starts because plot armor
        """
        if self.__hero.speed < self.__villain.speed:
            return self.__villain, self.__hero
        elif self.__hero.speed == self.__villain.speed:
            if self.__hero.luck < self.__villain.luck:
                return self.__villain, self.__hero
        return self.__hero, self.__villain

    def __who_won(self, attacker: Character, defender: Character) -> Character:
        """
        Determine based on the remaining health who won
        """
        return attacker if attacker.health > defender.health else defender

    def __characters_status(self):
        """
        Returns a table containing the character status of both the hero and the villain
        """
        status_values = [
            ['Hero', self.__hero.name, self.__hero.health, self.__hero.strength, self.__hero.defence, self.__hero.speed,
             self.__hero.luck],
            ['Villain', self.__villain.name, self.__villain.health, self.__villain.strength, self.__villain.defence,
             self.__villain.speed, self.__villain.luck]
        ]

        status_table = columnar(status_values, headers=['Type', 'Name', 'Health', 'Strength', 'Defence', 'Speed', 'Luck'])

        return status_table
