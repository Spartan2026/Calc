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
window.mainloop()

# to add componenets to our window, we need to create frame first.
frame = tkinter.Frame(window) # placing the frame inside window

label = tkinter.Label(frame, font=("Arial",45),background=color_black, 
                      foreground=color_white)

