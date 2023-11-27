"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    empty_spaces = 0
    count_o = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_spaces += 1
    if (empty_spaces %2) == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    result_board = copy.deepcopy(board)
    result_board[i][j] = player(result_board)
   
    return result_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_possibilites =[{(0, 0), (0, 1), (0, 2)}, {(1, 0), (1, 1), (1, 2)}, {(2, 0), (2, 1), (2, 2)},
                {(0, 0), (1, 0), (2, 0)}, {(0, 1), (1, 1), (2, 1)}, {(0, 2), (1, 2), (2, 2)},
                    {(0, 0), (1, 1), (2, 2)}, {(0, 2), (1, 1), (2, 0)}]
    board_pos_X = set()
    board_pos_O = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                board_pos_X.add((i, j))
            if board[i][j] == O:
                board_pos_O.add((i, j))
    for win_pos in win_possibilites:
        if win_pos.issubset(board_pos_X):
            return X
        elif win_pos.issubset(board_pos_O):
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board):
        return True
    for i in range(3):
        if EMPTY in board[i]:
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
    else: return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board. (i, j)
    """
    
    def min_value(board):
        v = math.inf
        for action in actions(board):
            state = result(board, action)
            if terminal(state):
                v = min(v, utility(state))
            else:
                v = min(v, max_value(state))
        return v
            

    def max_value(board):
        v = -math.inf
        for action in actions(board):
            state = result(board, action)
            if terminal(state):
                v = max(v, utility(state))
            else:
                v = max(v, min_value(state))
        return v
    

    if terminal(board):
        return None
    current_board = board
    current_player = player(board)
    current_actions = actions(current_board)

    if current_player == X:
        action_values = {-1: [], 0: [], 1: []}
        if len(current_actions) == 1:return current_actions.pop()
        elif len(current_actions) > 7: return random.choice(list(current_actions))
        else:
            for action in current_actions:
                if terminal(result(current_board, action)): return action
                else:
                    v = -math.inf
                    v_curr_action = max(v, min_value(result(current_board, action)))
                    if v_curr_action == 1: return action
                    action_values[v_curr_action].append(action)
            print(action_values)
            
            #if len(action_values[v]) > 0:
            return random.choice(action_values[0])
            
    else:
        action_values_ = {-1: [], 0: [], 1: []}
        if len(current_actions) == 1:return current_actions.pop()
        #elif len(current_actions) > 7: return current_actions.pop()
        else:
            for action in current_actions:
                if terminal(result(current_board, action)): return action
                else:
                    v = math.inf
                    v_curr_action = min(v, max_value(result(current_board, action)))
                    if v_curr_action == -1: return action
                    action_values[v_curr_action].append(action)
            print(action_values)
            return random.choice(action_values[0])
            


