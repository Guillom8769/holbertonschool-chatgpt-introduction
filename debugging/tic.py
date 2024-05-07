#!/usr/bin/python3

def print_board(board):
    """
    Imprime le plateau de jeu dans la console.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné la partie.

    Returns:
        str: Le symbole du gagnant ("X" ou "O"), ou None si pas de gagnant.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """
    Vérifie si toutes les cases du plateau sont occupées.

    Returns:
        bool: True si toutes les cases sont pleines, False sinon.
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_input(player):
    """
    Demande les coordonnées d'une case et assure la validité de l'entrée.

    Parameters:
        player (str): Le joueur actuel ("X" ou "O").

    Returns:
        tuple: Coordonnées (row, col) saisies par le joueur.
    """
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Coordinates must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    """
    Fonction principale pour jouer au tic-tac-toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        row, col = get_input(player)
        if board[row][col] == " ":
            board[row][col] = player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()
