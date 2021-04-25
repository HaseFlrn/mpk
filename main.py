from game import generate_board
from game import game_round
from player_input import human_input, stupid_cpu

def gameloop(player_x_input = human_input, player_o_input = human_input):
    '''Startet das Spiel und läuft so lange, bis ein Spieler gewonnen hat,
        oder es unentschieden steht.
        Optional können Inputfunktionen mitgegeben werden.
    '''
    board = generate_board(6,7)
    player = 'X'
    result = 2
    while result == 2:        
        if player == 'O':
            result, player = game_round(board, player, player_o_input)
        else:
            result, player = game_round(board, player, player_x_input)
        if result == 0:
            print("X hat gewonnen")
            break
        if result == 1:
            print("O hat gewonnen")
            break
        if result == -1:
            print("unentschieden")
            break
        

if __name__ == "__main__":
    gamemode = {'1': (human_input,human_input) , '2': (human_input,stupid_cpu)}
    print("Wähle einen Spielmodus.")
    user_selection = input("1: 1v1 oder 2: 1vCPU")
    player_x_input,player_o_input = gamemode[user_selection] 
    gameloop(player_x_input,player_o_input)