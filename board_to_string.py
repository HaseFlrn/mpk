def board_to_string(b):
    '''Erwartet ein zweidimensionales Array b.
        Liefert einen String der das Array als Spielfeld darstellt.
    '''
    n = "\n" + "".join(["--+-" for i in range(len(b[0])-1)]) + "-\n"
    return n.join([" | ".join(line) for line in b])


def test_board_to_string():
    b = [["1","2","3"],["4","5","6"],["7","8","9"]]
    assert(board_to_string(b) == "1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9")

if __name__ == "__main__":
    test_board_to_string()