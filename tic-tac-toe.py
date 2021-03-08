import numpy as np
from copy import deepcopy
class Board:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype = int)

    def print(self):
        for row in self.board:
            for x in row:
                if x == 1:
                    print('X', end = '\t')
                elif x == -1:
                    print('O', end = '\t')
                else:
                    print('_', end = '\t')

            print()

    def winner(self):
        for i in range(3):
            # row match
            if self.board[i][0] == self.board[i][1] and self.board[i][2] == self.board[i][1]:
                if self.board[i][0] == 1:
                    return 1
                elif self.board[i][0] == -1:
                    return -1

            # column match
            if self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i]:
                if self.board[0][i] == 1:
                    return 1
                elif self.board[0][i] == -1:
                    return -1

        # diagonal match
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[0][0]: 
            if self.board[0][0] == 1:
                return 1
            elif self.board[0][0] == -1:
                return -1
        
        # anti diagonal match
        if self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[0][2]:
            if self.board[0][2] == 1:
                return 1
            elif self.board[0][2] == -1:
                return -1

        return 0

    def all_filled(self):
        for row in self.board:
            for x in row:
                if x == 0:
                    return False
        
        return True

    def filled(self, i, j):
        return self.board[i][j] != 0

def minimax(board, depth, max_player):
    if board.winner() != 0 or depth == 0 or board.all_filled():
        return board.winner() * (-1), None

    if max_player:
        maxVal = float('-inf')
        move = None
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == 0:
                    temp_board = deepcopy(board)
                    temp_board.board[i][j] = -1
                    val, y = minimax(temp_board, depth - 1, False)
                    maxVal = max(val, maxVal)
                    if maxVal == val:
                        move = (i, j)
        
        return maxVal, move
    else:
        minVal = float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == 0:
                    temp_board = deepcopy(board)
                    temp_board.board[i][j] = 1
                    val, y = minimax(temp_board, depth - 1, True)
                    minVal = min(val, minVal)
                    if minVal == val:
                        move = (i, j)

        return minVal, move


print("Enter 1 to 9 for the cell you want to fill")

while True:
    # Create a board for the game
    board = Board()

    # Random turn selection
    rand = np.random.randint(low = 0, high = 2)
    if rand == 0:
        turn = True
    else:
        turn = False

    # Continue Playing
    while board.winner() == 0 and not board.all_filled():
        if turn:
            inp = int(input("Your turn: "))
            inp -= 1
            x = inp // 3
            y = inp % 3 
            if board.filled(x, y):
                print("Choose some other cell")
                continue

            board.board[x][y] = 1
        else:
            print("AI turn")
            val, (x, y) = minimax(board, 6, True)
            board.board[x][y] = -1

        # alternate the turns
        turn = not turn
        board.print()

    # Game result
    if board.all_filled():
        print("Game Drawn")
    elif board.winner() > 0:
        print("Congrats you win!")
    else:
        print("You lose")
    
    print("Do you want to continue again [Y/N]")
    val = input()
    if val == 'N' or val == 'n':
        break
