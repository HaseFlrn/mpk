from test_game_logic import test_game_logic
from test_get_func import test_get_functions
from test_helper_func import test_helper_functions

def test_all():
    test_game_logic()
    test_get_functions()
    test_helper_functions()

if __name__ == "__main__":
    test_all()