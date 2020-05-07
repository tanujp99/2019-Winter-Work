from tkinter import *

root = Tk()

root.title("Python Calculator")

# create screen widget
s1 = root.screen = Text(state='disabled', width=30, height=1.5)
# position screen in window
s1.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
s1.configure(state='normal')
root.equation = ''

# create screen widget
s2 = root.screen = Text(state='disabled', width=30, height=1.5)
# position screen in window
s2.grid(row=1,column=0,columnspan=4,padx=5,pady=5)
s2.configure(state='normal')


# initialize screen value as empty
root.equation = ''

# create buttons using method createButton
b1 =  root.createButton(7)
b2 = root.createButton(8)
b3 = root.createButton(9)
b4 = root.createButton(u"C",None)
b5 = root.createButton(4)
b6 = root.createButton(5)
b7 = root.createButton(6)
b8 = root.createButton(u"\u00F7")
b9 = root.createButton(1)
b10 = root.createButton(2)
b11 = root.createButton(3)
b12 = root.createButton('*')
b13 = root.createButton('.')
b14 = root.createButton(0)
b15 = root.createButton('+')
b16 = root.createButton('-')
b17 = root.createButton('=',None,34)

# buttons stored in list
buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]

# intialize counter
count = 0
# arrange buttons with grid manager
for row in range(2,6):
    for column in range(4):
        buttons[count].grid(row=row,column=column)
        count += 1
# arrange last button '=' at the bottom
buttons[16].grid(row=6,column=0,columnspan=4)

s3 = root.screen = Text( state='disabled', width=30, height=1.5)
# position screen in window
s3.grid(row=7,column=0,columnspan=4,padx=5,pady=5)
s3.configure(state='normal')
root.equation = ''



def createButton(val,write=True,width=7):
    # this function creates a button, and takes one compulsory argument, the value that should be on the button

    return Button(root.master, text=val,command = lambda: root.click(val,write), width=width)   
def click(root,text,write):
    # this function handles what happens when you click a button
    # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
    if write == None:

        #only evaluate code when there is an equation to be evaluated
        if text == '=' and root.equation: 
            # replace the unicode value of division ./.with python division symbol / using regex
            root.equation= re.sub(u"\u00F7", '/', root.equation)
            print(root.equation)
            answer = str(eval(root.equation))
            # root.clear_screen()
            root.insert_screen3(answer,newline=True)
        elif text == u"C":
            root.clear_screen()
        
        
    else:
        # add text to screen
        root.insert_screen(text)
    

def clear_screen(root):
    #to clear screen
    #set equation to empty before deleting screen
    root.equation = ''
    root.screen.configure(state='normal')
    root.screen.delete('1.0', END)

def insert_screen1(root, value,newline=False):
    root.screen.configure(state='normal')
    root.screen.insert(END,value)
    # record every value inserted in screen
    root.equation += str(value)
    root.screen.configure(state ='disabled')
def insert_screen2(root, value,newline=False):
    root.screen.configure(state='normal')
    root.screen.insert(END,value)
    # record every value inserted in screen
    root.equation += str(value)
    root.screen.configure(state ='disabled')
def insert_screen3(root, value,newline=False):
    root.screen.configure(state='normal')
    root.screen.insert(END,value)
    # record every value inserted in screen
    root.equation += str(value)
    root.screen.configure(state ='disabled')                



root.mainloop()