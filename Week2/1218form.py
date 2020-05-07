import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as tkfont
import sys
import os

root = tk.Tk()
root.title("College Form")
time = tkfont.Font(family='sERIF', size=(int((root.winfo_screenwidth() / 100))))

Label(root, text="TERNA ENGINEERING COLLEGE", font=time, justify = tk.CENTER, padx = (int((root.winfo_screenwidth() / 2.5)))).grid(row=0,columnspan=100)
#Label.config(root, font=("Courier", 44))

def run():
    os.system('newwindow.py')

#_______________NAME_______________________________
Label(root, text="1.Enter your First Name:",pady=5, justify = tk.LEFT).grid(row=1,column=0)
e1 = ttk.Entry(root, justify = tk.LEFT).grid(row=1, column=1)
Label(root, text="Last Name:").grid(row=1,column=2)
e1 = ttk.Entry(root, justify = tk.LEFT).grid(row=1, column=3)


#__________________GENDER__________________________

q = tk.IntVar()
q.set(2)  # initializing the choice, i.e. Python

gender = [
    ("Female"),
    ("Male"),
    ("Other"),
]

#def ShowChoice():
#    print(v.get())

tk.Label(root, 
         text="2. Gender:",pady=5,
         justify = tk.LEFT).grid(row=2)

for val, language in enumerate(gender):
    tk.Radiobutton(root, 
                  text=language,variable=q, justify = tk.LEFT, 
#                  command=ShowChoice,
                  value=val).grid(row=2,column=(val+1))

#____________________DOB__________________________
Label(root, text="3. Enter Birth Day:", pady=5).grid(row=6,column=0)
e11 = ttk.Entry(root).grid(row=6, column=1)
Label(root, text="Month").grid(row=6,column=2)
e12 = ttk.Entry(root).grid(row=6, column=3)
Label(root, text="Year").grid(row=6,column=4)
e13 = ttk.Entry(root).grid(row=6, column=5)

#___________________EMAIL________________________
Label(root, text="4. Enter e-Mail:",pady=5).grid(row=7,column=0)
e21 = ttk.Entry(root).grid(row=7, column=1)

#_____________________PREVIOUS_COLLEGE___________
Label(root, text="5. Previous College Name:",pady=5).grid(row=8,column=0)
e31 = ttk.Entry(root).grid(row=8, column=1)

#________________DROPDOWN_MENU__________________

#root = Tk()


# Add a grid
mainframe = Frame(root)
mainframe.grid( sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.grid()

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { '--Choose from below--','Mumbai University','SNDT','SVKM','VJTI','IIT'}
tkvar.set('--Choose from below--') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="6. Degree completed in University:",pady=5).grid(row = 9,columnspan=3)
popupMenu.grid(row = 10,columnspan=3)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

#root.mainloop()

#________________RADIO_BUTTONS__________________

v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

payments = [
    ("Cash"),
    ("Cheque"),
    ("DD"),
    ("NEFT"),
    ("UPI")
]

#def ShowChoice():
#    print(v.get())

tk.Label(root, 
         text="7. Choose your mode of payment:",
         justify = tk.LEFT,
         padx = 5).grid(row=11)

for val, language in enumerate(payments):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 5, 
                  variable=v, justify = tk.LEFT, 
#                  command=ShowChoice,
                  value=val).grid(row=11,column=(val+1))


tk.Button(root, text='Submit', command=run).grid(row=12,column=5,sticky=tk.E, pady=4)
tk.Button(root, text='Exit', command=root.quit).grid(row=12,column=6,sticky=tk.E, pady=4)








#_______________fullscreen___________________

#w = Label(root, text="Hello, world!")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
#w.pack()
root.mainloop()