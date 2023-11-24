import os, time, random

def print_board(boardpositions):
    """ this function takes a 3x3 
    2-dimensional list as argument 
    and prints it on the screen.
    ex: [["","",""],["","",""],["","",""]] 
    """


    # remove empty entries with spaces for clear formatting
    # for i in range(3):
    #     boardtodraw[i]=list(map(lambda x: x.replace("", " "), boardtodraw[i]))

    # initialize the empty board
    board_string=""

    # add the board positions to it
    board_print=[[boardpositions[0][0],"|",boardpositions[0][1],"|",boardpositions[0][2]], 
                 ["-","+","-","+","-"],
                 [boardpositions[1][0],"|",boardpositions[1][1],"|",boardpositions[1][2]], 
                 ["-","+","-","+","-"],
                 [boardpositions[2][0],"|",boardpositions[2][1],"|",boardpositions[2][2]] ]
    
    # turn the board into a string so we can print it on the screen
    for i in range(5):
        for j in range(5):
            board_string+=''.join(board_print[i][j])
        board_string+="\n"
    # print(board_string)

    # return the result
    return board_string

def test_board(boardpositions):
    for i in range(3):
        if boardpositions[0][i] == boardpositions[1][i] == boardpositions[2][i] != "":
            # print("Vertical win")
            return("Player {} won!".format(boardpositions[0][i]))
        
    for i in range(3):
        if boardpositions[i][0] == boardpositions[i][1] == boardpositions[i][2] != "":
            # print("Horizontal win")
            return ("Player {} won!".format(boardpositions[i][0]))
        

    if (boardpositions[0][0] == boardpositions[1][1] == boardpositions[2][2] != "") or \
       (boardpositions[0][2] == boardpositions[1][1] == boardpositions[2][0] != ""):
        # print("Diagonal Win")
        return ("Player {} won!".format(boardpositions[1][1]))
    
    return ("No winner yet")
    
def board_full(boardpositions):
    # Check if the board is complete
    for i in range(3):
        for j in range(3):
            if boardpositions[i][j] == "":
                return False            

    return True

if __name__ == '__main__':
    os.system ('clear')
    print ("Starting Tic Tac Toe game...")
    
    players = ["X","O"]
    board = [["","",""],["","",""],["","",""]] 
    winner = False
    startPlayer = random.randint(0,1)
    print("Start player will be: ",players[startPlayer])
    time.sleep(0.5)

    while (board_full(board) == False) and (winner == False):
        os.system ('clear')
        print(print_board(board))
        time.sleep(0.5)
        i = random.randint(0,2)
        j = random.randint(0,2)
        while board[i][j] != "":
            i = random.randint(0,2)
            j = random.randint(0,2)
        board[i][j] = players[startPlayer%2]
        startPlayer += 1
        if test_board(board) != "No winner yet":
            winner = True

    os.system ('clear')
    print(print_board(board))
    result = test_board(board)
 
    if board_full(board) and result == "No winner yet":
        print("Draw, no winner....")
    else:
        print(result)

    print("Thank you for playing the game.")





