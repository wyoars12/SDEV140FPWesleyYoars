from tkinter import * # Importing tkinter
from types import LambdaType # Importing lambda
from tkinter import PhotoImage

root = Tk()  # Adding first window
root.title("Simple Calcultor") #Setting roots title name

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Define Buttons

def button_switch():
    open()

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = int(e.get())
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
   
    if math == "multipulcation":
        e.insert(0, f_num * int(second_number))
    
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multipulcation"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)

def button_root():
    first_number = e.get()
    global f_num
    global math
    math = "square root"
    f_num = int(first_number)
    e.delete(0, END)

def button_squared():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = int(first_number)
    e.delete(0, END)

def open():
    top = Tk()  # Adding first window
    top.title("Simple Calcultor") #Setting roots title name

    f = Entry(top, width=35, borderwidth=5)
    f.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    top.title("Adavanced Calculator")
    openNewLabel = Label(top, text="Click the picture to go back Simple Calculator")
    openNewLabel.pack()
    buttonNewImage = Button(top, text="Image of the basic math operators", padx=40, pady=20, command=button_close) # Sizes button and gives a command to do when clicked
    buttonSwitchWindow = Button(top, text="asdadsad", padx=114, pady=20, command=button_switch)

    buttonSwitchWindow.grid(row=1, column=0, columnspan=3)
    buttonNewImage.grid(row=1, column=0, columnspan=3) # Places button in certain area

# Sizing and giving commands to Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)) # Sizes button and gives a command to do when clicked
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)) # Sizes button and gives a command to do when clicked
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)) # Sizes button and gives a command to do when clicked
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)) # Sizes button and gives a command to do when clicked
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)) # Sizes button and gives a command to do when clicked
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)) # Sizes button and gives a command to do when clicked
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)) # Sizes button and gives a command to do when clicked
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)) # Sizes button and gives a command to do when clicked
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)) # Sizes button and gives a command to do when clicked
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)) # Sizes button and gives a command to do when clicked
button_Add = Button(root, text="+", padx=39, pady=20, command=button_add) # Sizes button and gives a command to do when clicked
button_Equal = Button(root, text="=", padx=87, pady=20, command=button_equal) # Sizes button and gives a command to do when clicked
button_Clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear) # Sizes button and gives a command to do when clicked
button_Subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract) # Sizes button and gives a command to do when clicked
button_Multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply) # Sizes button and gives a command to do when clicked
button_Divide = Button(root, text="/", padx=40, pady=20, command=button_divide) # Sizes button and gives a command to do when clicked
buttonSwitchWindow = Button(root, text="asdadsad", padx=114, pady=20, command=button_switch) # Sizes button and gives a command to do when clicked


# Put buttons on screen

button_1.grid(row=4, column=0) # Places button in certain area
button_2.grid(row=4, column=1) # Places button in certain area
button_3.grid(row=4, column=2) # Places button in certain area

button_4.grid(row=3, column=0) # Places button in certain area
button_5.grid(row=3, column=1) # Places button in certain area
button_6.grid(row=3, column=2) # Places button in certain area

button_7.grid(row=2, column=0) # Places button in certain area
button_8.grid(row=2, column=1) # Places button in certain area
button_9.grid(row=2, column=2) # Places button in certain area

button_0.grid(row=5, column=0) # Places button in certain area
button_Clear.grid(row=5, column=1, columnspan=2) # Places button in certain area
button_Add.grid(row=6, column=0) # Places button in certain area
button_Equal.grid(row=6, column=1, columnspan=2) # Places button in certain area

button_Subtract.grid(row=7, column=0) # Places button in certain area
button_Multiply.grid(row=7, column=1) # Places button in certain area
button_Divide.grid(row=7, column=2) # Places button in certain area

buttonSwitchWindow.grid(row=1, column=0, columnspan=3) # Places button in certain area


root.mainloop() # Starts the main program
    