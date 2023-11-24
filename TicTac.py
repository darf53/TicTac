def print_board(boardpositions):
    """ this function takes a 3x3 
    2-dimensional list as argument 
    and prints it on the screen.
    ex: [["","",""],["","",""],["","",""]] 
    """

    # remove empty entries with spaces for clear formatting
    for i in range(3):
        boardpositions[i]=list(map(lambda x: x.replace("", " "), boardpositions[i]))

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

print_board([["","",""],["","",""],["","",""]])
print_board([["","","O"],["X","O",""],["O","","X"]])

