# Pirple Course
# Tic Tac Toe - Part A

# | | 0
#-----1
# | | 2
#-----3
# | | 4
#01234

def drawField(field):
    for row in range(5): #0,1,2,3,4
                         #0,.,1,.,2
        if row%2 == 0: #if row is even
            practical_row = int(row/2)
            #print writing lines
            for column in range(5): #0,1,2,3,4
                                    #0,.,1,.,2
                if column%2 == 0:
                    practical_column = int(column/2)
                    if column != 4:
                        print(field[practical_column][practical_row],end = "")
                    else:
                        print(field[practical_column][practical_row])
                else:
                    print("|",end = "") # end = "" removes the new line, we stay on the same line

        else:
            print("-----")

player = 1
current_field = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]] #3 lists within the list --> columns + rows (matix)
drawField(current_field)
while(True): #True == True
    print("Player's turn:",player)
    move_row  = int(input("Please enter the row: "))
    move_column = int(input("Please enter the column: "))
    if player == 1:
        #make move for player 1
        if current_field[move_column][move_row] == " ":
            current_field[move_column][move_row] = "X"
            player = 2
    else:
        #make move for player 2
        if current_field[move_column][move_row] == " ":
            current_field[move_column][move_row] = "O"
            player = 1
    drawField(current_field)
