def board_to_string(b):
    '''Erwartet ein zweidimensionales Array b.
        Liefert einen String der das Array als Spielfeld darstellt.
    '''
    n = "\n" + "".join(["--+-" for i in range(len(b[0])-1)]) + "-\n"
    return n.join([" | ".join(line) for line in b])

