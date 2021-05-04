#TicTacToe / Naughts and Crosses AI, play Tic Tac Toe against an Artificial Intelligence
#3/05/21 - 4/05/2021
while True:
    row1 = ["-","-","-"]
    row2 = ["-","-","-"]
    row3 = ["-","-","-"]
    print("I am going to go first, I am X, you are O")
    row3[0] = "x"
    print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
    print("input type: c1 r2, would put an O on collumn 1, row 2")
    over = "null"
    gameIteration = 0
    while over=="null":
        #Check if game is over
        #AI won?
        #diagonal
        if row1[0] == "x" and row2[1] == "x" and row3[2] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        if row3[0] == "x" and row2[1] == "x" and row1[2] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        #horizontal
        if row1[0] == "x" and row1[1] == "x" and row1[2] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        if row2[0] == "x" and row2[1] == "x" and row2[2] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        if row3[0] == "x" and row3[1] == "x" and row3[2] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        #vertical
        if row1[0] == "x" and row2[0] == "x" and row3[0] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        if row1[1] == "x" and row2[1] == "x" and row3[1] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        if row1[2] == "x" and row2[2] == "x" and row3[2] == "x":
            print ("Game Over, win by x (AI)")
            over = "true"
            break
        #Player won?
        if row1[0] == "o" and row2[1] == "o" and row3[2] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        if row3[0] == "o" and row2[1] == "o" and row1[2] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        if row1[0] == "o" and row1[1] == "x" and row1[2] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        if row2[0] == "o" and row2[1] == "o" and row2[2] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        if row3[0] == "o" and row3[1] == "o" and row3[2] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        if row1[1] == "o" and row2[1] == "o" and row3[1] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        if row1[2] == "o" and row2[2] == "o" and row3[2] == "o":
            print ("Game Over, win by O (You)")
            over = "true"
            break
        
        #Your move
        move = "null"
        while "c" != move[0] and "r" != move[3] and len(move) != 6:
            move = input("input your move: ")
            try:
                if move[4] == "1": 
                    if row1[int(move[1])-1] == "x" or row1[int(move[1])-1] == "o":
                        print(f"{move} is already occupied by {row1[int(move[1])-1]}")
                        move = "null"
                if move[4] == "2": 
                    if row2[int(move[1]-1)] == "x" or row1[int(move[1])-1] == "o":
                        print(f"{move} is already occupied by {row2[int(move[1])-1]}")
                        move = "null"
                if move[4] == "3": 
                    if row3[int(move[1])-1] == "x" or row3[int(move[1])-1] == "o":
                        print(f"{move} is already occupied by {row3[int(move[1])-1]}")
                        move = "null"
            except:
                continue
        if move[4] == "1":
            row1[int(move[1])-1] = "o"
        if move[4] == "2":
            row2[int(move[1])-1] = "o"
        if move[4] == "3":
            row3[int(move[1])-1] = "o"
        #AI Turn
        #Confirm AI Win
        #diagonal
        if row1[0] == "x" and row2[1] == "x" and row3[2] == "-":
            row3[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[0] == "x" and row2[1] == "x" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[0] == "-" and row2[1] == "x" and row3[2] == "x":
            row1[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[0] == "-" and row2[1] == "x" and row1[2] == "x":
            row3[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #horizontal
        if row1[0] == "x" and row1[1] == "x" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row2[0] == "x" and row2[1] == "x" and row2[2] == "-":
            row2[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[2] == "x" and row1[1] == "x" and row1[0] == "-":
            row1[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row2[2] == "x" and row2[1] == "x" and row2[0] == "-":
            row2[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #vertical
        if row3[1] == "x" and row2[1] == "x" and row1[1] == "-":
            row1[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[1] == "x" and row2[1] == "x" and row3[1] == "-":
            row3[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[2] == "x" and row2[2] == "x" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[2] == "x" and row2[2] == "x" and row3[2] == "-":
            row3[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[0] == "x" and row2[0] == "x" and row3[1] == "-":
            row3[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[0] == "x" and row2[0] == "x" and row1[0] == "-":
            row1[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #gap vertical
        if row1[2] == "x" and row3[2] == "x" and row2[2] == "-":
            row2[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[1] == "x" and row3[1] == "x" and row2[1] == "-":
            row2[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[0] == "x" and row3[0] == "x" and row2[0] == "-":
            row2[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #gap horizontal
        if row1[0] == "x" and row1[2] == "x" and row1[1] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row2[0] == "x" and row2[2] == "x" and row2[1] == "-":
            row2[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[0] == "x" and row3[2] == "x" and row3[1] == "-":
            row3[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #gap diagonal
        if row1[0] == "x" and row3[2] == "x" and row2[1] == "-":
            row2[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[2] == "x" and row3[0] == "x" and row2[1] == "-":
            row2[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #check if player might win:
        #diagonal
        if row1[0] == "o" and row2[1] == "o" and row3[2] == "-":
            row3[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[0] == "o" and row2[1] == "o" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[0] == "-" and row2[1] == "o" and row3[2] == "o":
            row1[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[0] == "-" and row2[1] == "o" and row1[2] == "o":
            row3[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #horizontal
        if row1[0] == "o" and row1[1] == "o" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row2[0] == "o" and row2[1] == "o" and row2[2] == "-":
            row2[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[2] == "o" and row1[1] == "o" and row1[0] == "-":
            row1[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row2[2] == "o" and row2[1] == "o" and row2[0] == "-":
            row2[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #vertical
        if row3[1] == "o" and row2[1] == "o" and row1[1] == "-":
            row1[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[1] == "o" and row2[1] == "o" and row3[1] == "-":
            row3[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row3[2] == "o" and row2[2] == "o" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[2] == "o" and row2[2] == "o" and row3[2] == "-":
            row3[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[2] == "o" and row3[2] == "o" and row2[2] == "-":
            row2[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[1] == "o" and row3[1] == "o" and row2[1] == "-":
            row2[1] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if row1[0] == "o" and row3[0] == "o" and row2[0] == "-":
            row2[0] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        #Starting Positions
        #when the player places adjecent to the AI
        if gameIteration == 0 and move == "c1 r2":
            row3[2] = "x"
        if gameIteration == 0 and move == "c2 r3":
            row1[0] = "x"
        if gameIteration == 1 and move == "c3 r1" and row3[2] == "x":
            row1[0] = "x"
        #heres the problem
        if gameIteration == 1 and move != "c3 r1" and row3[2] == "x" and row1[2] == "-" and row2[2] != "o":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue
        if gameIteration == 1 and row1[0] == "x" and row1[2] == "-":
            row1[2] = "x"
            print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
            continue       
        if gameIteration == 2 and row1[2] == "x" and row3[2] == "x" and row3[0] == "x":
            if row2[2] != "o":
                row2[2] = "x"
            elif row3[1] != "o":
                row3[1] = "x"
            else:
                row2[1] = "x"
        if gameIteration == 2 and row1[2] == "x" and row1[0] == "x" and row3[0] == "x":
            if row1[1] != "o":
                row1[1] = "x"
            elif row2[1] != "o":
                row2[1] = "x"
            else:
                pass
        #when the player starts opposite the AI
        if gameIteration == 0 and move == "c1 r1":
            row3[2] = "x"
        if gameIteration == 0 and move == "c3 r3":
            row1[0] = "x"
        if gameIteration == 1 and row3[2] == "x" and row1[0] == "o":
            row1[2] = "x"
        if gameIteration == 1 and row1[0] == "x" and row3[2] == "o":
            row1[2] = "x"
        #when the player starts in the middle away from you
        if gameIteration == 0 and move == "c3 r2":
            row3[2] = "x"
        if gameIteration == 0 and move == "c2 r1":
            row3[2] = "x"
        if gameIteration == 1 and row1[2] == "o" and row3[2] == "x":
            row1[0] = "x"
        if gameIteration == 1 and row2[2] == "o" and row3[2] == "x":
            row1[0] = "x"
        #when the player goes in the far corner
        if gameIteration == 0 and move == "c3 r1":
            row1[0] = "x"
        if gameIteration == 1 and row1[0] == "x" and row1[2] == "o":
            row3[2] = "x"
        #when the player goes in the middle
        if gameIteration == 0 and move == "c2 r2":
            row1[2] = "x"
        if gameIteration == 1 and row1[0] == "o" and row2[1] == "o" and row1[2] == "x":
            row3[2] = "x"
        print(str(row1) + "\n" + str(row2) +"\n" + str(row3))
        gameIteration+=1
        

                        

                        
    
