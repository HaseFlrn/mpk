from game import generate_board
from game import game_round

def gameloop():
    '''Startet das Spiel und läuft so lange, bis ein Spieler gewonnen hat,
        oder es unentschieden steht.
    '''
    b = generate_board(6,7)
    while True:
        r = game_round(b)
        if r == 0:
            print("X hat gewonnen")
            break
        if r == 1:
            print("O hat gewonnen")
            break
        if r == -1:
            print("unentschieden")
            break
        

if __name__ == "__main__":
    gameloop()