def check_winner(game_board_list):
    # player 1 is represented by 1
    # player 2 is represented by 2
    # if the section of the board was not claimed by anyone, it is represented as a 0
    if game_board_list[0][0] == game_board_list[1][1] == game_board_list[2][2] != 0:  # diagonal top left to bottom right
        return f'The winner is player {game_board_list[0][0]}!'
    elif game_board_list[0][2] == game_board_list[1][1] == game_board_list[2][0] != 0:  # diagonal top right to bottom left
        return f'The winner is player {game_board_list[0][2]}!'
    elif game_board_list[0][0] == game_board_list[1][0] == game_board_list[2][0] != 0:  # very left column
        return f'The winner is player {game_board_list[0][0]}!'
    elif game_board_list[0][1] == game_board_list[1][1] == game_board_list[2][1] != 0:  # middle column
        return f'The winner is player {game_board_list[0][1]}!'
    elif game_board_list[0][2] == game_board_list[1][2] == game_board_list[2][2] != 0:  # very right column
        return f'The winner is player {game_board_list[0][2]}!'
    elif game_board_list[0][0] == game_board_list[0][1] == game_board_list[0][2] != 0:  # top row
        return f'The winner is player {game_board_list[0][0]}!'
    elif game_board_list[1][0] == game_board_list[1][1] == game_board_list[1][2] != 0:  # middle row
        return f'The winner is player {game_board_list[0][0]}!'
    elif game_board_list[2][0] == game_board_list[2][1] == game_board_list[2][2] != 0:  # bottom row
        return f'The winner is player {game_board_list[0][0]}!'
    else:
        for i in range(3):
            for j in range(3):
                if game_board_list[i][j] == 0:
                    return False
        return 'The game is a tie'


def convert(num):
    first_digit = 0
    second_digit = 0
    if 0 < num <= 3:
        first_digit = 0
        second_digit = num - 1
    elif 3 < num <= 6:
        first_digit = 1
        second_digit = num - 4
    elif 6 < num <= 9:
        first_digit = 2
        second_digit = num - 7
    return first_digit, second_digit


def xOrO(num):
    if num == 1:
        return 'X'
    elif num == 2:
        return 'O'
    else:
        return None


game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


def printboard():
    print(' ---' * 3)
    print(f'| {xOrO(game_board[0][0]) or "1"} | {xOrO(game_board[0][1]) or "2"} | {xOrO(game_board[0][2]) or "3"} |')
    print(' ---' * 3)
    print(f'| {xOrO(game_board[1][0]) or "4"} | {xOrO(game_board[1][1]) or "5"} | {xOrO(game_board[1][2]) or "6"} |')
    print(' ---' * 3)
    print(f'| {xOrO(game_board[2][0]) or "7"} | {xOrO(game_board[2][1]) or "8"} | {xOrO(game_board[2][2]) or "9"} |')
    print(' ---' * 3)


def playerone():
    try:
        player1 = int(input('Player 1 (X) where would you like to place on the board? (type a number 1-9, 1 for top left and goes left to right) '))
        if player1 > 9 or player1 < 1:
            print('Please enter an integer 1-9 (1 for top left and goes left to right) ')
            playerone()
        else:
            one, two = convert(player1)
            if game_board[one][two] == 0:
                game_board[one][two] = 1
                printboard()
            else:
                print('That spot is already taken!')
                printboard()
                playerone()
    except ValueError:
        print('Please enter an integer')
        playerone()


def playertwo():
    try:
        player2 = int(input('Player 2 (O) where would you like to place on the board? (type a number 1-9, 1 for top left and goes left to right) '))
        if player2 > 9 or player2 < 1:
            print('Please enter an integer 1-9 (1 for top left and goes left to right) ')
            playertwo()
        else:
            one, two = convert(player2)
            if game_board[one][two] == 0:
                game_board[one][two] = 2
                printboard()
            else:
                print('That spot is already taken!')
                printboard()
                playertwo()
    except ValueError:
        print('Please enter an integer')
        playertwo()


printboard()

while check_winner(game_board) is False:
    playerone()
    if check_winner(game_board):
        break
    playertwo()

print(check_winner(game_board))
