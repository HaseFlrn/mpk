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


def test_get_row():
    a1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert(get_row(a1,0) == [1,2,3])

def test_get_column():
    a1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert(get_column(a1,0) == [1,4,7])

def test_flip_row():
    a1 = [['X','X','X'],['X','X','O'],['X','O',' ']]
    assert(flip_row(a1,len(a1)-1) == [' ','O','X'])

def test_flip():
    a1 = [['X','X','X'],['X','X','O'],['X','O',' ']]
    assert(flip(a1) == [['X','X','X'],['O','X','X'],[' ','O','X']])
    a2 = [['O','O','X'],['X','O','O'],['X','O',' ']]
    assert(flip(a2) == [['X','O','O'],['O','O','X'],[' ','O','X']])

def test_prep_diag():
    a1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert(prep_diag(a1,1,1) == (2,2))
    assert(prep_diag(a1,0,1) == (1,2))
    assert(prep_diag(a1,1,0) == (2,1))
    a2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(prep_diag(a2,1,1) == (3,3))
    assert(prep_diag(a2,0,1) == (2,3))
    assert(prep_diag(a2,1,0) == (3,2))

def test_calc_diag():
    a1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert(calc_diag(a1,2,2) == [9,5,1])
    assert(calc_diag(a1,2,1) == [8,4])
    a2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(calc_diag(a2,2,2) == [11,6,1])

def test_get_diag1():
    a1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert(get_diag1(a1,2,2) == [9,5,1])
    assert(get_diag1(a1,2,1) == [8,4])
    a2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(get_diag1(a2,2,2) == [16,11,6,1]) 
    a3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    assert(get_diag1(a3,2,2) == [11,6,1])

def test_get_diag2():
    a1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(get_diag2(a1,3,0) == [13,10,7,4]) 

def test_get_all_lines():
    a1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert(get_all_lines(a1,0,0) == [[1, 5, 9, 13], [1, 2, 3, 4], [16, 11, 6, 1], [1]])

def test_get_insertionpoint():
    l1 = [' ','X','X']
    assert(get_insertionpoint(l1,len(l1)-1) == 0)
    l2 = ['X','X','X']
    assert(get_insertionpoint(l2,len(l2)-1) == -1)

def test_get_manipulation_point():
    a1 = [['X','X',' '],['X','X','X'],['X','O','O']]
    print("Bitte 2 eingeben, um das korrekte Ergebnis zu rehalten, sonst dauerhafte wiederholung: ")
    assert(get_manipulation_point(a1,'X') == (0, 2))
    a2 = [[' ','X',' '],['X','X','X'],['X','O','O']]
    print("Bitte 0 oder 2 eingeben, um das korrekte Ergebnis zu rehalten, sonst dauerhafte wiederholung: ")
    assert(get_manipulation_point(a2,'X') == (0, 2) or get_manipulation_point(a2,'X') == (0, 0))

if __name__ == "__main__":
    test_get_row()
    test_get_column()
    test_flip_row()
    test_flip()
    test_prep_diag()
    test_calc_diag()
    test_get_diag1()
    test_get_diag2()
    test_get_all_lines()
    test_get_insertionpoint()
    test_get_manipulation_point()