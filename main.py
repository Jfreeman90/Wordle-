import tkinter as tk
import math
from tkinter import messagebox
from datetime import datetime
from random import choice

#create the key
def create_key(length):
    key_list=[]
    for i in range(length):
        digits=list(range(26))
        #X=left, H=right
        step=['X','H']
        digit=str(choice(digits))
        if len(digit)==1:
            digit=str(0)+digit
        step=str(choice(step))
        keystep=(digit+step)
        key_list.append(keystep)
  
    key=''.join(key_list)
    return key

#split the key into a list of steps
def split_key(key):
    key_list=[]
    for i in range(int(len(key)/3)):
        key_step=key[i*3:i*3+3]
        key_list.append(key_step)
    return key_list

#use the key and algorithsm to encrypt the password
def encryption_algorithm(password, key):
    key_list=split_key(key)
    import string
    #set up a list to reference what is being picked
    lowercase_alphabet=list(string.ascii_lowercase)
    uppercase_alphabet=list(string.ascii_uppercase)
    numbers=['0','1','2','3','4','5','6','7','8','9']
    #empty list to store the encrypted password
    encrypted=[]
    for i in range(len(password)):
        steps=key_list[i][0:2]
        if steps[0]=='0':
            steps=int(key_list[i][1:2])
        else:
            steps=int(key_list[i][0:2])
        method=key_list[i][2]
        #print('steps:',steps,'method:', method)
        element=password[i]
         #if the password element is in numbers
        #algorithm used to encode the numbers
        if element in numbers:
            index_loc=numbers.index(element)
            if steps>len(numbers):
                steps=steps%len(numbers)
            if method=='H':
                if index_loc+steps > len(numbers)-1:
                    new_index=(steps-(len(numbers)-index_loc))
                else:
                    new_index=index_loc+steps
            else:
                if index_loc-steps < 0:
                    new_index=len(numbers)-(steps-index_loc)
                else:
                    new_index=index_loc-steps
            new_element=numbers[new_index]
            encrypted.append(new_element)
        #if the password element is a lowercase letter
        #algorithm used to encode the lowercase_letters as other lowercase letters
        elif element in lowercase_alphabet:
            #print('lower case')
            index_loc=lowercase_alphabet.index(element)
            #print('current index,',index_loc)
            if steps>len(lowercase_alphabet):
                steps=steps%len(lowercase_alphabet)
            if method=='H':
                #print('move right', steps)
                if index_loc+steps > len(lowercase_alphabet)-1:
                    new_index=(steps-(len(lowercase_alphabet)-index_loc))
                else:
                    new_index=index_loc+steps
            else:
                #print('move left',steps)
                if index_loc-steps < 0:
                    new_index=len(lowercase_alphabet)-(steps-index_loc)
                else:
                    new_index=index_loc-steps
            #print('new index',new_index)
            new_element=lowercase_alphabet[new_index]
            encrypted.append(new_element)  
          
        #if the password element is a lowercase letter
        #algorithm used to encode the lowercase_letters as other lowercase letters
        elif element in uppercase_alphabet:
            #print('upper case')
            index_loc=uppercase_alphabet.index(element)
            #print(index_loc)
            if steps>len(uppercase_alphabet):
                steps=steps%len(uppercase_alphabet)
            if method=='H': 
                #print('move right', steps)
                if index_loc+steps > len(uppercase_alphabet)-1:
                    new_index=(steps-(len(uppercase_alphabet)-index_loc))
                else:
                    new_index=index_loc+steps
            else:
                #print('move left',steps)
                if index_loc-steps < 0:
                    new_index=len(uppercase_alphabet)-(steps-index_loc)
                else:
                    new_index=index_loc-steps
            #print('new index',new_index)
            new_element=uppercase_alphabet[new_index]
            encrypted.append(new_element)
    return(''.join(encrypted))

#given the key and the encypted password return back to the normal password without storing it.
#the only variables stored are the key and the encrypted password
def decipher_encrytion_algorithm(encrypted_password, key):
    key_list=split_key(key)
    import string
    #set up a list to reference what is being picked
    lowercase_alphabet=list(string.ascii_lowercase)
    uppercase_alphabet=list(string.ascii_uppercase)
    numbers=['0','1','2','3','4','5','6','7','8','9']
    #empty list to store the encrypted password
    encrypted=[]
    for i in range(len(encrypted_password)):
        steps=key_list[i][0:2]
        if steps[0]=='0':
            steps=int(key_list[i][1:2])
        else:
            steps=int(key_list[i][0:2])
        method=key_list[i][2]
        #print('steps:',steps,'method:', method)
        element=encrypted_password[i]
         #if the password element is in numbers
        #algorithm used to encode the numbers
        if element in numbers:
            index_loc=numbers.index(element)
            if steps>len(numbers):
                steps=steps%len(numbers)
            if method=='X':
                if index_loc+steps > len(numbers)-1:
                    new_index=(steps-(len(numbers)-index_loc))
                else:
                    new_index=index_loc+steps
            else:
                if index_loc-steps < 0:
                    new_index=len(numbers)-(steps-index_loc)
                else:
                    new_index=index_loc-steps
            new_element=numbers[new_index]
            encrypted.append(new_element)
        #if the password element is a lowercase letter
        #algorithm used to encode the lowercase_letters as other lowercase letters
        elif element in lowercase_alphabet:
            #print('lower case')
            index_loc=lowercase_alphabet.index(element)
            #print('current index,',index_loc)
            if steps>len(lowercase_alphabet):
                steps=steps%len(lowercase_alphabet)
            if method=='X':
                #print('move right', steps)
                if index_loc+steps > len(lowercase_alphabet)-1:
                    new_index=(steps-(len(lowercase_alphabet)-index_loc))
                else:
                    new_index=index_loc+steps
            else:
                #print('move left',steps)
                if index_loc-steps < 0:
                    new_index=len(lowercase_alphabet)-(steps-index_loc)
                else:
                    new_index=index_loc-steps
            #print('new index',new_index)
            new_element=lowercase_alphabet[new_index]
            encrypted.append(new_element)  
          
        #if the password element is a lowercase letter
        #algorithm used to encode the lowercase_letters as other lowercase letters
        elif element in uppercase_alphabet:
            #print('upper case')
            index_loc=uppercase_alphabet.index(element)
            #print(index_loc)
            if steps>len(uppercase_alphabet):
                steps=steps%len(uppercase_alphabet)
            if method=='X': 
                #print('move right', steps)
                if index_loc+steps > len(uppercase_alphabet)-1:
                    new_index=(steps-(len(uppercase_alphabet)-index_loc))
                else:
                    new_index=index_loc+steps
            else:
                #print('move left',steps)
                if index_loc-steps < 0:
                    new_index=len(uppercase_alphabet)-(steps-index_loc)
                else:
                    new_index=index_loc-steps
            #print('new index',new_index)
            new_element=uppercase_alphabet[new_index]
            encrypted.append(new_element)
    return(''.join(encrypted))

#function that checks username are correctly formatted.
def check_username_rules(input):
    #check length
    #true means password/username is acceptable
    if 4<len(input)<14:
        for letter in input:
            import string
            #check for symbols
            symbols=list(string.punctuation)
        if letter in symbols:
            return False
    else:
        return False
    return True 
    
#function that checks passwords are correctly formatted.
def check_password_rules(input):
    #true means password/username is acceptable
    if 5<len(input)<14:
        for letter in input:
            import string
            #check for symbols
            symbols=list(string.punctuation)
        if letter in symbols:
            return False
    else:
        return False
    return True
    
    
#------------------------INITIATE THE FIRST SCREEN
global attempt, word_to_find, word_letters, word_dictionary,initial_load, user_log_in_succesful
#start the game at attempt 0
attempt=0
#when the game loads up defein a variable so the correct display can be shown
initial_load=True
user_log_in_succesful=False

#get a word for the dictionary of words avaiable
word_dictionary=[]
with open('6_letter_words.txt') as f:  #open the text file to get each word and add to the dictionary of words
    for word in f:
        word = word.strip()
        word_dictionary.append(word)
 
#print(word_dictionary)
word_to_find=choice(word_dictionary)
word_letters=list(word_to_find)
#print(word_letters)
#set up an empty list to store all of the letters pressed and entered by the user
global letters_guessed
letters_guessed=[]

# datetime object containing current date and time to initiate the file
newgameTime = datetime.now()
# dd/mm/YY H:M:S
global dt_start_date, dt_start_time
dt_start_date = newgameTime.strftime("%Y/%m/%d")  
dt_start_time = newgameTime.strftime("%H:%M:%S")        
#print(dt_start_date)
#print(dt_start_time)  

#create a grid that can be checked for each row where ach row is the correct word and value the user is looking for
#this variable will not be altered and just refered to to check things.
global correct_word_grid
correct_word_grid=[word_letters,word_letters,word_letters,word_letters,word_letters,word_letters]

#holds all values the player has entered 0 means that nothing has been entered
global game_state_grid
game_state_grid=[[0,0,0,0,0,0], 
				[0,0,0,0,0,0],
				[0,0,0,0,0,0],
				[0,0,0,0,0,0],
				[0,0,0,0,0,0],
				[0,0,0,0,0,0]]


#---------------ALL FUNCTIONS NEEDED-------------------
#function to highlight the row which the player is currently trying to guess, works based off an atetmpt number
def draw_outline(attempt):
    if attempt==0:
        #check which attempt the player is on and then draw a grey box to outline the current row the player may enter values on
        outline_x0=MARGIN - BUFFER/2 
        outline_y0=MARGIN + BUFFER/2 + (attempt* CELL_HEIGHT)
        outline_x1=MARGIN + BUFFER/2 + (6 * CELL_WIDTH )
        outline_y1=MARGIN + BUFFER/2 + (CELL_HEIGHT * (attempt+1))
        grid_canvas.create_rectangle(outline_x0, outline_y0, outline_x1, outline_y1, outline='white', fill=outline_row_color[0], width=1, tags='outline_row') 
    else:
        #check which attempt the player is on and then draw a grey box to outline the current row the player may enter values on
        outline_x0=MARGIN - BUFFER/2 
        outline_y0=MARGIN + BUFFER/2 + (attempt* CELL_HEIGHT)
        outline_x1=MARGIN + BUFFER/2 + (6 * CELL_WIDTH )
        outline_y1=MARGIN + BUFFER/2 + (CELL_HEIGHT * (attempt+1))
        grid_canvas.create_rectangle(outline_x0, outline_y0, outline_x1, outline_y1, outline='white', fill=outline_row_color[0], width=1, tags='outline_row')
        #check that any values on the previous row were correct and draw them down with a green box and text in them already
        previous_row=game_state_grid[attempt-1]
        word_check=correct_word_grid[attempt-1]
        for i in range(len(previous_row)):
            if previous_row[i]==word_check[i]:
                #replace the starting grid value with the correct value already found
                game_state_grid[attempt][i]=previous_row[i]
                x0 = MARGIN  + (i * CELL_WIDTH)
                y0 = MARGIN + BUFFER + (attempt * CELL_HEIGHT)
                x1 = MARGIN + ((i + 1) * CELL_WIDTH)
                y1 = MARGIN + (attempt + 1) * CELL_HEIGHT 
                grid_canvas.create_rectangle(x0, y0, x1, y1, outline='green', width=1, tags='prev_row_check_outline')
                #draw out the text value for what is in each part of the data frame
                x_loc=MARGIN  + (i * CELL_WIDTH + CELL_WIDTH/2)
                y_loc=MARGIN +(attempt * CELL_HEIGHT + CELL_HEIGHT/2) + BUFFER/2
                grid_canvas.create_text(x_loc, y_loc, text=previous_row[i], font=("Lucida Sans Typewriter", 20), tags='prev_row_check_text', fill=main_colors[0])
                
#draw out the grid check each element and update the canvas to display the game state
def draw_grid():
    #draw the outline of the row the player is currently on.
    draw_outline(attempt)
    
    for i in range(rows):
        for j in range(cols):
            element=game_state_grid[i][j]
            #draw a box around each element
            x0 = MARGIN  + j * CELL_WIDTH + 1
            y0 = MARGIN +BUFFER + i * CELL_HEIGHT + 1
            x1 = MARGIN + (j + 1) * CELL_WIDTH - 1
            y1 = MARGIN + (i + 1) * CELL_HEIGHT - 1
            
            #outline for each element
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline='black', width=1, tags='outlines')    
            #draw out the text value for what is in each part of the data frame
            x_loc=MARGIN  + (j * CELL_WIDTH + CELL_WIDTH/2)
            y_loc=MARGIN +(i * CELL_HEIGHT + CELL_HEIGHT/2) + BUFFER/2
            
 
            #check for values in the grid and draw out the corespending letters and frames depending on game state
            #elemnt in grid =0 is an unguessed value
            if element==0:
                grid_canvas.create_text(x_loc, y_loc, text=' ', font=("Lucida Sans Typewriter", 20), tags='unknown', fill=main_colors[0])
            elif element==correct_word_grid[i][j]:
                grid_canvas.create_text(x_loc, y_loc, text=element, font=("Lucida Sans Typewriter", 20), tags='correct_text', fill=main_colors[0])
                grid_canvas.create_rectangle(x0+1, y0, x1+1, y1, outline='green', width=2, tags='correct_outline')
            elif element in set(word_letters):
                grid_canvas.create_text(x_loc, y_loc, text=element, font=("Lucida Sans Typewriter", 20), tags='incorrect_text', fill=main_colors[0])
                grid_canvas.create_rectangle(x0+1, y0, x1+1, y1, outline='orange', width=2, tags='correct_wrong_place_outline')
            else:
                grid_canvas.create_text(x_loc, y_loc, text=element, font=("Lucida Sans Typewriter", 20), tags='incorrect_text', fill=main_colors[0])
                grid_canvas.create_rectangle(x0+1, y0, x1+1, y1, outline='red', width=2, tags='incorrect_outline')

#function to draw out a winning screen image that shows data and so on
def draw_vitory_scene():
    grid_canvas.create_image(MARGIN-5 ,MARGIN, anchor=tk.NW, image=victory_image)    
    # create text in the correct locations
    x = WIN_WIDTH/2
    y = WIN_HEIGHT/2
    grid_canvas.create_text(x, y-MARGIN, text="You win!", tags="winner", fill='black', font=("Arial", 32,'bold'))
    grid_canvas.create_text(x, y+MARGIN, text="WORD: "+str(word_to_find.upper()), tags="Winning_word", fill='black', font=("Arial", 16,'bold'))
    
#function to draw out a winning screen image that shows data and so on
def draw_losing_scene():
    grid_canvas.create_image(MARGIN-10 ,MARGIN-10, anchor=tk.NW, image=losing_image)
    # create text in the correct locations
    x = WIN_WIDTH/2
    y = WIN_HEIGHT/2
    grid_canvas.create_text(x, y-MARGIN, text="You lost!", tags="loser", fill='black',font=("Arial", 32,'bold'))
    grid_canvas.create_text(x, y+MARGIN, text="WORD: "+str(word_to_find.upper()), tags="Winning_word", fill='black', font=("Arial",16,'bold'))

#function that will be used everytime a cell is clicked
def cell_clicked(event):
    x,y=event.x, event.y
    #print(x,y)
    #check that the location clicked is on the board
    if MARGIN < x < WIN_WIDTH - MARGIN and MARGIN < y < WIN_HEIGHT - MARGIN and initial_load==False:
        #get row and column index from position
        global row, col, x0, y0, x1, y1
        row, col = math.floor((y - MARGIN) / CELL_HEIGHT), math.floor((x - MARGIN) / CELL_WIDTH)
        x0 = MARGIN + col * CELL_WIDTH + 1
        y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
        x1 = MARGIN + (col + 1) * CELL_WIDTH - 1
        y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
        
        #check that the row can be3 clicked if it matches up with the attempts taken so far
        if attempt==row and game_state_grid[row][col]==0:
            grid_canvas.delete('highlight')
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")

#function that will be used everytime a cell is left clicked to delete and reset the cells infomation
def cell_right_clicked(event):
    x,y=event.x, event.y
    grid_canvas.delete('highlight')
    #print(x,y)
    #check that the location clicked is on the board
    if MARGIN < x < WIN_WIDTH - MARGIN and MARGIN < y < WIN_HEIGHT - MARGIN:
        #get row and column index from position
        global row, col, x0, y0, x1, y1
        row, col = math.floor((y - MARGIN) / CELL_HEIGHT), math.floor((x - MARGIN) / CELL_WIDTH)
        x0 = MARGIN + col * CELL_WIDTH + 1
        y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
        x1 = MARGIN + (col + 1) * CELL_WIDTH - 1
        y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
        
        #check that the row can be clicked if it matches up with the attempts taken so far
        if attempt==row:
            grid_canvas.create_rectangle(x0, y0, x1, y1, fill=outline_row_color[0], outline='black',width=1, tags="deleted")
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")
            #reset the game state grid to 0
            game_state_grid[row][col]=0

#function that will delete the letter in the current grid space
def delete_key_pressed(event):
    global row, col, attempt, game_state_grid
    grid_canvas.delete('highlight')
    #check that the row can be clicked if it matches up with the attempts taken so far
    x0 = MARGIN + col * CELL_WIDTH + 1
    y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
    x1 = MARGIN + (col + 1) * CELL_WIDTH - 1
    y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
    if attempt==row:
        grid_canvas.create_rectangle(x0, y0, x1, y1, fill=outline_row_color[0], outline='black',width=1, tags="deleted")
        grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")
        #reset the game state grid to 0
        game_state_grid[row][col]=0
            
            
#function that will draw on the value pressed at the correct location based on where the cell has been clicked
def key_pressed(event):
    global game_state_grid,letters_guessed
    #print('row:',row,'col:', col)
    guessed_value=event.char
    #print('guessed_value:', guessed_value)
    import string
    uppercases=string.ascii_uppercase
    guessed_value=str(guessed_value.upper())
    letters_guessed.append(guessed_value)
    if attempt==row  and 0<=col<=cols and guessed_value in uppercases and game_state_grid[row][col]==0: #check input and location are valid before drawing the attempt
        game_state_grid[row][col]=guessed_value
        x_loc=MARGIN + (col * CELL_WIDTH + CELL_WIDTH/2)
        y_loc=MARGIN + (row * CELL_HEIGHT + CELL_HEIGHT/2) + BUFFER/2
        #edit the grid to show what the player has typed in
        grid_canvas.create_text(x_loc, y_loc, text=guessed_value,font=("Lucida Sans Typewriter", 20), tags='guess', fill=main_colors[0])
    else:
        messagebox.showinfo(title="Input error", message='There is already a letter in this space. \nYou can right click the grid sqaure to delete the letter')
    
#function that allows the player to move to the right by clicking the right arrow
def move_right(event):
    global row, col
    if 0<=col<5:
        grid_canvas.delete('highlight')
        col=col+1
        #get row and column index from position
        x0 = MARGIN + (col) * CELL_WIDTH + 1
        y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
        x1 = MARGIN + ((col) + 1) * CELL_WIDTH - 1
        y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
            
        #check that the row can be clicked if it matches up with the attempts taken so far
        if attempt==row and game_state_grid[row][col]==0:
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")
        elif attempt==row and game_state_grid[row][col]!=0:
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=1, tags="highlight")

#function that allows the player to move to the left by clicking the left arrow
def move_left(event):
    global row, col
    if 0<col<=5:
        grid_canvas.delete('highlight')
        col=col-1
        #get row and column index from position
        x0 = MARGIN + (col) * CELL_WIDTH + 1
        y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
        x1 = MARGIN + ((col) + 1) * CELL_WIDTH - 1
        y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
            
        #check that the row can be clicked if it matches up with the attempts taken so far
        if attempt==row and game_state_grid[row][col]==0:
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")
        elif attempt==row and game_state_grid[row][col]!=0:
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=1, tags="highlight")
            
#function that will compare all of the values entered and draw out accordingly and add one to attempts so that a new grid can be drawn correct
#and intereacted with
def check_row():
    global attempt, game_state_grid
    #print(word_letters)
    #check the user has attempted to fill in each space
    if 0 not in game_state_grid[attempt]:
        if attempt==5:
            if game_state_grid[attempt]==word_letters:
                end_game_win_data_collection()
                draw_vitory_scene()
            else: 
                end_game_lose_data_collection()
                draw_losing_scene()
        elif game_state_grid[attempt]==word_letters:
            end_game_win_data_collection()
            draw_vitory_scene()
        else:
            #increase attemps by 1 and redraw the grid
            attempt+=1
            grid_canvas.delete('outline_row')
            grid_canvas.delete('highlight')
            grid_canvas.delete('deleted')
            grid_canvas.delete('guess')
            #redraw the grid after updating
            draw_grid()
    else:
        messagebox.showinfo(title="Input error", message='Enter a letter in each box before checking row')

#function that calls check_row when enter is pressed
def enter_pressed(event):
    check_row()

#function that will run once the game ends, either a win or a loss and collect all the data on the game played
def end_game_win_data_collection():
    # datetime object containing current date and time to initiate the file
    endgameTime = datetime.now()
    # dd/mm/YY H:M:S
    global  dt_end_time, letters_guessed 
    dt_end_time = endgameTime.strftime("%H:%M:%S")        
    #print(dt_end_time)  
    # In same directory open file in append mode and add a new line of data
    raw_data=open('raw_data_collection.txt',"a")
    raw_data.write("\n"+dt_start_date+','+dt_start_time+','+dt_end_time+','+str(username)+','+str(word_to_find)+","+"W"+","+str(attempt+1)+","+str(''.join(letters_guessed))) 
    raw_data.close()

#function that will run once the game ends, either a win or a loss and collect all the data on the game played
def end_game_lose_data_collection():
    # datetime object containing current date and time to initiate the file
    endgameTime = datetime.now()
    # dd/mm/YY H:M:S
    global  dt_end_time, letters_guessed
    dt_end_time = endgameTime.strftime("%H:%M:%S")        
    #print(dt_end_time)  
    # In same directory open file in append mode and add a new line of data
    raw_data=open('raw_data_collection.txt',"a")
    raw_data.write("\n"+dt_start_date+','+dt_start_time+','+dt_end_time+','+str(username)+','+str(word_to_find)+","+"L"+","+str(attempt+1)+","+str(''.join(letters_guessed))) 
    raw_data.close()

#function that will open database of username/passwords and collect them into list(username, key, encrypted_password) to look up.
def username_database_to_lists():
    database=open('username_database.txt', 'r')
    lists=[]
    #mport each data list into a list of lists
    for line in database:
        stripped_line=line.strip()
        infomation=stripped_line.split(',')
        lists.append(infomation)
    #go through the lists of lists above and set up a column of each variable that can be used to search through usernames and use
    #the index location to find all other infomation
    usernames=[]
    keys=[]
    encrypted_passwords=[]
    for data in lists:
        usernames.append(data[0])
        keys.append(data[1])
        encrypted_passwords.append(data[2])
    return usernames, keys, encrypted_passwords
    
    
#allow the user to create an account with the same constraints as password. Look up all other usernames to check it hasnt been taken
def create_account():
    global user_log_in_succesful, usernames, username
    #get the username and password
    username=username_input.get()
    password=password_input.get()
    #check the input is correctly format
    if check_username_rules(username)==True: 
        if check_password_rules(password) ==True:
            if username in usernames:
                #find the usernames index location to reference.
                log_in_window.lift()
                messagebox.showinfo(title="Log in Error", message='This username already exists. Try again')
                log_in_window.lift()
            else: 
                key=create_key(13)
                encrypted_password=encryption_algorithm(password, key)
                # In same directory open file in append mode and add a new line username and passwords with a key
                username_data=open('username_database.txt',"a")
                username_data.write("\n"+str(username)+','+str(key)+','+str(encrypted_password))
                username_data.close()
                user_log_in_succesful=True
                log_in_window.destroy()
                #begin the game by updating the canvas
                if user_log_in_succesful==True:
                    global row, col,initial_load
                    window.title("Wordle+ "+str(username))
                    row=0
                    col=0
                    grid_canvas.delete('all')
                    grid_canvas.configure(bg=main_colors[1])
                    initial_load=False
                    draw_grid()
                    new_game_btn['text']='New Game'
                    x0 = MARGIN + col * CELL_WIDTH + 1
                    y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
                    x1 = MARGIN + (col + 1) * CELL_WIDTH - 1
                    y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
                        
                    #check that the row can be clicked if it matches up with the attempts taken so far
                    if attempt==row and game_state_grid[row][col]==0:
                        grid_canvas.delete('highlight')
                        grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")
                
        else:
            messagebox.showinfo(title="Log in Error", message='Passwords must be between 6 and 13 letters.\nUsernames must only contain letters and numbers.')
            log_in_window.lift()
    else:
        messagebox.showinfo(title="Input Error", message='Usernames must be between 5 and 13 letters.\nUsernames must only contain letters and numbers.')
        log_in_window.lift()
        
#check the user names match up with someone in the files already and check that the password entered by the user matches 
#decipher the stored password using the key and check it is equal to the entry.
def log_in_user():
    global user_log_in_succesful, username
    #get the username and password
    username=username_input.get()
    password=password_input.get()
    #check username exists
    if username in usernames:
        #find the usernames index location to reference.
        user_index=usernames.index(username)
        decipher_pass=decipher_encrytion_algorithm(encrypted_passwords[user_index], keys[user_index])
        #log the user in
        if   password==decipher_pass:
            user_log_in_succesful=True
            log_in_window.destroy()
        else:
            messagebox.showinfo(title="Log in Error", message='Incorrect username or password. Try again')
            log_in_window.lift()  
    else:
        messagebox.showinfo(title="Log in Error", message='This username doesnt not exist press create account to start.')
        log_in_window.lift() 
        
    #begin the game
    if user_log_in_succesful==True:
        global row, col,initial_load
        window.title("Wordle+ "+str(username))
        row=0
        col=0
        grid_canvas.delete('all')
        grid_canvas.configure(bg=main_colors[1])
        initial_load=False
        draw_grid()
        new_game_btn['text']='New Game'
        x0 = MARGIN + col * CELL_WIDTH + 1
        y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
        x1 = MARGIN + (col + 1) * CELL_WIDTH - 1
        y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
            
        #check that the row can be clicked if it matches up with the attempts taken so far
        if attempt==row and game_state_grid[row][col]==0:
            grid_canvas.delete('highlight')
            grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")

#function that will log the user in when pressing enter if they have entered the password
def enter_to_log_in_pressed(event):
    log_in_user()

#function that will open a new window and allow users to enter a username and password
def log_in_window():
    #get relative x and y values of the original window
    x = window.winfo_x()
    y = window.winfo_y()
    #open a new pop up window and re position it relative to the original window
    #log in window must be global to allow it to be destroyed after clicking
    global log_in_window
    log_in_window = tk.Toplevel(window)
    log_in_window.geometry("+%d+%d" % (x+5,  y + 150))
    #log_in_window.geometry('280x100')
    
    #FRAME TO HOLD second window infomation
    frm_window2=tk.Frame(master=log_in_window, bg=main_colors[1])
    frm_window2.grid(row=0, column=0, sticky="ew")
    frm_window2.grid_columnconfigure([0,1], weight=1)
    frm_window2.grid_rowconfigure([0,1,2], weight=1)
    
    #define the username and password input string variables
    global username_input, password_input
    username_input = tk.StringVar()
    password_input = tk.StringVar()
    #username label hold the infomation
    username_lbl=tk.Label(master=frm_window2, text="Username:",font=("Lucida Sans Typewriter", 14, "bold"), fg=main_colors[0], bg=main_colors[1])
    username_lbl.grid(row=0, column=0, padx=(0,0), pady=(0,0))
    #username entry
    username_ent=tk.Entry(master=frm_window2, textvariable=username_input, width = 16)
    username_ent.grid(row=0, column=1, padx=(0,0), pady=(0,0))
    
    #password label hold the infomation
    password_lbl=tk.Label(master=frm_window2, text="Password:",font=("Lucida Sans Typewriter", 14, "bold"), fg=main_colors[0], bg=main_colors[1])
    password_lbl.grid(row=1, column=0, padx=(0,0), pady=(0,0))
    #password entry
    password_ent=tk.Entry(master=frm_window2, show="*", textvariable=password_input, width = 16)
    password_ent.grid(row=1, column=1, padx=(0,0), pady=(0,0))
    password_ent.bind("<Return>", enter_to_log_in_pressed)        #bind ENTER to the password entry
    
    #Button to create account
    create_account_btn=tk.Button(master=frm_window2, text="Create Account", font=("Lucida Sans Typewriter", 10), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command=create_account)
    create_account_btn.grid(row=2, column=0, padx=(4,4), pady=(3,3))
    #Button to log in
    log_in_btn=tk.Button(master=frm_window2, text="Log in", font=("Lucida Sans Typewriter", 10), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3,width = 15, command=log_in_user)
    log_in_btn.grid(row=2, column=1, padx=(4,4), pady=(3,3))
    
#function to run when new game button is pressed which will reset everything
def new_game():
    from random import choice
    global initial_load, user_log_in_succesful
    global game_state_grid, attempt
    global row, col
    #if the game has only just been started display a pop up window that will open a user/password entry box.
    if initial_load==True:
        #initial_load=False
        log_in_window()
    else: 
        #create a check box that allows the user to check if they want to run the entire script since it can take a while for larger data sets.
        check=messagebox.askyesno(title='Warning!', message='This will start a new game and you will lose all progress. \nStart new Game?')
        if check==True:
            game_state_grid=[[0,0,0,0,0,0], 
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0]]
            row=0
            col=0                
            attempt=0
            #print(game_state_grid)
            grid_canvas.delete('all')
            grid_canvas.configure(bg=main_colors[1])
            draw_grid()
            new_game_btn['text']='New Game'
            x0 = MARGIN + col * CELL_WIDTH + 1
            y0 = MARGIN + row * CELL_HEIGHT + 1 +BUFFER
            x1 = MARGIN + (col + 1) * CELL_WIDTH - 1
            y1 = MARGIN + (row + 1) * CELL_HEIGHT - 1 
        
            #check that the row can be3 clicked if it matches up with the attempts taken so far
            if attempt==row and game_state_grid[row][col]==0:
                grid_canvas.delete('highlight')
                grid_canvas.create_rectangle(x0, y0, x1, y1, outline=highlights[0], width=2, tags="highlight")
            
            #pick a new word
            global word_to_find, word_letters, word_dictionary
            word_to_find=choice(word_dictionary)
            word_letters=list(word_to_find)
            #print(word_letters)
            
            global correct_word_grid
            correct_word_grid=[word_letters,word_letters,word_letters,word_letters,word_letters,word_letters]
            
            #restart the timer  
            newgameTime = datetime.now()
            # dd/mm/YY H:M:S
            global dt_start_date, dt_start_time
            dt_start_date = newgameTime.strftime("%Y/%m/%d")  
            dt_start_time = newgameTime.strftime("%H:%M:%S")        
            #print(dt_start_date)
            #print(dt_start_time) 




# ------------------------------------ ALL APP FORMATTING -------------------------------------------
#variables for app size and also drawing the grid
global WIN_HEIGHT, WIN_WIDTH, MARGIN, CELL_WIDTH, CELL_HEIGHT, BUFFER, rows, cols
rows=len(game_state_grid[0])     
cols=len(game_state_grid)
#all variables to determine grid size and canvas size.
MARGIN=25
CELL_WIDTH=40
CELL_HEIGHT=60
WIN_HEIGHT=MARGIN * 2 + CELL_HEIGHT * cols
WIN_WIDTH=MARGIN * 2 + CELL_WIDTH * rows
BUFFER=12	#space between each rectangle

#use the username and password to look up all of the infomation from the data base and decided if they can log in or not.
global usernames, keys, encrypted_passwords
usernames, keys, encrypted_passwords=username_database_to_lists() 


#color variables that can change the whole program straight away
main_colors=['black','white']               #brown, light yellow
button_colors=['#000000','#AFEEEE']         #black, light blue
highlights=['#BA55D3', '#0000FF']           #gold, dark blue
font_colors=['#000000', '#696969']          #black, dark gray.
victory_colors=["#FFFAF0", "#D8BFD8"]      	#text and background for victory scene
losing_colors=["#A0522D", "#D8BFD8"]      	#text and background for victory scene
outline_row_color=['#DCDCDC']




#------------------ALL OF THE BELOW IS FORMATING FOR THE GUI AND ITS DISPLAYS
# Create instance
#have to use tkx if using a bloon widget to hover over tool tips.
window = tk.Tk()
# Disable resizing the GUI
window.resizable(0,0)  #(x,y)
# Add a title
window.title("Wordle+ - APP (jlf)")

#losing and winning images
losing_image = tk.PhotoImage(file='LosingImage.png')
victory_image = tk.PhotoImage(file='VictoryImage.png')

#FRAME TO HOLD TITLE
frm_title=tk.Frame(background=main_colors[1])
frm_title.grid(row=0, column=0, sticky="ew")
frm_title.grid_columnconfigure(0, weight=1)

#TITLE
lbl_title=tk.Label(master=frm_title, 
                text="WORDLE+", font=("Minion Pro Med", 30,  "bold"), foreground=main_colors[0], background=main_colors[1])
lbl_title.grid(row=0, column=0, sticky="ew")
     
#load all of the images needed via tk.Photoimage
titlescreen = tk.PhotoImage(file='loadingImage.png')
#FRAME TO HOLD CANVAS AND WORD GRID
frm_grid=tk.Frame(background=main_colors[1])
frm_grid.grid(row=1, column=0, sticky="ew")
frm_grid.grid_rowconfigure(0, weight=1)

#DRAWING CANVAS HERE 
grid_canvas=tk.Canvas(master=frm_grid, width=WIN_WIDTH, height=WIN_HEIGHT, bg=main_colors[1], highlightthickness=0)
grid_canvas.create_image(MARGIN ,MARGIN, anchor=tk.NW, image=titlescreen)  
grid_canvas.grid(row=0, column=0)

#define which buttons and events can be used when interacting with the canvas
grid_canvas.bind("<Button-1>", cell_clicked)          #bind left mouse click to the canvas with a command to follow
grid_canvas.bind("<Button-3>", cell_right_clicked)    #bind right mouse click to the canvas with a command to follow
grid_canvas.bind("<Key>", key_pressed)                #bind a key which will be numbers to the canvas with a command to draw the number on the canvas
grid_canvas.bind("<Return>", enter_pressed)           #bind ENTER to the entry that will run the same as button pressed
grid_canvas.bind("<Right>", move_right)               #bind right arrow 
grid_canvas.bind("<Left>", move_left)                 #bind left arrow
grid_canvas.bind("<Delete>", delete_key_pressed)        #bind delete key to do the same as right cell clicked
grid_canvas.bind("<BackSpace>", delete_key_pressed)        #bind delete key to do the same as right cell clicked
grid_canvas.focus_set() #set focus of canvas here so when a key is pressed it can be used

#FRAME TO HOLD END GAME BUTTONS
frm_end_game_button=tk.Frame(background=main_colors[1])
frm_end_game_button.grid(row=2, column=0, sticky="ew", pady=(0,5))
frm_end_game_button.grid_rowconfigure(0, weight=1)
frm_end_game_button.grid_columnconfigure([0,1], weight=1)

#SUBMIT GUESS
btn_submit_guess=tk.Button(master=frm_end_game_button, text='Guess Row', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command=check_row)
btn_submit_guess.grid(row=0, column=0, padx=(30,10), pady=(5,5))

#NEW GAME BUTTON
new_game_btn=tk.Button(master=frm_end_game_button, text='Log In', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command=new_game)
new_game_btn.grid(row=0, column=1, padx=(10,30), pady=(5,5))

# Run the application
window.mainloop()
