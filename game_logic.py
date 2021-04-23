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

def test_contains_combo():
    l1 = ['O','X','X','X','X',' ']
    assert(contains_combo(l1,'X'))
    l2 = ['X','O','X','X','X',' ']
    assert(not contains_combo(l2,'X'))

def test_player_wins():
    a1 = [[" ","X"," "," "],["X","X"," "," "],["O","X"," "," "],["X","X","X","X"]]
    assert(player_wins(a1,0,1,'X'))
    a2 = [[" ","X"," "," "],["X","X"," "," "],["O","X"," "," "],["X","X","O","X"]]
    assert(player_wins(a2,1,1,'X'))
    a3 = [["X","X"," "," "],["X","X",""," "],["O","O","X"," "],["O","X","O","X"]]
    assert(player_wins(a3,0,0,'X'))

def test_player_x_wins():
    a1 = [[" ","X"," "," "],["X","X"," "," "],["O","X"," "," "],["X","X","X","X"]]
    assert(player_x_wins(a1,3,1))
    a2 = [[" ","X"," "," "],["X","X"," "," "],["O","X"," "," "],["X","X","O","X"]]
    assert(player_x_wins(a2,1,1))
    a3 = [["X","X"," "," "],["X","X",""," "],["O","O","X"," "],["O","X","O","X"]]
    assert(player_x_wins(a3,0,0))

def test_player_o_wins():
    a1 = [[" ","X"," "," "],["X","X"," "," "],["O","X"," "," "],["O","O","O","O"]]
    assert(player_o_wins(a1,3,1))
    a2 = [[" ","O"," "," "],["X","O"," "," "],["O","O"," "," "],["X","O","O","X"]]
    assert(player_o_wins(a2,1,1))
    a3 = [["O","X"," "," "],["X","O",""," "],["O","O","O"," "],["O","X","O","O"]]
    assert(player_o_wins(a3,0,0))

def test_board_full():
    b1 = [["X", "X", " "],["X", "X", "X"],["X", "X", "X"]]
    b2 = [["O", "O", " "],["O", "O", "O"],["O", "O", "O"]]
    b3 = [["O", "O", "X"],["O", "O", "O"],["O", "O", "O"]]
    assert(not board_full(b1))
    assert(not board_full(b2))
    assert(board_full(b3))


if __name__ == "__main__":
    test_contains_combo()
    test_player_wins()
    test_player_x_wins()
    test_player_o_wins()
    test_board_full()