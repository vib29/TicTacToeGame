import random 
def start():
        begin = input("Welcome to Tic Tac Toe! Are you ready to get started? \n A. Yes! \n B. No\n")
        if (begin == "A." or begin == "A"):
            name = input("Choose a name : ")
            print("It's " + name + "'s turn (X)")
            board()
        elif (begin == "B." or begin == "B"):
            print( "Alright bye \n")
        else:
            print("Invalid input. Please try again \n")
            start()
        
            
        
def board():
    global a
    a = [['_','_','_'], ['_','_','_'], ['_','_','_']]
    for i in range(len(a)):
        for j in range(len(a[i]) + 1):
            if (j == 3):
                print('\n')
            else:
                print(a[i][j], end=' ')
    player_turn()


def player_turn():
        global first_pos, second_pos, a
        first_pos = int(input("Enter the row : "))
        second_pos = int(input("Enter the column : "))
        for i in range(len(a)):
            for j in range(len(a[i])+1):
                a[first_pos][second_pos] = 'X'
                if (j == 3):
                    print('\n')
                else:
                    print(a[i][j], end=' ')
        computer_turn()

def computer_turn():
    global row, column
    print("It's the computer's turn now (O) \n")
    row = random.randint(0,2)
    column = random.randint(0,2)
    if(row == first_pos and column == second_pos):
        row = random.randint(0,2)
        column = random.randint(0,2)
    for i in range(len(a)):
        for j in range(len(a[i]) + 1):
            a[row][column] = 'O'
            if (j == 3):
                print('\n')
            else:
                print(a[i][j], end=' ')
    next_steps()

def next_steps():
    if(
                    a[0][0] == 'X' and a[0][1] == 'X' and a[0][2] == 'X' or
                    a[1][0] == 'X' and a[1][1] == 'X' and a[1][2] == 'X' or
                    a[2][0] == 'X' and a[2][1] == 'X' and a[2][2] == 'X' or
                    a[0][0] == 'X' and a[1][0] == 'X' and a[2][0] == 'X' or
                    a[0][1] == 'X' and a[1][1] == 'X' and a[2][1] == 'X' or
                    a[0][2] == 'X' and a[1][2] == 'X' and a[2][2] == 'X' or
                    a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X' or
                    a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X'):
        print("You win!")
    elif(
                    a[0][0] == 'O' and a[0][1] == 'O' and a[0][2] == 'O' or
                    a[1][0] == 'O' and a[1][1] == 'O' and a[1][2] == 'O' or
                    a[2][0] == 'O' and a[2][1] == 'O' and a[2][2] == 'O' or
                    a[0][0] == 'O' and a[1][0] == 'O' and a[2][0] == 'O' or
                    a[0][1] == 'O' and a[1][1] == 'O' and a[2][1] == 'O' or
                    a[0][2] == 'O' and a[1][2] == 'O' and a[2][2] == 'O' or
                    a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O' or
                    a[0][2] == 'O' and a[1][1] == 'O' and a[2][0] == 'O'):
        print("The computer wins :/")
    else:
        print(player_turn())
            
start()


