import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as tkfont
import sys
import os
###############################################################################
# Parameters and global variables

def runprev():
    os.system('newwindow.py')


# Default font size
font_size = -14


# Global variable to remember if we are fullscreen or windowed
fullscreen = False

###############################################################################
# Functions


# Create the main window
root = tk.Tk()
root.title("My Clock")

time = tkfont.Font(family='sERIF', size=20)

tk.Label(root, text="This is a New window !",font=time, justify = tk.CENTER,pady = (int((root.winfo_screenheight() / 2.5))), padx = (int((root.winfo_screenwidth() / 2.5)))).grid(row=0,columnspan=100)


# Lay out widgets in a grid in the frame


tk.Button(root, text='Previous', command=runprev).grid(row=12,column=97,sticky=tk.E, pady=4)
tk.Button(root, text='Exit', command=root.quit).grid(row=12,column=98,sticky=tk.E, pady=4)


# Start in fullscreen mode and run
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.focus_set()  # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()