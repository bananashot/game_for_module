"""
Custom exception file.
"""
from os.path import getsize


class EnemyDown(Exception):
    """
    Custom exception called on enemy death
    """


class GameOver(Exception):
    """
    Custom exception called on death of the player.
    Score interactions are here
    """
    @staticmethod
    def sort_scores(score_dict):

        score_dict = {
            key: value for key, value in
            sorted(score_dict.items(), key=lambda item: item[1], reverse=True)
        }

        return score_dict

    @staticmethod
    def read_score():
        """
        Checks if file exists and returns current scores
        """

        try:
            if getsize('scores.txt'):
                print('\nCurrent scores are:\n')

                with open('scores.txt', 'r') as scores:
                    score_list = scores.read().strip()
                    print(score_list)

                return
        except IOError:
            pass

        print('\nScore file is empty or absent for now!')

    @staticmethod
    def check_score():
        """
        Creates a dictionary from current score
        """
        dictionary_score = {}

        try:
            if getsize('scores.txt'):

                with open('scores.txt', 'r') as scores:

                    score_list = scores.readlines()
                    score_list = [item.strip().rsplit(': ', 1) for item in score_list]

                    for pair in score_list:
                        key, value = pair[0], pair[1]
                        dictionary_score[key] = int(value)

                    GameOver.sort_scores(dictionary_score)
        except IOError:
            pass

        return dictionary_score

    @staticmethod
    def write_score(player, score_dict, limit):
        """
        Creates a new and correct file of scores
        """

        if player.name not in score_dict:
            score_dict[player.name] = player.score

        else:
            score_dict[player.name] = max(player.score, score_dict[player.name])

        score_dict = GameOver.sort_scores(score_dict)

        with open('scores.txt', 'w') as scores:
            limited_score = {key: value for key, value in list(score_dict.items())[0:limit + 1]}

            for key, value in limited_score.items():
                scores.write(f'{key}: {value}\n')
