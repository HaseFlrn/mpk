from game_logic import contains_combo, player_wins, player_o_wins, player_x_wins, board_full

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

def test_game_logic():
    test_contains_combo()
    test_player_wins()
    test_player_x_wins()
    test_player_o_wins()
    test_board_full()

if __name__ == "__main__":
    test_game_logic()