from tkinter import *
root = Tk()


# position screen in window
# root.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
# root.screen.configure(state='normal')

# initialize screen value as empty
root.equation = ''

# create buttons using method createButton
b1 =  createButton(7)
b2 = createButton(8)
b3 = createButton(9)
b4 = createButton(u"C",None)
b5 = createButton(4)
b6 = createButton(5)
b7 = createButton(6)
b8 = createButton(u"\u00F7")
b9 = createButton(1)
b10 =createButton(2)
b11 =createButton(3)
b12 =createButton('*')
b13 =createButton('.')
b14 = createButton(0)
b15 = createButton('+')
b16 = createButton('-')
b17 = createButton('=',None,34)

# buttons stored in list
buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]

# intialize counter
count = 0
# arrange buttons with grid manager
for row in range(1,5):
    for column in range(4):
        buttons[count].grid(row=row,column=column)
        count += 1
# arrange last button '=' at the bottom
buttons[16].grid(row=5,column=0,columnspan=4)

def createButton(root, val,write=True,width=7):
    # this function creates a button, and takes one compulsory argument, the value that should be on the button

    return Button(root.master, text=val,command = lambda: root.click(val,write), width=width)


root.mainloop()
