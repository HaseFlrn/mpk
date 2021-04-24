def human_input():
    '''Liefert einen Input aus der Konsole.'''
    j = input("Gib bitte eine Zahl zwischen 0 und 6 an, um deine Spalte auszuwählen: ")
    return j

def validate_input(a,j):
    '''Erwartet ein Array a und eine Zahl j.
        Liefert True, wenn die Stelle j in a existiert.
        Liefert False, wenn die Stelle j in a nicht existiert.
    '''
    return False if j > len(a) or j < 0 else True

def convertable_to_int(player_input: str):
    '''Erwartet einen String player_input.
        Überprüft, ob player_input in int konvertiert werden kann.
    '''
    check = False
    try:
        int(player_input)
        check = True
    except ValueError:
        print("Eingabe Fehlerhaft.")
    return check
