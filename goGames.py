while True:
    print("|   /)   |    |-------    |            (--------)        (--------)        | )       (|     |--------")
    print("|  /  )  |    |           |           (                (            )      |  )     ( |     |")
    print("|  /  )  |    |           |          (                (              )     |  )     ( |     |")
    print("| /    ) |    |-----      |          (                (              )     |   )   (  |     |------")
    print("| /    ) |    |           |           (                (            )      |   )   (  |     |")
    print("|/      )|    |           |            (                (          )       |    ) (   |     | ")
    print("|/      )|    |_______    |________     (________)       (________)        |    )|(    |     |_________")
    print("")
    print("                       --------------          (--------)      ")
    print("                              |               (           )    ")
    print("                              |              (             )   ")
    print("                              |              (             )   ")
    print("                              |               (           )    ")
    print("                              |                (         )     ")
    print("                              |                 (_______)      ")
    print("                                                               ")
    print("|----------)    (-------)                 |----------)       ()     | )       ( |   |-------    ------   ")
    print("|          )   (         )                |          )      (  )    | )       ( |   |         |         ")
    print("|             (           )               |                (    )   |  )     (  |   |         |         ")
    print("|            (             )              |                (    )   |   )   (   |   |         |         ")
    print("|            (             )              |                (----)   |   )   (   |   |---      -------     ")
    print("|    ______   (            )              |    ------      (    )   |    ) (    |   |                |    ")
    print("|   |      )   (          )               |    |     )    (      )  |    ) (    |   |                |    ")
    print("|__________)    (________)                |__________)    (      )  |    )|(    |   |______   ________   ")
    print("                                                 ")
    print("                                      Created by Scott Fennell.")
    import os
    os.system("say 'Welcome to Go Games!'")

    beg_start = input("To start type 'S' or 'E' to Exit: ")
    if beg_start == 'S':
        while True:
            print("Games-")
            print("1.) Tic Tac Toe")
            print("2.) Hangman")
            print("3.) Rock, Paper, Scissors")
            print("E.) Exit")
            game_selection = input("Select what game you want to play! {Ex. 1}: ")
            if game_selection == '1':

                board = [' ' for x in range(10)]


                def insert_letter(letter, pos):
                    board[pos] = letter


                def space_is_free(pos):
                    return board[pos] == ' '


                def print_board(board):
                    print(' [1] | [2] | [3] ')
                    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
                    print('     |     |')
                    print('-----------------')
                    print(' [4] | [5] | [6] ')
                    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
                    print('     |     |')
                    print('-----------------')
                    print(' [7] | [8] | [9] ')
                    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
                    print('     |     |')


                def is_winner(bo, le):
                    return (bo[7] == le and bo[8] == le and bo[9] == le) or (
                                bo[4] == le and bo[5] == le and bo[6] == le) or (
                                   bo[1] == le and bo[2] == le and bo[3] == le) or (
                                       bo[1] == le and bo[4] == le and bo[7] == le) or (
                                   bo[2] == le and bo[5] == le and bo[8] == le) or (
                                   bo[3] == le and bo[6] == le and bo[9] == le) or (
                                   bo[1] == le and bo[5] == le and bo[9] == le) or (
                                       bo[3] == le and bo[5] == le and bo[7] == le)


                def player_move():
                    run = True
                    while run:
                        move = input('Please select a position to place an \'X\' (1-9): ')
                        try:
                            move = int(move)
                            if move > 0 and move < 10:
                                if space_is_free(move):
                                    run = False
                                    insert_letter('X', move)
                                else:
                                    print('Sorry, this space is occupied!')
                            else:
                                print('Please type a number within the range!')
                        except:
                            print('Please type a number!')


                def minimax():
                    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
                    move = 0

                    for let in ['O', 'X']:
                        for i in possible_moves:
                            board_copy = board[:]
                            board_copy[i] = let
                            if is_winner(board_copy, let):
                                move = i
                                return move

                    corners_open = []
                    for i in possible_moves:
                        if i in [1, 3, 7, 9]:
                            corners_open.append(i)

                    if len(corners_open) > 0:
                        move = select_random(corners_open)
                        return move

                    if 5 in possible_moves:
                        move = 5
                        return move

                    edges_open = []
                    for i in possible_moves:
                        if i in [2, 4, 6, 8]:
                            edges_open.append(i)

                    if len(edges_open) > 0:
                        move = select_random(edges_open)

                    return move


                def select_random(li):
                    import random
                    ln = len(li)
                    r = random.randrange(0, ln)
                    return li[r]


                def is_board_full(board):
                    if board.count(' ') > 1:
                        return False
                    else:
                        return True


                def main():
                    print('Welcome to Tic Tac Toe!')
                    print_board(board)

                    while not (is_board_full(board)):
                        if not (is_winner(board, 'O')):
                            player_move()
                            print_board(board)
                        else:
                            print('Sorry, O\'s won this time!')
                            break

                        if not (is_winner(board, 'X')):
                            move = minimax()
                            if move == 0:
                                print('Tie Game!')
                            else:
                                insert_letter('O', move)
                                print('Computer placed an \'O\' in position', move, ':')
                                print_board(board)
                        else:
                            print('X\'s won this time! Good Job!')
                            break

                    if is_board_full(board):
                        print('Tie Game!')


                while True:
                    answer = input('Do you want to play/ play again? (Y/N): ')
                    if answer == 'Y':
                        board = [' ' for x in range(10)]
                        print('-----------------------------------')
                        main()
                    elif answer == 'N':
                        break
                    else:
                        print("Sorry, I did not understand")
                        continue
            elif game_selection == '2':
                while True:
                    print("Welcome to hangman!")
                    import time
                    print(""
                          "")
                    time.sleep(1)
                    print("Start Guessing...")
                    time.sleep(0.5)
                    words = ['rainbow', 'cow', 'horse', 'lion', 'book', 'science', 'heifer', 'knife', 'sword',
                             'dangerous', 'christmas', 'beach', 'dinosaur', 'golf', 'wax', 'melt', 'speaker'
                             'truck', 'jeep', 'study', 'camper', 'state', 'apple', 'road', 'information', 'artificial'
                             'website', 'hangman', 'secret', 'code', 'python', 'halloween', 'desktop', 'software',
                             'hardware', 'virtual', 'machine']
                    import random
                    word = random.choice(words)
                    guesses = ''
                    turn = 15
                    while turn > 0:
                        failed = 0
                        for char in word:
                            if char in guesses:
                                print(char)
                            else:
                                print("_")
                                failed += 1
                        if failed == 0:
                            print("You won!")
                            break
                        guess = input("Guess a character: ")
                        guesses += guess
                        if guess not in word:
                            turn -= 1
                            print("Wrong!")
                            print("You have", + turn, 'more guesses')
                            if turn == 0:
                                print("You lose!")
                    cont_hang = input("Another game? {Y/N}: ")
                    if cont_hang == "Y":
                        continue
                    else:
                        print("Thank you for playing! Bye!")
                        break
            elif game_selection == '3':
                while True:
                    from random import randint
                    import time
                    import os

                    moves = ["Rock", "Paper", "Scissors"]
                    computer_move = moves[randint(0, 2)]
                    intro = str("Welcome to Rock! Paper! Scissors! Shoot!")
                    spoke = "say 'Rock, paper, Scissors Shoot!'"
                    desc = str("Rules of the game-\n"
                               "1.) Rock smashes scissors\n"
                               "2.) Scissors cuts paper\n"
                               "3.) Paper covers rock\n"
                               "4.) Best out of three games win\n"
                               "    or keep playing!")
                    how = str("To play select 'R' for rock, 'S' for scissors, and 'P' for paper.")
                    print(intro)
                    print(
                        " "
                    )
                    os.system(spoke)
                    print(desc)
                    print(
                        " "
                    )
                    time.sleep(1.5)
                    print(how)
                    print(
                        " "
                    )
                    time.sleep(1.5)
                    player_start = input("When ready type 'S' to start or 'E' to exit- ")
                    print(
                        " "
                    )
                    if player_start == 'S':
                        player = False
                        computer_score = 0
                        player_score = 0
                        while not player:
                            print(
                                " "
                            )
                            player_move = input("Player move: ")
                            if player_move == computer_move:
                                print("Computer move: " + computer_move)
                                print(
                                    " "
                                )
                                print("Tie! Tie! Tie!")
                            elif player_move == 'R':
                                if computer_move == "Scissors":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Rock smashes scissors!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You Lose! Paper covers rock!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            elif player_move == "S":
                                if computer_move == "Paper":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Scissors cutes paper!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You lose! Rock smashes scissors!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            elif player_move == "P":
                                if computer_move == "Rock":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Paper covers rock!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You lose! Scissors cuts paper!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            else:
                                print("Invalid move, please try again")
                                continue
                            time.sleep(0.5)
                            print(
                                " "
                            )
                            player_move = input("Player move: ")
                            if player_move == computer_move:
                                print("Computer move: " + computer_move)
                                print(
                                    " "
                                )
                                print("Tie! Tie! Tie!")
                            elif player_move == 'R':
                                if computer_move == "Scissors":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Rock smashes scissors!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You Lose! Paper covers rock!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            elif player_move == "S":
                                if computer_move == "Paper":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Scissors cutes paper!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You lose! Rock smashes scissors!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            elif player_move == "P":
                                if computer_move == "Rock":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Paper covers rock!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You lose! Scissors cuts paper!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            else:
                                print("Invalid move, please try again")
                                continue
                            time.sleep(0.5)
                            print(
                                " "
                            )
                            player_move = input("Player move: ")
                            if player_move == computer_move:
                                print("Computer move- " + computer_move)
                                print(
                                    " "
                                )
                                print("Tie! Tie! Tie!")
                            elif player_move == 'R':
                                if computer_move == "Scissors":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Rock smashes scissors!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You Lose! Paper covers rock!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            elif player_move == "S":
                                if computer_move == "Paper":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Scissors cutes paper!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You lose! Rock smashes scissors!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            elif player_move == "P":
                                if computer_move == "Rock":
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You win! Paper covers rock!")
                                    os.system("say 'You Win!'")
                                    player_score = player_score + 1
                                else:
                                    print("Computer move: " + computer_move)
                                    print(
                                        " "
                                    )
                                    print("You lose! Scissors cuts paper!")
                                    os.system("say 'You lose!'")
                                    computer_score = computer_score + 1
                            else:
                                print("Invalid move, please try again!")
                                continue
                            time.sleep(1)
                            print(
                                ""
                            )
                            print("Player score-")
                            print(player_score)
                            print("Computer score-")
                            print(computer_score)
                            if player_score > computer_score:
                                print("You won the game! Player Wins!")
                                os.system("say 'You won!'")
                            if computer_score > player_score:
                                print("You lost! Computer wins!")
                                os.system("say 'You lost!'")
                            if player_score == computer_score:
                                print("Tie game! Tie game!")
                                os.system("say 'Tie game!'")
                            time.sleep(0.5)
                            print(
                                " "
                            )
                            cont_game = input("Play again? [Y/N]- ")
                            if cont_game == "Y":
                                continue
                            elif cont_game == "N":
                                break
                            else:
                                print("Invalid request, please try again!")
                                continue

                    elif player_start == 'E':
                        break
                    else:
                        print("Invalid request! Need to be in uppercase format.")
                    continue
            elif game_selection == 'E':
                break
            else:
                print("Invalid Option!")
                continue
    elif beg_start == 'E':
        print("Thank you for playing! Bye!")
        break
    else:
        print("Invalid Login")
        continue
