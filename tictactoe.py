"""
Tic Tac Toe Player
"""

import math
import copy

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

    if terminal(board) == True:
        return None

    # check the number of X and O in the board. If num(X) = num (O), then it's X's turn.
    xCounter = 0
    oCounter = 0
    
    for line in board:
        for element in line:
            if element == "X":
                xCounter = xCounter + 1
            elif element == "O":
                oCounter = oCounter + 1
    if xCounter == oCounter and xCounter == 0:
        return X
    elif xCounter <= oCounter:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) == True:
        return None
    
    actionSet = []
    outerIndex = 0
    for line in board:
        innerIndex = 0
        for element in line:
            if element == None:
                action = (outerIndex, innerIndex)
                actionSet.append(action)
            innerIndex = innerIndex + 1
        outerIndex = outerIndex + 1
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    ## Issue is result is called too many times and action was not valid
    if action == None:
        raise Exception
    
    copyBoard = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    
    whoseTurn = player(board)
    if whoseTurn == X:
        copyBoard[i][j] = "X"
    elif whoseTurn == O:
        copyBoard[i][j] = "O"
        
    return copyBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board == None:
        return None
    
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return X
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return O
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return X
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return O
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return X
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return O
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return X
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return O
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return X
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return O
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return X
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return O
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return X
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return O
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return X
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == "X" or winner(board) == "O":
        return True
    else:
        for line in board:
            for element in line:
                if element == EMPTY:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    #continue if the game is not over
    if terminal(board) == False:

        currentPlayer = player(board)
        copyBoard = copy.deepcopy(board)
        bestBoard = copy.deepcopy(board)
        
        # X is the current player
        if currentPlayer == X:
            bestValue = -1
            bestMove = (-1, -1)
            
            for action in actions(board):
                moveValue = oTurns(result(board, action))
                #These 3 lines below are very critical! It breaks the loop once it finds the best move. 
                if moveValue == 1:
                    bestMove = action
                    break
                if moveValue > bestValue:
                    bestMove = action
            return bestMove
            
        # O is the current player
        elif currentPlayer == O:
            bestValue = 1
            bestMove = (-1, -1)
            for action in actions(board):
                moveValue = xTurns(result(board, action))
                #These 3 lines below are very critical! It breaks the loop once it finds the best move. 
                if moveValue == -1:
                    bestMove = action
                    break
                if moveValue < bestValue:
                    bestMove = action
            return bestMove
            
        
    # If the game is over, 
    else:
        return None


def xTurns(copyBoard):
    if terminal(copyBoard) == True:
        return utility(copyBoard)

    v = -1
    for action in actions(copyBoard):
        v = max(v, oTurns(result(copyBoard, action)))
        if v == 1:
            break
    return v
        

def oTurns(copyBoard):
    if terminal(copyBoard):
        return utility(copyBoard)
    v = 1
    for action in actions(copyBoard):
        v = min(v, xTurns(result(copyBoard, action)))
        if v == -1:
            break
    return v
