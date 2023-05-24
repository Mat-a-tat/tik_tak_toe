#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def choose_player():
    
    global choice
    
    global space_3
    global space_2
    global space_1

    global current_player
    global move
    global legal_moves
    
    choice = '_'
    
    space_3 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    space_2 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    space_1 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']

    current_player = ''
    move = 0
    legal_moves = [1,2,3,4,5,6,7,8,9]
    
    player_1 = input("Do you want to be X or O?:" )
    X_and_O = ['X','O','x','o']
    
    while player_1 not in X_and_O:
        print("Sorry, I can only see X and O, please choose one!")
        player_1 = input("Do you want to be X or O?:" )
        
    current_player = player_1
    
    if player_1 == 'X' or player_1 == 'x':
        player_2 = 'O'
    else:
        player_1 = 'O'
        player_2 = 'X'
    

    player_move(player_1,player_2,current_player,legal_moves)


# In[ ]:


def print_board():

    print('\n')
    print(''.join(space_3))
    print('---+---+---')
    print(''.join(space_2))
    print('---+---+---')
    print(''.join(space_1))
    print('\n')


# In[ ]:


def change_board(move,player_1,player_2,current_player,legal_moves):
    
    
    if move in range (0,4):
        if move == 1:
            space_1[1] = current_player
        elif move == 2:
            space_1[5] = current_player
        elif move == 3:
            space_1[9] = current_player
            
    elif move in range (3,7):
        if move == 4:
            space_2[1] = current_player
        elif move == 5:
            space_2[5] = current_player
        elif move == 6:
            space_2[9] = current_player
            
    elif move in range (6,10):
        if move == 7:
            space_3[1] = current_player
        elif move == 8:
            space_3[5] = current_player
        elif move == 9:
            space_3[9] = current_player
    
    else:
        print ('Error')
        
    who_wins(current_player)

    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
 
        
        
    player_move(player_1,player_2,current_player,legal_moves)


# In[ ]:


def who_wins(current_player):
    
    space_rows = [space_1,space_2,space_3]
    
    for horizontal in space_rows:
        if all(horizontal[char] == current_player for char in [1, 5, 9]):
            print(f"{current_player} got a horizontal, {current_player} wins!")
            play_again()
            
    
    if all(vertical[1] == current_player for vertical in space_rows) or \
       all(vertical[5] == current_player for vertical in space_rows) or \
       all(vertical[9] == current_player for vertical in space_rows):
        print(f"{current_player} got a vertical, {current_player} wins!")
        play_again()
    
    #check diagnals
    if space_1[1] == current_player and space_2[5] == current_player and space_3[9] == current_player:
        print(f"{current_player} got a diagnal, {current_player} wins!")
        play_again()
    if space_1[9] == current_player and space_2[5] == current_player and space_3[1] == current_player:
        print(f"{current_player} got a diagnal, {current_player} wins!")
        play_again()
    
    if legal_moves == []:
        print ("RIP, its a tie!")
        play_again()
    
    '''
    This all function works, and is technicly shorter, but is less readable, I think.
    if all(space_rows[i][j] == current_player for i, j in [(0, 1), (1, 5), (2, 9)]):
        print(f"{current_player} wins!")
        play_again()
    '''


# In[ ]:


def player_move(player_1,player_2,current_player,legal_moves):

    while choice != 'N':
        print_board()

        move = 100
        move = input("Please choose a move using your numberpad(1-9):")

        if move.isdigit(): 
            move = int(move)

        while move not in range(0,10):
            print("Whoops! That dosen't work, sorry!")
            move = input("Please choose a move using your numberpad:")

            if move.isdigit(): 
                move = int(move)

        while move not in legal_moves:
            print(move)
            print("Please choose a spot not already taken up.")
            print_board()
            move = input("Please choose a move using your numberpad:")

            if move.isdigit(): 
                move = int(move)

        legal_moves.remove(move)

        change_board(move,player_1,player_2,current_player,legal_moves)


# In[ ]:


def play_again():

    choice = 'Wrong'
    yes_no = ['Y','N']
    print_board()
    
    while choice not in yes_no:
        
        choice = input("Keep playing? (Y or N) ").upper()
    
        if choice not in yes_no:
            print("Sorry, please choose Y or N!")
        
        if choice == 'N':
            print("Thanks for playing!")
        else:
            choose_player()


# In[ ]:


choose_player()


# In[ ]:





# In[ ]:




