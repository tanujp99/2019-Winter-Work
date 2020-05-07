import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as tkfont
import sys
import os
###############################################################################
# Parameters and global variables

# Default font size
font_size = -14


# Global variable to remember if we are fullscreen or windowed
fullscreen = False

###############################################################################
# Functions

root = tk.Tk()
root.title("My Clock")

time = tkfont.Font(family='sERIF', size=20)

def runprev():
    os.system('1218form.py')

def runnext():
    os.system('college.py')

#_______________NAME_______________________________
# Create the main window


tk.Label(root, text="WELCOME TO TERNA ENGINEERING COLLEGE",font=time, justify = tk.CENTER,pady = (int((root.winfo_screenheight() / 2.5))), padx = (int((root.winfo_screenwidth() / 3)))).grid(row=0,columnspan=100)

#button_quit = tk.Button(root, 
#                        text="Quit",  
#                        command=root.destroy,
#      
#                   borderwidth=0,
#                        highlightthickness=0, 
#                        fg='gray10',
#                        bg='black').grid(column=1)

# Lay out widgets in a grid in the frame

tk.Button(root, text='Previous', command=runprev).grid(row=12,column=96,sticky=tk.E, pady=4)
tk.Button(root, text='Next', command=runnext).grid(row=12,column=97,sticky=tk.E, pady=4)
tk.Button(root, text='Exit', command=root.quit).grid(row=12,column=98,sticky=tk.E, pady=4)


# Start in fullscreen mode and run
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()