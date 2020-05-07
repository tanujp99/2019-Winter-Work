import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as tkFont
###############################################################################
# Parameters and global variables

# Default font size
font_size = 9
#my_font= ("Ariel", 9)


# Global variable to remember if we are fullscreen or windowed
fullscreen = False

###############################################################################
# Functions

# Toggle fullscreen
def toggle_fullscreen(event=None):

    global root
    global fullscreen

    # Toggle between fullscreen and windowed modes
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    resize()

# Return to windowed mode
def end_fullscreen(event=None):

    global root
    global fullscreen

    # Turn off fullscreen mode
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize()

# Automatically resize font size based on window size
def form():
    tk.Label(frame, font=my_font, text="First Name").grid(row=0, sticky="nsew")
    tk.Label(frame, font=my_font, text="Last Name").grid(row=1, sticky="nsew")
    tk.Label(frame, font=my_font, text="e-Mail").grid(row=2, sticky="nsew")
    tk.Label(frame, font=my_font, text="Phone Number").grid(row=3, sticky="nsew")

    e1 = ttk.Entry(frame)
    e2 = ttk.Entry(frame)
    e3 = ttk.Entry(frame)
    e4 = ttk.Entry(frame)

    e1.grid(row=0, column=1, sticky="W",ipady=4,ipadx=14)
    e2.grid(row=1, column=1, sticky="W",ipady=4,ipadx=14)
    e3.grid(row=2, column=1, sticky="W",ipady=4,ipadx=14)
    e4.grid(row=3, column=1, sticky="W",ipady=4,ipadx=14)

    tk.Button(frame, text='Exit', command=frame.quit).grid(row=5, column=0, sticky=tk.E, pady=4)

def resize(event=None):

    global my_font
    global button_dfont
    global frame

    # Resize font based on frame height (minimum size of 12)
    # Use negative number for "pixels" instead of "points"
    new_size = -max(12, int((frame.winfo_height() / 5)))
    my_font.configure(size=new_size)
    new_size = -max(12, int((frame.winfo_height() / 30)))
    button_dfont.configure(size=new_size)


# Create the main window
root = tk.Tk()
root.title("My Clock")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container (expand to fit window)
frame.pack(fill=tk.BOTH, expand=0)
#frame.pack()

# Create dynamic font for text
my_font = tkFont.Font(family='sERIF', size=font_size)
button_dfont = tkFont.Font(size=font_size)

# Create widgets
form()


# Make it so that the grid cells expand out to fill window
frame.rowconfigure(0, weight=10)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)

# Bind F11 to toggle fullscreen and ESC to end fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

# Have the resize() function be called every time the window is resized
root.bind('<Configure>', resize)



# Start in fullscreen mode and run
toggle_fullscreen()
root.mainloop()
