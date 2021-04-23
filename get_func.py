
def get_row(a, i):
    '''Erwartet ein zweidimensionales Array a und eine Zahl i.
        Liefert die i-te Zeile aus a.
    '''
    return a[i]


def get_column(a, j):
    '''Erwartet ein zweidimensionales Array a und eine Zahl j.
        Liefert die j-te Spalte.
    '''
    return [a[i][j] for i in range(len(a))]


def flip_row(a,i):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        @param i Zeile
        Liefert das Array um die Y-Achse gespiegelt zurück.
    '''
    l = get_row(a,i)
    return [l[len(l)-1-j] for j in range(len(l))]


def flip(a):
    '''Erwartet ein zweidimensionales Array a.
        Liefert ein um die y-Achse gespiegeltes Array. 
    '''
    return [flip_row(a,i) for i in range(len(a))]


def prep_diag(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert i und j in der tiefsten Ebene des Arrays.
    '''
    if i+1 < len(a) and j+1 < len(a[i]):
        return prep_diag(a,i+1,j+1)
    return i,j


def calc_diag(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert eine Diagonale von Element a[i][j] bis an einen Rand des Arrays.
    '''
    if i == 0 or j == 0:
        return [a[i][j]]
    return [a[i][j]] + calc_diag(a,i-1,j-1)


def get_diag1(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert die Diagonale von rechts in der das Element a[i][j] liegt.
    '''
    (i, j) = prep_diag(a,i,j)
    return calc_diag(a,i,j)


def get_diag2(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl j.
        Liefert diag2 in der das Element a[i][j] liegt.
    '''
    return get_diag1(flip(a),i,len(a[i])-1-j) #j muss sozusagen um die i-Achse gespiegelt werden, um damit richtig weiterrechnen zu können.


def get_all_lines(a,i,j):
    '''Erwartet ein zweidimensionales Array a, eine Zahl i und eine Zahl.
        Liefert alle relevanten Linien.
    '''
    return [get_column(a,j), get_row(a,i), get_diag1(a,i,j), get_diag2(a,i,j)]


def get_insertionpoint(l,j):
    '''Erwartet eine Liste l und eine Zahl j.
        Liefert das hinterste Leerzeichen in der Liste. 
        Liefert -1, wenn kein Leerzeichen existiert.
    '''
    if j < 0 :
        return -1
    if l[j] == ' ':
        return j
    return get_insertionpoint(l,j-1)


def get_manipulation_point(a,c):
    '''Erwartet ein zweidimensionales Array a und holt über den Input eine Zahl j und einen Charakter c.
        Bestimmt die erste freie Zeile in der Spalte j des Arrays a.
        Liefert das Zahlentupel (i, j).
        [TODO] return statement aus der Exception
        [TODO] input evtl. auslagern => Funktion durch simulierte Eingabe testbar
    '''
    try:
        j = int(input("Spieler " + c + " gib bitte eine Zahl zwischen 0 und 6 an, um deine Spalte auszuwählen: "))
    except ValueError:
        print("Eingabe Falsch! Versuchs nochmal.")
        return get_manipulation_point(a,c)
    if j > len(a) or j < 0: 
        print("Eingabe Falsch! Versuchs nochmal.")
        return get_manipulation_point(a,c)
    i = get_insertionpoint(get_column(a,j),len(get_column(a,j))-1)
    if i == -1:
        print("Zeile voll, versuchs nochmal.")
        return get_manipulation_point(a,c)
    return i, j

