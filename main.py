from game import generate_board
from game import game_round
from player_input import human_input

def gameloop(player_x_input = human_input, player_o_input = human_input):
    '''Startet das Spiel und läuft so lange, bis ein Spieler gewonnen hat,
        oder es unentschieden steht.
    '''
    b = generate_board(6,7)
    c = 'X'
    while True:
        print(c, "ist am Zug")
        if c == 'O':
            r, c = game_round(b, c, player_o_input)
        else:
            r, c = game_round(b, c, player_x_input)
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