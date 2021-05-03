def any_of(a: list, f):
    '''Erwartet ein Array a und eine Funktion f.
        Liefert True, wenn f(el) == True für irgendein el in a gilt.
    '''
    return any(map(f,a))


def board_to_string(board: list):
    '''Erwartet ein zweidimensionales Array board.
        Liefert einen String der das Array als Spielfeld in der Kosole darstellbar macht.
    '''
    n = "\n" + "".join(["--+-" for i in range(len(board[0])-1)]) + "-\n"
    return n.join([" | ".join(line) for line in board])


def line_to_string(line: list):
    '''Erwartet eine Liste aus Strings oder Charaktern.
        Liefert einen zusammengesetzten String der Elemente aus l.  
    '''
    return "".join(line)


def show_board(board: list):
    '''Erwartet ein zweidimensionales Array board.
        Gibt board als Spielfeld in der Konsole aus.
    '''
    print(board_to_string(board))