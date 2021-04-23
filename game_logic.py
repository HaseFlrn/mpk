from line_to_string import line_to_string
from any_of import any_of
from get_func import get_all_lines
from get_func import get_row

def contains_combo(l,c):
    '''Erwartet eine Liste l und einen Charakter c.
        Liefert True, wenn c viermal aufeinander-folgend in l ist.
    '''
    return line_to_string(l).find(line_to_string([c for i in range(4)])) != -1


def player_wins(a,i,j,c):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i, eine Zahl j und einen Charakter c.
        Liefert True, wenn in einer Zeile, Reihe oder Diagonalen, in der a[i][j] liegt, 4 c aufeinander folgen.
    '''
    contains_combo_c = lambda l: contains_combo(l,c)
    return any_of(get_all_lines(a,i,j), contains_combo_c)


def player_x_wins(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert True, wenn in einer Zeile, Reihe oder Diagonalen, in der a[i][j] liegt, 4 X aufeinander folgen.
    '''
    return player_wins(a,i,j,'X')

def player_o_wins(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert True, wenn in einer Zeile, Reihe oder Diagonalen, in der a[i][j] liegt, 4 O aufeinander folgen.
    '''
    return player_wins(a,i,j,'O')

def board_full(b):
    '''Erwartet ein zweidimensionales Array b.
        Liefert True, wenn die 0-te Zeile gefüllt ist.
    '''
    return line_to_string(get_row(b,0)).find(" ") == -1

