import tkinter as tk 
r = tk.Tk() 
r.title('General Window Opened') 
button = tk.Button(r, text='Close this window', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 