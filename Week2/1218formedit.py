import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont

root = tk.Tk()
root.title("College Form")
time = tkfont.Font(family='sERIF', size=30)

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class page1(Page):
    Label(root, text="TERNA ENGINEERING COLLEGE", font=time, justify = tk.CENTER, padx = (int((root.winfo_screenwidth() / 3)))).grid(row=0,columnspan=100)
#Label.config(root, font=("Courier", 44))
#def page1():
#def page2():

#_______________NAME_______________________________
    a1=Label(root, text="1.Enter your First Name:",pady=20, justify = tk.LEFT).grid(row=1,column=0)
    a2=e1 = ttk.Entry(root, justify = tk.LEFT).grid(row=1, column=1)
    a3=Label(root, text="Last Name:").grid(row=1,column=2)
    a4=e1 = ttk.Entry(root, justify = tk.LEFT).grid(row=1, column=3)
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
    a5=tk.Label(root, 
         text="2. Gender:",pady=20,
         justify = tk.LEFT).grid(row=2)

    for val, language in enumerate(gender):
        a6=tk.Radiobutton(root, 
                  text=language,variable=q, justify = tk.LEFT, 
#                  command=ShowChoice,
                  value=val).grid(row=2,column=(val+1))

#____________________DOB__________________________
    Label(root, text="3. Enter Birth Day:", pady=20).grid(row=6,column=0)
    e11 = ttk.Entry(root).grid(row=6, column=1)
    Label(root, text="Month").grid(row=6,column=2)
    e12 = ttk.Entry(root).grid(row=6, column=3)
    Label(root, text="Year").grid(row=6,column=4)
    e13 = ttk.Entry(root).grid(row=6, column=5)

#___________________EMAIL________________________
    Label(root, text="4. Enter e-Mail:",pady=20).grid(row=7,column=0)
    e21 = ttk.Entry(root).grid(row=7, column=1)

#_____________________PREVIOUS_COLLEGE___________
    Label(root, text="5. Previous College Name:",pady=20).grid(row=8,column=0)
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
    Label(mainframe, text="6. Degree completed in University:",pady=20).grid(row = 9,columnspan=3)
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
         padx = 20).grid()
    for val, language in enumerate(payments):
        tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, justify = tk.LEFT, 
#                  command=ShowChoice,
                  value=val).grid()
#_______________fullscreen___________________
#w = Label(root, text="Hello, world!")

if __name__ == "__main__":
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()  # <-- move focus to this widget
    root.bind("<Escape>", lambda e: e.widget.quit())
#w.pack()
    root.mainloop()