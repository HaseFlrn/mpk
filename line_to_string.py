def line_to_string(l):
    '''Erwartet eine Liste aus Strings oder Charaktern.
        Liefert einen concatinierten String der Elemente aus l.  
    '''
    return "".join(l)


def test_line_to_string():
    l = ['X','X','X']
    assert(line_to_string(l) == "XXX")

if __name__ == "__main__":
    test_line_to_string()
    