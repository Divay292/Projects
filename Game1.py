import random
def MakeBoard(board):
    print('   |   |    ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('----------------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |    ')

def PlayerChoice():
    choice = ' '
    while not (choice == 'X' or choice == '0'):
        choice = input("Pick X or 0").upper()

    if choice == 'X':
        return ['X', '0']
    else:
        return ['0', 'X']
def playAgain():
    print("Do you want to play again? Yes or No?")
    return input().lower().startswith('y')

def pickWinner(board, choice):
    return((board[9] == choice and board[7] == choice and board [8] == choice) or
           (board[1] == choice and board[2] == choice and board[3] == choice) or
           (board[6] == choice and board[4] == choice and board[5] == choice) or
           (board[1] == choice and board[4] == choice and board[7] == choice) or
           (board[2] == choice and board[5] == choice and board[8] == choice) or
           (board[3] == choice and board[6] == choice and board[9] == choice) or
           (board[9] == choice and board[5] == choice and board[1] == choice) or
           (board[3] == choice and board[5] == choice and board[7] == choice))

def makeMove(board, choice, move):
    board[move] = choice

def LegalMove(board, move):
    return board[move] == ' '

def BoardCopy(board):
    dupboard = []
    for i in board:
        dupboard.append(i)
    return dupboard
def PlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not LegalMove(board, int(move)):
        move = input("PICK YOUR MOVE (1-9)")
    return int(move)

def RandomMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if LegalMove(board, i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
def CompMove(board, Compchoice):
    if Compchoice == 'X':
        playerChoice = '0'
    else:
        playerChoice = 'X'
    for i in range (1, 10):
        copy = BoardCopy(board)
        if LegalMove(copy, i):
            makeMove(copy, Compchoice, i)
            if pickWinner(copy, playerChoice):
                return i
    for i in range(1,10):
        copy = BoardCopy(board)
        if LegalMove(copy, i):
           makeMove(copy, playerChoice, i)
           if pickWinner(copy, playerChoice):
              return i

    move = RandomMove(board, [1,3,7,9])
    if move is not None:
        return move
    if LegalMove(board, 5):
        return 5
    return RandomMove(board, [2,4,6,8])

def BoardFull(board):
    for i in range(1,10):
        if LegalMove(board, i):
            return False
    return True

print("Welcome to Tic Tac Toe!")
while True:
    theBoard = [' '] * 10
    playerChoice, Compchoice = PlayerChoice()
    if random.randint(0, 1) == 0:
        Play = 'Computer'
    else:
        Play = 'Player'
    print("The " + Play + "goes first.")
    gameunderway = True
    
    while gameunderway:
        if Play == 'Player':
            MakeBoard(theBoard)
            move = PlayerMove(theBoard)
            makeMove(theBoard, playerChoice, move)
            if pickWinner(theBoard, playerChoice):
                MakeBoard(theBoard)
                
            if pickWinner(theBoard, playerChoice):
                MakeBoard(theBoard)
                print("You win congratulations")
                gameunderway = False
            else:
                if BoardFull(theBoard):
                    MakeBoard(theBoard)
                    print('It is a draw')
                    break
                else:
                    Play = 'Computer'
        else:
            move = CompMove(theBoard, Compchoice)
            makeMove(theBoard, Compchoice, move)
            if pickWinner(theBoard, Compchoice):
               MakeBoard(theBoard)
               print('You lose. Please try again')
               gameunderway = False
            else:
                if BoardFull(theBoard):
                    MakeBoard(theBoard)
                    print("The game is tie")
                    break
                else:
                    Play = 'Player'
    if not playAgain():
        break
                