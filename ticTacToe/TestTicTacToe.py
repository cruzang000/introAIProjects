import copy
import unittest
import tictactoe


class TestTicTacToe(unittest.TestCase):

    # tests player function takes board and returns current player
    def test_player(self):
        board = [[tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY]]

        player = tictactoe.player(board)

        self.assertEqual(player, tictactoe.X)

    # tests actions function, takes board and returns possible actions
    # or None
    def test_actions(self):
        board = [[tictactoe.X, tictactoe.O, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.X, tictactoe.EMPTY],
                 [tictactoe.O, tictactoe.EMPTY, tictactoe.EMPTY]]

        moves = tictactoe.actions(board)

        print(moves)

    # test result function takes board and makes deep copy then returns
    # new board with passed in action completed
    def test_result(self):
        board = [[tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY]]

        newBoard = tictactoe.result(board, (0, 2))

        print(newBoard)

    # test winner function, takes board and decides if there is a winner
    # returns X, O, None
    def test_winner(self):
        board = [[tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.O, tictactoe.O, tictactoe.EMPTY],
                 [tictactoe.O, tictactoe.O, tictactoe.O]]

        winner = tictactoe.winner(board)

        print(winner)

    # test whether passed board is an ended game either by winning
    # or by full board
    def test_terminal(self):
        board = [[tictactoe.X, tictactoe.X, tictactoe.O],
                 [tictactoe.EMPTY, tictactoe.X, tictactoe.X],
                 [tictactoe.X, tictactoe.O, tictactoe.O]]

        endGame = tictactoe.terminal(board)

        print(endGame)

    # tests utility function returns utility score of game if X wins 1
    # else if O wins -1 else if a tie 0
    def test_utility(self):
        board = [[tictactoe.O, tictactoe.X, tictactoe.O],
                 [tictactoe.X, tictactoe.O, tictactoe.X],
                 [tictactoe.X, tictactoe.O, tictactoe.X]]

        utilityScore = tictactoe.utility(board)

        print(utilityScore)

    def test_minimax(self):
        board = [[tictactoe.X, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY]]

        bestMoves = tictactoe.actions(board)

        print(bestMoves)
