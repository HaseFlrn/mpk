from helper_func import board_to_string, line_to_string, any_of

def test_line_to_string():
    l = ['X','X','X']
    assert(line_to_string(l) == "XXX")

def even(x):
  '''Liefert True, falls x eine gerade Zahl ist.'''
  return x % 2 == 0


def test_any_of():
    a1 = [1,3,5,7,9]
    a2 = [1,2,3,4,5]
    assert(any_of(a1,even) == False)
    assert(any_of(a2,even) == True)


def test_board_to_string():
    b = [["1","2","3"],["4","5","6"],["7","8","9"]]
    assert(board_to_string(b) == "1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9")

def test_helper_functions():
    test_line_to_string()
    test_any_of()
    test_board_to_string()
  

if __name__ == "__main__":
    test_helper_functions()
  