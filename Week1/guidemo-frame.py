
from tkinter import *
  
root = Tk() 
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'Red', fg ='red', bg = 'white') 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Brown', fg='brown', bg = 'white') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='blue', bg = 'white') 
bluebutton.pack( side = LEFT ) 
blackbutton = Button(bottomframe, text ='Black', fg ='black', bg = 'white') 
blackbutton.pack( side = BOTTOM) 
root.mainloop()