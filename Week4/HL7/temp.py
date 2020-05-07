
import tkinter as tk
import os
 
# WINDOW CREATION
win = tk.Tk()
geo = win.geometry
geo("400x400+400+400")
win['bg'] = 'orange'
 
# get the list of files
path = 'D:\\WORK\\PF\\VSC\\HL7\\savedata'
flist = os.listdir(path)

lbox = tk.Listbox(win)
lbox.pack()
 
# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)
 
 
def showcontent(event):
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(path+ "\\"+ file) as file:
        file = file.read()
    text.delete('1.0', tk.END)
    text.insert(tk.END, file)
 
 
text = tk.Text(win, bg='cyan')
text.pack()
 
lbox.bind("<<ListboxSelect>>", showcontent)
 
win.mainloop()