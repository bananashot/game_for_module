"""
random - generate random attacks for enemy
settings - constants
exceptions - custom exceptions
"""
from random import randint

from settings import NUMBER_OF_LIVES, AllowedAttacks
from exceptions import EnemyDown, GameOver


class Enemy:
    """
    Creation of an enemy.
    """

    def __init__(self, level):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        """
        Selecting one of three attacks.
        """
        return randint(1, 3)

    def decrease_lives(self):
        """
        Reducing lives on attacks.
        """
        self.lives -= 1

        if self.lives:
            return self.lives

        print('Enemy killed!')
        raise EnemyDown


class Player:
    """
    Creation of a player.
    """

    def __init__(self, name):
        self.name = name
        self.lives = NUMBER_OF_LIVES
        self.score = 0
        self.allowed_attacks = AllowedAttacks

    @staticmethod
    def fight(attack, defence):
        """
        Logic for a fight, method decides a result of a fight
        """
        if attack == defence:
            return 0

        if attack in (defence + 1, defence - 2):
            return 1

        return -1

    def decrease_lives(self):
        """
        Reducing lives on attacks.
        """
        self.lives -= 1

        if not self.lives:
            raise GameOver

    @staticmethod
    def check_allowed_attacks(user_input):

        allowed_attack_list = list(map(int, AllowedAttacks))

        try:
            user_input = int(user_input.strip())

            if int(user_input) in allowed_attack_list:
                return user_input

            print('This digit is not from allowed ones.')

        except AttributeError:
            print('Make sure you are entering a digit.')

        except ValueError:
            print('Make sure you are entering a digit.')

        return 0

    def attack(self, enemy_obj):

        while True:

            user_input = self.check_allowed_attacks(
                input('Choose attack option from set of: 1, 2, 3: ')
                )

            if user_input:
                break

        player_attack = user_input
        battle_result = Player.fight(player_attack, enemy_obj.select_attack())

        if battle_result == 0:
            print("It's a draw!")

        if battle_result == 1:
            self.score += 1
            enemy_obj.decrease_lives()
            print("You attacked successfully!")

        if battle_result == -1:
            print("You missed!")

    def defence(self, enemy_obj):

        while True:

            user_input = self.check_allowed_attacks(
                input('Choose defence option from set of: 1, 2, 3: ')
            )

            if user_input:
                break

        player_defence = user_input
        battle_result = Player.fight(enemy_obj.select_attack(), player_defence)

        if battle_result == 0:
            print("It's a draw!")

        if battle_result == 1:
            self.decrease_lives()
            print("You missed the attack!")

        if battle_result == -1:
            print("You have succeeded in defence!")
