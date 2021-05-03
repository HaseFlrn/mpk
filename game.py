from get_func import get_manipulation_point 
from game_logic import player_wins, board_full
from helper_func import show_board


def generate_board(n: int,m: int):
    '''Erwartet eine Zahl n und eine Zahl m.
        Liefert ein zweidimensionales Array mit Ausprägung n Zeilen auf m Spalten.
    '''
    return [[" " for i in range(m)] for j in range(n)]


def manipulate(board: list, player: str, player_input):
    '''Erwartet ein zweidimensionales Array board und einen Charakter player.
        Liefert das an Stelle board[row][col] mit player manipulierte Array board.
    '''
    new_board = board.copy() 
    row,col = get_manipulation_point(board,player,player_input)
    new_board[row][col] = player
    return new_board, row, col 


def game_round(board: list, player: str, player_input):
    '''Erwartet ein zweidimensionales Array board, einen Charakter player und eine Inputfunktion player_input.
        Spielt eine Runde des Spiels durch.
        Liefert 0, wenn Spieler X gewonnen hat.
        Liefert 1, wenn Spieler O gewonnen hat.
        Liefert 2, wenn noch keiner gewonnen hat.
        Liefert -1 bei einem Unentschieden.
    '''
    show_board(board)
    print(player, "ist am Zug")
    board, row, col = manipulate(board, player, player_input)
    if player_wins(board, row, col, player):
        show_board(board)
        return (0, 'X') if player == 'X' else (1, 'O')
    if board_full(board):
        show_board(board)
        return -1, ''
    return (2, 'X') if player == 'O' else (2, 'O')
