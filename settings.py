"""
Constants are stored here.
"""

from enum import IntEnum


NUMBER_OF_LIVES = 10
BEST_SCORE_LIMIT = 4


class AllowedAttacks(IntEnum):
    """
    Storing digits for possible attacks.
    """
    MAGE = 1
    WARRIOR = 2
    ROGUE = 3


COMMANDS = """
show scores - will show you current top of scores.txt
exit - will make you fail and exit the game
help - you will see all the commands
continue - continue your game till the next enemy down"""