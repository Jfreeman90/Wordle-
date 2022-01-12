import tkinter as tk
import math
from tkinter import messagebox
from datetime import datetime
from random import choice
#------------------------INITIATE THE FIRST SCREEN
global attempt, word_to_find, word_letters, word_dictionary,initial_load
#start the game at attempt 0
attempt=0
#when the game loads up defein a variable so the correct display can be shown
initial_load=True

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
    raw_data.write("\n"+dt_start_date+','+dt_start_time+','+dt_end_time+','+str(word_to_find)+","+"W"+","+str(attempt+1)+","+str(''.join(letters_guessed))) 
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
    raw_data.write("\n"+dt_start_date+','+dt_start_time+','+dt_end_time+','+str(word_to_find)+","+"L"+","+str(attempt+1)+","+str(''.join(letters_guessed))) 
    raw_data.close()

#function to run when new game button is pressed which will reset everything
def new_game():
    from random import choice
    global initial_load
    #if the game has only just been started do not display a message box and just begin the game
    if initial_load==True:
        grid_canvas.delete('all')
        grid_canvas.configure(bg=main_colors[1])
        initial_load=False
        draw_grid()
        new_game_btn['text']='New Game'
    else: 
        #create a check box that allows the user to check if they want to run the entire script since it can take a while for larger data sets.
        check=messagebox.askyesno(title='Warning!', message='This will start a new game and you will lose all progress. \nStart new Game?')
        if check==True:
            global game_state_grid, attempt
            game_state_grid=[[0,0,0,0,0,0], 
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0]]
            attempt=0
            #print(game_state_grid)
            grid_canvas.delete('all')
            grid_canvas.configure(bg=main_colors[1])
            draw_grid()
            new_game_btn['text']='New Game'
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
new_game_btn=tk.Button(master=frm_end_game_button, text='Start Game', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command=new_game)
new_game_btn.grid(row=0, column=1, padx=(10,30), pady=(5,5))

# Run the application
window.mainloop()