from game import manipulate, generate_board
from main import gameloop

def test_generate_board():
    assert(generate_board(2,3) == [[' ', ' ', ' '], [' ', ' ', ' ']])
    assert(not generate_board(2,3) == [[' ', ' '], [' ', ' '], [' ', ' ']])

def test_manipulate():
    a1 = [['X','X',' '],['X','X','X'],['X','O','O']]
    moves_x = [2]
    moves_x = iter(moves_x)
    assert(manipulate(a1,'X', lambda: next(moves_x)) == ([['X','X','X'],['X','X','X'],['X','O','O']], 0, 2))

def test_game_loop():
    moves_x = [1,2,3,1]
    moves_x = iter(moves_x)
    moves_o = [0,0,0,0]
    moves_o = iter(moves_o)

    gameloop(lambda : next(moves_x), lambda : next(moves_o))

def test_game():
    test_game_loop()
    test_generate_board()
    test_manipulate()

if __name__ == "__main__":
    test_game()