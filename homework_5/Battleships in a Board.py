# 419. Battleships in a Board

def countBattleships(board):
    """
    We iterate over all positions of the board.
    Number of battleships is added by 1 if in certain position it is 'X' and
    row -1 and col -1 positions are '.'
    Other positions and its values do not be in account.

    | | |.| | |
    | |.|X| | |

    :param board:
    :return:
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X' and (
                    i == 0 or board[i - 1][j] == '.'
            ) and (
                    j == 0 or board[i][j - 1] == '.'):
                count += 1
    return count


a_board = [
    ["X", ".", ".", "X"],
    [".", ".", ".", "X"],
    [".", ".", ".", "X"]
]

b_board = [["."]]

print(countBattleships(a_board))



