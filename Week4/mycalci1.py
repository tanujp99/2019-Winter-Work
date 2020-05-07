
from tkinter import *

x3 = ""
def press(num): 
	# point out the global expression variable 
	global x3
	global x2
	global x1

	# concatenation of string 
	x3 = x1 + str(num) + x2

	# update the expression by using set method 
	# equation.set(x3) 


root = Tk() 

# set the background colour of root window 
# root.configure(background="light green") 

# set the title of root window 
root.title("Simple Calculator") 

# set the configuration of root window 
# root.geometry("265x125") 

# StringVar() is the variable class 
# we create an instance of this class 
equation1 = StringVar() 
equation2 = StringVar() 
equation3 = StringVar() 

# create the text entry box for 
# showing the expression . 
s1 = Entry(root) 

# grid method is used for placing 
# the widgets at respective positions 
# in table like structure . 
s1.grid(columnspan=4, ipadx=70) 
x1 = s1.get()
s2 = Entry(root) 
s2.grid(columnspan=4, ipadx=70) 
x2 = s2.get()
s3 = Entry(root) 
s3.grid(columnspan=4, ipadx=70) 
x3 = s3.get()

# equation.set('enter your expression') 

# create a Buttons and place at a particular 
# location inside the root window . 
# when user press the button, the command or 
# function affiliated to that button is executed . 
button1 = Button(root, text=' 1 ', 
                command=lambda: press(1), height=1, width=7) 
button1.grid(row=4, column=0) 

button2 = Button(root, text=' 2 ', 
                command=lambda: press(2), height=1, width=7) 
button2.grid(row=4, column=1) 

button3 = Button(root, text=' 3 ', 
                command=lambda: press(3), height=1, width=7) 
button3.grid(row=4, column=2) 

button4 = Button(root, text=' 4 ', 
                command=lambda: press(4), height=1, width=7) 
button4.grid(row=5, column=0) 

button5 = Button(root, text=' 5 ',
                command=lambda: press(5), height=1, width=7) 
button5.grid(row=5, column=1) 

button6 = Button(root, text=' 6 ', 
                command=lambda: press(6), height=1, width=7) 
button6.grid(row=5, column=2) 

button7 = Button(root, text=' 7 ',
                command=lambda: press(7), height=1, width=7) 
button7.grid(row=5, column=0) 

button8 = Button(root, text=' 8 ',
                command=lambda: press(8), height=1, width=7) 
button8.grid(row=6, column=1) 

button9 = Button(root, text=' 9 ',
                command=lambda: press(9), height=1, width=7) 
button9.grid(row=6, column=2) 

button0 = Button(root, text=' 0 ',
                command=lambda: press(0), height=1, width=7) 
button0.grid(row=6, column=0) 

plus = Button(root, text=' + ',  
            command=lambda: press("+"), height=1, width=7) 
plus.grid(row=4, column=3) 

minus = Button(root, text=' - ', 
            command=lambda: press("-"), height=1, width=7) 
minus.grid(row=5, column=3) 

multiply = Button(root, text=' * ',
                command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=6, column=3) 

divide = Button(root, text=' / ', 
                command=lambda: press("/"), height=1, width=7) 
divide.grid(row=7, column=3) 

# clear = Button(root, text='C', 
#             command=clear, height=1, width=7) 
# clear.grid(row=7, column='1') 



s3.delete(0, END)
s3.insert(0, x3)


# start the root 
root.mainloop() 
