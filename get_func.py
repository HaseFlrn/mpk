from player_input import convertable_to_int, input_in_bounds

def get_row(a: list, i: int):
    '''Erwartet ein zweidimensionales Array a und eine Zahl i.
        Liefert die i-te Zeile aus a.
    '''
    return a[i]


def get_column(a: list, j: int):
    '''Erwartet ein zweidimensionales Array a und eine Zahl j.
        Liefert die j-te Spalte.
    '''
    return [a[i][j] for i in range(len(a))]


def flip_row(a: list, i: int):
    '''Erwartet ein zweidimensionales Array a und eine Zahl i.
        Liefert das Array um die Y-Achse gespiegelt zurück.
    '''
    l = get_row(a,i)
    return [l[len(l)-1-j] for j in range(len(l))]


def flip(a: list):
    '''Erwartet ein zweidimensionales Array a.
        Liefert ein um die y-Achse gespiegeltes Array. 
    '''
    return [flip_row(a,i) for i in range(len(a))]


def prep_diag(a: list, i: int, j: int):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert i und j in der tiefsten Ebene des Arrays.
    '''
    #verschiebt die gegebene Position so lange diagonal um 1, bis man an einen Rand von a gelangt
    if i+1 < len(a) and j+1 < len(a[i]):
        return prep_diag(a,i+1,j+1)
    return i,j


def calc_diag(a: list, i: int, j: int):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert die Diagonale von rechts unten nach links oben, in der a[i][j] liegt.
    '''
    if i == 0 or j == 0:
        return [a[i][j]]
    return [a[i][j]] + calc_diag(a,i-1,j-1)


def get_diag1(a: list, i: int, j: int):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert die Diagonale von rechts unten in der das Element a[i][j] liegt.
    '''
    (i, j) = prep_diag(a,i,j)
    return calc_diag(a,i,j)


def get_diag2(a: list, i: int, j: int):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert Diagonale von links unten in der das Element a[i][j] liegt.
    '''
    return get_diag1(flip(a),i,len(a[i])-1-j) #j muss sozusagen um die i-Achse gespiegelt werden, um damit richtig weiterrechnen zu können.(offset)


def get_all_lines(a: list, i: int, j: int):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl.
        Liefert alle Reihen/Zeilen/Diagonalen, in denen a[i][j] liegt als eine Liste.
    '''
    return [get_column(a,j), get_row(a,i), get_diag1(a,i,j), get_diag2(a,i,j)]


def get_insertionpoint(l: list, i: int):
    '''Erwartet eine Liste l und eine Zahl i.
        Liefert das hinterste Leerzeichen in der Liste (später im Spielfeld das tiefste freie Feld). 
        Liefert -1, wenn kein Leerzeichen existiert.
    '''
    if i < 0 :
        return -1
    if l[i] == ' ':
        return i
    return get_insertionpoint(l,i-1)



def get_manipulation_point(board: list, player: str, get_player_input):
    '''Erwartet ein zweidimensionales Array a und einen Charakter player und eine Inputfunktion get_player_input.
        Bestimmt die erste freie Zeile in der Spalte col des Arrays board.
        Liefert das Zahlentupel (row, col).
    '''
    col = get_player_input()
    if convertable_to_int(col):
        col = int(col)
    else:
        return get_manipulation_point(board, player, get_player_input)
        
    if not input_in_bounds(board,col):
        print("Eingabe fehlerhaft, versuchs nochmal.")
        return get_manipulation_point(board, player, get_player_input)

    row = get_insertionpoint(get_column(board,col),len(get_column(board,col))-1) #Übergabe der relevanten Spalte und der letzten Position darin, um die Zeile des untersten freien Feldes in der Spalte zu bestimmen.

    if row == -1:
        print("Zeile voll, versuchs nochmal.")
        return get_manipulation_point(board, player, get_player_input)
        
    return row, col

