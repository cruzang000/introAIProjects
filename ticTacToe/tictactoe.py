"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countEmpty = sum(row.count(EMPTY) for row in board)

    # return false if count is less than one else, X or O player
    return None if countEmpty < 1 else (O if (countEmpty % 2) == 0 else X)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    movesAvailable = []

    if sum(row.count(EMPTY) for row in board) > 0:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY:
                    movesAvailable.append((i, j))

        return movesAvailable
    else:
        return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currentPlayer = player(board)
    board_temporary = copy.deepcopy(board)

    if (board[action[0]][action[1]] == EMPTY) and (currentPlayer is not None):
        board_temporary[action[0]][action[1]] = currentPlayer

        return board_temporary
    else:
        raise Exception("Move is invalid.")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # transpose columns to row
    colToRows = list(map(list, zip(*board)))
    horizontalOne = list([board[0][0], board[1][1], board[2][2]])
    horizontalTwo = list([board[0][2], board[1][1], board[2][0]])

    xWon = horizontalOne.count(X) == 3 or horizontalTwo.count(X) == 3
    oWon = horizontalOne.count(O) == 3 or horizontalTwo.count(O) == 3

    for row in range(3):
        if board[row].count(X) == 3 or colToRows[row].count(X) == 3 or xWon:
            return X
        elif board[row].count(O) == 3 or colToRows[row].count(O) == 3 or oWon:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check board for empty cells or winner
    countEmpty = sum(row.count(EMPTY) for row in board)
    hasWon = winner(board) is not None

    return countEmpty < 1 or hasWon


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if not terminal(board):

        currentPlayer = player(board)

        if currentPlayer == X:
            highestValue = -1
            for action in actions(board):
                if highestValue < min_value(result(board, action)):
                    bestMove = action
        else:
            lowestValue = 1
            for action in actions(board):
                if lowestValue > max_value(result(board, action)):
                    bestMove = action

        return bestMove
    else:
        return None


def max_value(board):

    if terminal(board):
        return utility(board)

    # set default highest value
    highestValue = -math.inf

    for action in actions(board):
        highestValue = max(highestValue, min_value(result(board, action)))

    return highestValue


def min_value(board):
    # if game ended return none
    if terminal(board):
        return utility(board)

    # set default highest value
    lowestValue = math.inf

    for action in actions(board):
        lowestValue = min(lowestValue, max_value(result(board, action)))

    return lowestValue
