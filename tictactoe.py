import os
import time
import random
import sys

class Tictactoe:

    the_board = "012345678"
    play = True
    def __init__(self):
        pass

    def draw(self, board):
        print("\n")
        for i in range(3):
            print(
                f"{' '*7}|{' '*7}|",
                f"{' '*4}{board[i+(0,2,4)[i]]}{' '*2}|{' '*3}{board[i+1+(0,2,4)[i]]}{' '*3}|{' '*2}{board[i+2+(0,2,4)[i]]}",
                f"{' '*7}|{' '*7}|",
                sep="\n",
            )
            if i != 2:
                print("-" * 24)
        print("\n")

    def play(self):
        players = int(input("\nHow many players?(1/2): "))
        choice_letter = input("\nChoose a letter.(x/o): ").lower()
        letters = "xo" if choice_letter == "x" else "ox"
        if players == 2:
            self.draw("012345678")
            turn = 0
            while not self.game_done(self.the_board):
                position = input(
                    f"Let player {turn+1} ({letters[turn]}) enter a position: "
                )
                if self.the_board[int(position)].isdigit():
                    self.the_board = self.the_board.replace(position, letters[turn])
                    turn = (turn + 1) % 2
                else:
                    print("\nThe position is already occupied. \n")
                    time.sleep(3)
                the_new_board = self.the_board
                for i in the_new_board:
                    if i.isdigit():
                        the_new_board = the_new_board.replace(i," ")
                os.system("cls")
                self.draw(the_new_board)
                self.draw("012345678")

        else:
            turn = random.randint(0, 1)
            other = "x" if choice_letter == "o" else "o"
            my_string = f"\nYou will play against the computer as '{choice_letter}' and the computer will play as '{other}'.\n"
            for char in my_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(2)
            while not self.game_done(self.the_board):
                if turn == 0:
                    self.draw("012345678")
                    position = input(f"The position for the letter: ")
                    if self.the_board[int(position)].isdigit():
                        self.the_board = self.the_board.replace(position, letters[turn])
                        turn = (turn + 1) % 2
                    else:
                        print("\nThe position is already occupied. \n")
                        time.sleep(3)
                else:
                    self.play = True
                    self.computer_play(letters[turn],choice_letter)
                    turn = (turn + 1) % 2
                the_new_board = self.the_board
                for i in the_new_board:
                    if i.isdigit():
                        the_new_board = the_new_board.replace(i," ")
                os.system("cls")
                self.draw(the_new_board)

    def game_done(self,the_board):
        iterables = [
            [the_board[0], the_board[1], the_board[2]],
            [the_board[3], the_board[4], the_board[5]],
            [the_board[6], the_board[7], the_board[8]],
            [the_board[0], the_board[3], the_board[6]],
            [the_board[1], the_board[4], the_board[7]],
            [the_board[2], the_board[5], the_board[8]],
            [the_board[0], the_board[4], the_board[8]],
            [the_board[2], the_board[4], the_board[6]],
        ]
        for item in iterables:
            if item == ["x", "x", "x"]:
                print("\nX won.\n")
                return True
            elif item == ["o", "o", "o"]:
                print("\nO won.\n")
                return True
        else:
            for i in range(len(self.the_board)):
                if self.the_board[i].isdigit():
                    return False
            else:
                print("\nIt's a draw.\n")
                return True

        
    def has_won(self,the_board,the_letter):
        return ((the_board[0] == the_letter and the_board[1] == the_letter and the_board[2] == the_letter) or
                (the_board[3] == the_letter and the_board[4] == the_letter and the_board[5] == the_letter) or
                (the_board[0] == the_letter and the_board[3] == the_letter and the_board[6] == the_letter) or
                (the_board[1] == the_letter and the_board[4] == the_letter and the_board[7] == the_letter) or
                (the_board[2] == the_letter and the_board[5] == the_letter and the_board[8] == the_letter) or
                (the_board[0] == the_letter and the_board[4] == the_letter and the_board[8] == the_letter) or
                (the_board[2] == the_letter and the_board[4] == the_letter and the_board[6] == the_letter) or
                (the_board[6] == the_letter and the_board[7] == the_letter and the_board[8] == the_letter))
    
    def computer_play(self,the_letter,the_other_letter):
        empty = []
        dupe = []
        for item in self.the_board:
            dupe.append(item)
            if item.isdigit():
                empty.append(item)
        if self.play:
            try:
                try:
                    for i in range(9):
                        if dupe[i].isdigit():
                            dupe[i] = the_letter
                            if self.has_won(dupe,the_letter):
                                self.the_board = self.the_board.replace(str(i),the_letter)
                                self.play = False
                                return
                            else:
                                dupe[i] = str(i)
                except Exception as error:
                    print(error)
                else:
                    for i in range(9):
                        if dupe[i].isdigit():
                            dupe[i] = the_other_letter
                            if self.has_won(dupe,the_other_letter):
                                self.the_board = self.the_board.replace(str(i),the_letter)
                                self.play = False
                                return
                            else:
                                dupe[i] = str(i)
            except Exception as error:
                print(error)
            else:
                self.the_board = self.the_board.replace(random.choice(empty),the_letter)
                self.play = False
                return

game = Tictactoe()

game.play()
