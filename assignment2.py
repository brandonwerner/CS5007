# Brandon Werner
# Homework 2
# CS 5007


import sys


class ConnectN:
    def __init__(self, rows=6, columns=7, winning_number=4):
        self.__game_state = []
        self.__rows = rows
        self.__columns = columns
        self.__winning_number = winning_number
        self.__player_turn = 1

        for i in range(self.__rows):
            row = []
            for j in range(self.__columns):
                row.append(0)
            self.__game_state.append(row)

        self.__last_row = -1
        self.__last_column = -1

    @property
    def game_state(self):
        return self.__game_state

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    @property
    def winning_number(self):
        return self.__winning_number

    @property
    def player_turn(self):
        return self.__player_turn

    def switch_turn(self):
        self.__player_turn = self.__player_turn = 2 - (self.__player_turn - 1)

    # DO THIS FUNCTION FIRST AND HAVE IT WORKING PROPERLY BEFORE CONTINUING
    # OTHER TEST CASES MAY PRINT THE GAME STATE, THEREFORE THIS FUNCTION MUST WORK OR ALL TESTS WILL FAIL
    # IMPLEMENT ME!
    def __str__(self):
        """
        :return: String representation of game
        """

        game_state_string = ''
        for i in range(self.__rows):
            if i > 0:
                game_state_string += "\n"
            for j in range(self.__columns):
                if j > 0:
                    game_state_string += " "

                game_state_string += str(self.game_state[i][j])

        # single string
        # syntax of table
        # 0 on to n for columns
        # 0 of to columns
        # loop through all rows
        #   loop through all columns
        #       append value to string

        return game_state_string

    # IMPLEMENT ME!
    def reset_game(self):
        # set last_row and last_column to -1
        # set all positions to empty
        self.__last_row = -1
        self.__last_column = -1

        for i in range(self.__rows):
            for j in range(self.__columns):
                self.game_state[i][j] = 0
        pass

    # IMPLEMENT ME!
    def is_game_full(self):
        """
        :return: True if game is full, otherwise false
        """

        is_full = True
        for j in range(self.__columns):
            if self.game_state[0][j] == 0:
                is_full = False
        return is_full

        # loop through all columns
        #   if top position is empty then game is not full


    # IMPLEMENT ME
    def insert_chip(self, column_number):
        """
        :return: True if chip was inserted, otherwise false
        """



        # try to insert
        # if the top position is empty
        #   start at row 0 (the top row)
        #   loop through the rows until a non-empty position is found
        # for i in range(self.__rows):
        inserted = False
        i = -1
        stop = True
        while i < self.rows and not inserted and stop:
            if i == -1 and self.game_state[i+1][column_number] != 0:
                stop = False
                inserted = False
            elif (i + 1) == self.rows:
                self.game_state[i][column_number] = self.player_turn
                inserted = True
            elif self.game_state[i+1][column_number] != 0:
                self.game_state[i][column_number] = self.player_turn
                inserted = True

            i += 1
        return inserted


        #while i < self.rows and not inserted:
         #   if self.game_state[i][column_number] != 0:
          #      self.game_state[i][column_number] = self.player_turn
           #     inserted = True
            #i += 1
        #return inserted
        #   set game state position to the player number
        #game_state = self.__player_turn
        #   inserted = true
        #   set last row and last column to the inserted position
        #self.__last_row = self.insert_chip[i]
        #self.__last_column = self.insert_chip[j]


    # IMPLEMENT ME
    def detect_win(self):
        """
        :return: Winning player number, otherwise -1
        """
        winner = -1
        #winner = self.__winning_number



        # add some logic with the following win detection functions
        # detect win by columns
        # detect win by rows
        # detect by by diagonals

        return winner

    # IMPLEMENT ME!
    def detect_win_by_column(self):
        """
        :return: Winning player number, otherwise -1
        """

        win_column = -1
        last_position = (self.__game_state[self.__last_row])
        i = self.__last_row
        chip_count = (self.__winning_number - self.__last_row)
        while i < self.__rows:
            # determine chip count position by subtracting winning number required from last_position
            if last_position == self.__player_turn:
                chip_count += 1
            i += 1
            #count consecutive chips >= winning number
        if chip_count >= self.winning_number:
            win_column = self.player_turn

        return win_column

        # start at last position

        # loop down the column as far as needed
        # set win_column if count of consecutive chip color >= winning_number



    # IMPLEMENT ME!
    def detect_win_by_row(self, chip_count):
        """
        :return: Winning player number, otherwise -1
        """

        win_row = -1
        last_player = self.__game_state[self.__last_row][self.__last_column]
        count = 1
        stop_left = False
        stop_right = False
        last_position = (self.__game_state[self.__last_row])
        # search to the left
        # loop starting at last_column-1 until out of bounds or stop_left = True
        #while
        #   if value at current position == current player
        #       increment consecutive chip count
        if last_position == self.__player_turn:
            chip_count += 1
        else:
               stop_left = True

        # search to the right

        # similar to left

        return win_row

    # IMPLEMENT ME!
    def detect_win_by_diagonal(self):
        """
        :return: Winning player number, otherwise -1
        """

        win_diagonal = -1
        last_player = self.__game_state[self.__last_row][self.__last_column]
        count_left_to_right = 1
        count_right_to_left = 1
        stop_left1 = False
        stop_right1 = False
        stop_left2 = False
        stop_right2 = False

        # left to right /
        # left
        #   use code from win rows and modify to work with changing row numbers
        # right
        #   similar to left

        # right to left \
        #   similar to (left to right)
        # left
        # right

        if count_left_to_right >= self.__winning_number or count_right_to_left >= self.__winning_number:
            win_diagonal = last_player

        return win_diagonal


# Done for you!
def main():
    rows = 6
    columns = 7
    winning_number = 4

    if len(sys.argv) == 3+1:
        rows = int(sys.argv[1])
        columns = int(sys.argv[2])
        winning_number = int(sys.argv[3])

    game = ConnectN(rows, columns, winning_number)
    keep_playing = True

    while keep_playing:
        game_on = True
        game.reset_game()

        while game_on:
            print(game)
            print('Player ' + str(game.player_turn) + '\'s turn ')
            # assumes an integer was entered
            # although you should never make this assumption on user input, I have not taught exception handling yet
            column_number = int(input('Enter a column number or -1 to exit\n'))

            # if input is invalid
            if not(column_number == -1 or (0 < column_number <= columns)):
                print('Invalid input')
            elif column_number == -1:
                game_on = False
                keep_playing = False
            else:
                inserted = game.insert_chip(column_number-1)

                if inserted:
                    winner = game.detect_win()

                    if winner != -1 or game.is_game_full():
                        print(game)
                        game_on = False
                        if winner == -1:
                            print('Tie Game')
                        else:
                            print('Player ' + str(winner) + ' has won')
                            play_again = int(input('Enter any number to play again or -1 to exit\n'))
                            if play_again == -1:
                                keep_playing = False
                    else:
                        game.switch_turn()
                else:
                    print('Cannot insert a chip in that column')


if __name__ == '__main__':
    main()
