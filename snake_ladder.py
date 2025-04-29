""" Snakes and Ladders game"""

import random
import sys


class Card:
    """
    Initializes set of values for ladder
    """

    def output(self, data):
        banner = "+" + "-" * (len(data)-2) + "+"
        border = "|" + " " * (len(data)-2) + "|"
        lines = [banner, border, data, border, banner]
        card = "\n".join(lines)
        print(card)
        print()


class Snake:
    """
    Initializes set of values for snake
    """

    def __init__(self):
        self.snake_data = {
            8: 4,
            18: 1,
            26: 10,
            39: 5,
            51: 6,
            54: 36,
            56: 1,
            60: 23,
            75: 28,
            83: 45,
            85: 59,
            90: 48,
            92: 25,
            97: 87,
            99: 63
        }

    def check_snake_bite(self, position):
        if(position in self.snake_data):
            new_pos = self.snake_data.get(position)
            print("You got a snake bite...")
            print("Your current position is {0}".format(str(new_pos)))
            return new_pos
        return position


class Ladder:
    """
    Initializes set of values for ladder
    """

    def __init__(self):
        self.ladder_data = {
            3: 20,
            6: 14,
            11: 28,
            15: 34,
            17: 74,
            22: 37,
            38: 59,
            49: 67,
            57: 76,
            61: 78,
            73: 86,
            81: 98,
            88: 91
        }

    def check_ladder_jump(self, position):
        if(position in self.ladder_data):
            new_pos = self.ladder_data.get(position)
            print("You got a ladder jump...")
            print("Your current position is {0}".format(str(new_pos)))
            return new_pos
        return position


class Player:
    """
    Set number of players in game and their names
    """

    def set_no_of_players(self, players):
        if(self.validate_player_input(players)):
            self.no_of_players = players
            return True

        return False

    def validate_player_input(self, players):
        try:
            if((int(players) >= 2) and (int(players) <= 4)):
                return True

        except(Exception):
            return False

        return False


class Board:
    """
    Sets player position on board
    """

    def check_current_pos(self, curr_pos, dice_value, snake, ladder):
        new_pos = curr_pos + dice_value
        if(new_pos > 100):
            print("You can't move next...you require {0} to win".format(
                str(100 - curr_pos)))
            return curr_pos

        print("Your current position is {0}".format(str(new_pos)))

        # check for snake bite
        new_pos = snake.check_snake_bite(new_pos)

        # check for ladder jump
        new_pos = ladder.check_ladder_jump(new_pos)

        return new_pos


class Dice:
    """
    Generates random value on roll of dice
    """

    def get_dice_number(self):
        dice_value = random.randint(1, 6)
        print("Dice rolled number :{0}".format(str(dice_value)))
        return dice_value


class Game:
    """
    Run Game
    """

    def __init__(self):
        self.welcome_message = "Welcome to Snakes and Ladders Game"
        self.no_of_players = 0

    def start(self, card):
        card.output(self.welcome_message)

    def set_no_of_players(self, card):
        set_player = False
        player = Player()
        while(not set_player):
            self.no_of_players = input("Enter number of players b/w 2 to 4: ")
            set_player = player.set_no_of_players(self.no_of_players)

        player_data = "Total players in this game are : {0}\n".format(
            self.no_of_players)
        for player in range(1, int(self.no_of_players) + 1):
            player_data += "Player {0}\n".format(str(player))

        card.output(player_data)

    def check_win(self, position, player, card):
        if(position == 100):
            card.output("Player {0} wins".format(str(player)))
            # print("Player {0} wins".format(str(player)))
            sys.exit(1)

    def play_turn(self, card):
        player_position = list()
        for player in range(1, int(self.no_of_players) + 1):
            player_position.append(1)

        dice = Dice()
        board = Board()
        snake = Snake()
        ladder = Ladder()
        while True:
            print("-------------------------------")
            for player in range(1, int(self.no_of_players) + 1):
                print("Player {0} current position now is {1}".format(
                    str(player), str(player_position.__getitem__(player - 1))))

            for player in range(1, int(self.no_of_players) + 1):
                print("Player {0} turn now".format(str(player)))
                data = input("Press enter to roll dice...")
                dice_value = dice.get_dice_number()
                player_position[player - 1] = board.check_current_pos(
                    player_position[player - 1], dice_value, snake, ladder)
                self.check_win(player_position[player - 1], player, card)
            print("-------------------------------")
            print()


def main():
    game = Game()
    card = Card()
    game.start(card)
    game.set_no_of_players(card)
    game.play_turn(card)


if __name__ == '__main__':
    main()
