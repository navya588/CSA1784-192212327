board = [' '] * 9

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-----')

def is_victory(icon):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == icon
               for a, b, c in wins)

for turn in range(9):
    icon = 'X' if turn % 2 == 0 else 'O'

    print_board()

    pos = int(input(f"Player {icon}'s turn (1-9): ")) - 1

    if 0 <= pos < 9 and board[pos] == ' ':
        board[pos] = icon

        if is_victory(icon):
            print_board()
            print(f"{icon} wins!")
            break
    else:
        print("Position taken or invalid!")
else:
    print_board()
    print("Draw!")
