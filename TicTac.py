def sum(sum_to_list):
    total = 0
    for i in sum_to_list:
        total += i
    print(total)
    return total

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
    print(board_string)

    # return the result
    return board_string

print_board([["","",""],["","",""],["","",""]])

