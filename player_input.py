from random import randint
from time import sleep

def human_input():
    '''Liefert einen Input aus der Konsole.'''
    col = input("Gib bitte eine Zahl zwischen 0 und 6 an, um deine Spalte auszuwählen: ")
    return col

def validate_input(board: list,col: int):
    '''Erwartet ein Array board und eine Zahl col.
        Liefert True, wenn die Stelle col in board existiert.
        Liefert False, wenn die Stelle col in board nicht existiert.
    '''
    return False if col > len(board) or col < 0 else True

def convertable_to_int(player_input):
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

def stupid_cpu():
    '''Liefert eine random Zahl zwischen 0 und 6'''
    sleep(1)
    return randint(0, 6)

