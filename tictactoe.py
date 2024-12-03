height = 3
width = 3

def print_board(board):
    for row in board:
        print(" ---" * width)
        print("| " + " | ".join(row) + " |")
    print(" ---" * width)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(width):
        if all(board[row][col] == player for row in range(height)):
            return True
    if all(board[i][i] == player for i in range(width)):
        return True
    if all(board[i][width - 1 - i] == player for i in range(width)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(width)] for _ in range(height)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Joueur {current_player}, entrez la ligne (1, 2, 3): ")) - 1
            col = int(input(f"Joueur {current_player}, entrez la colonne (1, 2, 3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Entrée invalide. Veuillez entrer un nombre entre 1 et 3.")
                continue
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 3.")
            continue
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("La case est déjà prise.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Joueur {current_player} a gagné!")
            break
        
        if is_full(board):
            print_board(board)
            print("Egalité!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
