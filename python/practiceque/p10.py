#Tic-Tac-Toe program
# Create the board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Function to display board
def display_board():
    for row in board:
        print(row[0] + " | " + row[1] + " | " + row[2])
        print("---------")

# Function to check win
def check_win(player):

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Function to check draw
def check_draw():
    for row in board:
        if " " in row:
            return False
    return True


# Start game
current_player = "X"

while True:

    display_board()

    print("Player", current_player)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player     #assign value of the part RC for the  current player
    else:
        print("Position already taken")
        continue

    # Check win
    if check_win(current_player):
        display_board()
        print(current_player, "wins!")
        break

    # Check draw
    if check_draw():
        display_board()
        print("Game Draw!")
        break

    # Switch player
    if current_player == "X":    #switch the player
        current_player = "O"
    else:
        current_player = "X"



