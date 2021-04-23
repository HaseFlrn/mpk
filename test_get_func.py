from get_func import get_row, get_column, prep_diag, calc_diag, get_diag1, flip_row, flip, get_diag2, get_all_lines, get_insertionpoint, get_manipulation_point

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

# def test_get_manipulation_point():
#     a1 = [['X','X',' '],['X','X','X'],['X','O','O']]
#     print("Bitte 2 eingeben, um das korrekte Ergebnis zu rehalten, sonst dauerhafte wiederholung: ")
#     assert(get_manipulation_point(a1,'X') == (0, 2))
#     a2 = [[' ','X',' '],['X','X','X'],['X','O','O']]
#     print("Bitte 0 oder 2 eingeben, um das korrekte Ergebnis zu rehalten, sonst dauerhafte wiederholung: ")
#     assert(get_manipulation_point(a2,'X') == (0, 2) or get_manipulation_point(a2,'X') == (0, 0))

def test_get_functions():
    test_get_row()
    test_get_column()
    test_prep_diag()
    test_calc_diag()
    test_get_diag1()
    test_flip_row()
    test_flip()
    test_get_diag2()
    test_get_all_lines()
    test_get_insertionpoint()
#    test_get_manipulation_point()

if __name__ == "__main__":
    test_get_functions()