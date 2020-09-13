"""
This is a main file where the game should be run.
"""

from exceptions import GameOver, EnemyDown
from models import Player, Enemy
from settings import BEST_SCORE_LIMIT, COMMANDS


def play():
    player_name = input('Name yourself: ')
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)

    while True:
        start = input('Type "start" to begin: ')

        if start.strip().lower() == 'start' :
            break

        print('Make sure you are entering a correct command.')

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            level += 1
            player.score += 5
            enemy = Enemy(level)

            print(f'--------------\nYour score is - {player.score}')
            print(f'Your lives - {player.lives}\n--------------')
            print('This round has ended, choose what you want to do now:\n' + COMMANDS)

            while True:
                command_option = input('\nYour input: ')
                try:
                    command_option = command_option.strip().lower()
                except TypeError:
                    print('Make sure you have entered something.')

                if command_option == 'show scores':
                    GameOver.read_score()

                if command_option == 'exit':

                    print(f'Your total score {player.score}')
                    GameOver.write_score(player, GameOver.check_score(), BEST_SCORE_LIMIT)

                    raise GameOver from None

                if command_option == 'help':
                    print(COMMANDS)

                if command_option == 'continue':
                    break

        except GameOver as game_over:

            print(f'Your final score {player.score}')
            GameOver.write_score(player, GameOver.check_score(), BEST_SCORE_LIMIT)

            raise game_over from None


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print('You have decided to leave our game in a wrong way!!1')

    except GameOver:
        print('You have failed!')

    finally:
        print('Good bye!')
