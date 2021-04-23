from get_func import get_manipulation_point
from board_to_string import board_to_string
from game_logic import player_o_wins
from game_logic import player_x_wins
from game_logic import board_full


def generate_board(n,m):
    '''Erwartet eine Zahl n und eine Zahl m.
        Liefert ein zweidimensionales Array mit Ausprägung n Zeilen auf m Spalten.
    '''
    return [[" " for i in range(m)] for j in range(n)]


def manipulate(a,c): #vielleicht als list comprehension umschreiben
    '''Erwartet ein zweidimensionales Array a und einen Charakter c.
        Liefert das an Stelle [i][j] mit c manipulierte Array a.
    '''
    new_a = a.copy() 
    i,j = get_manipulation_point(a,c)
    new_a[i][j] = c
    return new_a, i, j


#vorübergehende Lösung?
def show_board(b):
    '''Erwartet ein zweidimensionales Array b.
        Gibt b als Spielfeld in der Konsole aus.
    '''
    print(board_to_string(b))


def game_round(b):
    '''Erwartet ein zweidimensionales Array b.
        Spielt eine Runde des Spiels durch.
        Liefert 0, wenn Spieler X gewonnen hat.
        Liefert 1, wenn Spieler O gewonnen hat.
        Liefert 2, wenn noch keiner gewonnen hat.
        Liefert -1 bei einem Unentschieden.
        [TODO] Funktion verkürzen, indem Spielerwechsel parametergesteuert gemacht wird
    '''
    show_board(b)
    b, i, j = manipulate(b,"X")
    if player_x_wins(b, i, j):
        show_board(b)
        return 0
    if board_full(b):
        show_board(b)
        return -1
    show_board(b)
    b, i, j = manipulate(b,"O")
    if player_o_wins(b, i, j):
        show_board(b)
        return 1
    if board_full(b):
        show_board(b)
        return -1
    return 2

#Testfunktionen auslagern
def test_generate_board():
    assert(generate_board(2,3) == [[' ', ' ', ' '], [' ', ' ', ' ']])
    assert(not generate_board(2,3) == [[' ', ' '], [' ', ' '], [' ', ' ']])

def test_manipulate():
    a1 = [['X','X',' '],['X','X','X'],['X','O','O']]
    print("Erwartet 2 als Input, sonst erneute Eingabe: ")
    assert(manipulate(a1,'X') == ([['X','X','X'],['X','X','X'],['X','O','O']], 0, 2))


if __name__ == "__main__":
    test_generate_board()
    test_manipulate()