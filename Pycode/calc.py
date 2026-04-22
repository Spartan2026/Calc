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
                      foreground=color_white,anchor="e")
# the text label should take up the entire column space
# columns span refers to how mnay columns this label should take
# to stretch out the color to take up all 4 coumns,
# in tkinter, left-> west, right->east, up-->north, down-> south
label.grid(row=0, column=0,columnspan=column_count,sticky="we")
frame.pack()



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


def button_clicked(value):
    pass

# we want the program to keep running and keep the window open
window.mainloop()