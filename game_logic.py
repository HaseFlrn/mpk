from helper_func import any_of, line_to_string
from get_func import get_all_lines
from get_func import get_row

def contains_combo(line: list, player: str):
    '''Erwartet eine Liste line und einen Charakter player.
        Liefert True, wenn player viermal aufeinander-folgend in line ist.
    '''
    return line_to_string(line).find(player*4) != -1


def player_wins(board: list, row: int, col: int, player : str):
    '''Erwartet ein zweidimensionales Array board, eine Zahl row, eine Zahl col und einen Charakter player.
        Liefert True, wenn in einer Zeile, Reihe oder Diagonalen, in der board[row][col] liegt, 4 player aufeinander folgen.
    '''
    contains_combo_player = lambda l: contains_combo(l,player)
    return any_of(get_all_lines(board,row,col), contains_combo_player)


def player_x_wins(board: list, row: int, col: int):
    '''Erwartet ein zweidimensionales Array board, eine Zahl row und eine Zahl col.
        Liefert True, wenn in einer Zeile, Reihe oder Diagonalen, in der board[row][col] liegt, 4 'X' aufeinander folgen.
    '''
    return player_wins(board, row, col,'X')

def player_o_wins(board: list, row: int, col: int):
    '''Erwartet ein zweidimensionales Array board, eine Zahl row und eine Zahl col.
        Liefert True, wenn in einer Zeile, Reihe oder Diagonalen, in der board[row][col] liegt, 4 'O' aufeinander folgen.
    '''
    return player_wins(board, row, col,'O')

def board_full(board: list):
    '''Erwartet ein zweidimensionales Array board.
        Liefert True, wenn die 0-te Zeile und somit das Spielfeld komplett gefüllt ist.
    '''
    return line_to_string(get_row(board,0)).find(" ") == -1

