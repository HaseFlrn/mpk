def board_to_string(board: list):
    '''Erwartet ein zweidimensionales Array board.
        Liefert einen String der das Array als Spielfeld darstellt.
    '''
    n = "\n" + "".join(["--+-" for i in range(len(board[0])-1)]) + "-\n"
    return n.join([" | ".join(line) for line in board])

