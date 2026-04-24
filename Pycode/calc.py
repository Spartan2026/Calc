import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# to keep track of how many rows and columns do we have
row_count = len(button_values) # we have 5 rows for now
column_count = len(button_values[0]) # we have 4 columns for now


color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# to create the window
window = tkinter.Tk() # creates the window
window.title("Calculator")
# to make window unresizable by both width and height
window.resizable(False,False)
# we want the program to keep running and keep the window open

# to add componenets to our window, we need to create frame first.
frame = tkinter.Frame(window) # placing the frame inside window

label = tkinter.Label(frame,text="0", font=("Arial",45),background=color_black, 
                      foreground=color_white,anchor="e",width=column_count)
# the text label should take up the entire column space
# columns span refers to how mnay columns this label should take
# to stretch out the color to take up all 4 coumns,
# in tkinter, left-> west, right->east, up-->north, down-> south
label.grid(row=0, column=0,columnspan=column_count,sticky="we")




# for creating the button we are going to iterate over the 2D list of button_values

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        # creates the button and places it inside the frame.
        button = tkinter.Button(frame, text=value, font=("Arial",30),
                                width=column_count-1,height=1,
                                command=lambda value=value: button_clicked(value))
        
        # adds colors to buttons
        if value in top_symbols:
            button.config(foreground=color_black,background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        # to order the button in grid layout
        button.grid(row=row+1,column=column)


frame.pack()
# A+B, A-B, A*B, A/B


def clear_all():
    """
    function for clearing the display
    Pre-condition: Non
    """
    global A, B, operator
    A = "0"
    operator = None
    B = None


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        pass
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            pass
        elif value == "%":
            pass
    
    else: # digit or .
        if value == ".":
            # only one decimal point allowed, e.g, 5.5 not 5..5
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value # replace 0
            else:
                label["text"] += value #append digit


        



# to centre the window, we need to get the current width and height of our window and screen
window.update()
window_width= window.winfo_width()
window_height = window.winfo_height()
# we need to get the width and height of our computer screen
screen_width = window.winfo_width()
screen_height = window.winfo_height()

window_x = int((window_width/2)- (window_width/2))
window_y = int((window_height/2)- (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# we want the program to keep running and keep the window open
window.mainloop() # update window with the new size dimensions
