from tkinter import *
def add():
    global x1
    global x2
    global x3
    global equation1
    global equation2
    global equation3
    global expression
    expression = str(equation1)+ "+"+ str(equation2)
    
    total = str(eval(expression)) 
    equation3.set(total)


def press(val):
    print("this is non functional")

def sub():
    global x1
    global x2
    global x3
    x3 = x1 - x2
    text = Text(root)
    s3.Text.insert(END,x3)
    text.configure(state='disabled')
def mult():
    global x1
    global x2
    global x3
    x3 = x1 * x2
    text = Text(root)
    s3.Text.insert(END,x3)
    text.configure(state='disabled')

def div():
    print("hi")

root = Tk()
expression=""
equation1 = StringVar() 
equation2 = StringVar() 
equation3 = StringVar() 

s1 = Entry(root, textvariable= equation1) 
s1.grid(columnspan=4, ipadx=70) 
x1 = s1.get()
s2 = Entry(root, textvariable= equation2) 
s2.grid(columnspan=4, ipadx=70) 
x2 = s2.get()
s3 = Entry(root, textvariable= equation3) 
s3.grid(columnspan=4, ipadx=70) 
x3 = s3.get()

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
            command=lambda: add(), height=1, width=7) 
plus.grid(row=4, column=3) 

minus = Button(root, text=' - ', 
            command=lambda: sub(), height=1, width=7) 
minus.grid(row=5, column=3) 

multiply = Button(root, text=' * ',
                command=lambda: mult(), height=1, width=7) 
multiply.grid(row=6, column=3) 

divide = Button(root, text=' / ', 
                command=lambda: div(), height=1, width=7) 
divide.grid(row=7, column=3) 


root.mainloop()