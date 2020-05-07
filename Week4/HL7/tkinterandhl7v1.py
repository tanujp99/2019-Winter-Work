import hl7
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as tkfont
import sys
import os


font_size = -14


# Global variable to remember if we are fullscreen or windowed
fullscreen = False

###############################################################################
# Functions

root = tk.Tk()
root.title("My Data")

time = tkfont.Font(family='sERIF', size=20)


# from hl7.xml import MSH
def programmm():
    data="D:\\WORK\\2019winterinternship\\Week4\\HL7\\dummydata.hl7"
    #Path of the HL7 file that is required to be processed
    save="D:\\WORK\\2019winterinternship\\Week4\\HL7\\savedata\\savefile2.txt"
    #Path where the savefile must be created

    # demo="C:\\Users\\tanuj\\Desktop\\demo2.txt"
    f = open(data,"r")
    # g = open(demo,"w+")
    g = open(save,"w+")
    # Go forward only if the file is readable:
    if f.mode == 'r':
        # load the contents of the read file
        contents =f.read()
        # divide the content derived into individual segments
        m= contents.split('\n')
        # Convert the segments individual elemnts into segments
        i=1
        message= m[0]
        for i in m:
            message+= i
            message+='\r'  
        # Parse the formatted data
        h = hl7.parse(message)

        # ---------Printing the patient-data-----------
        for j in range(0,len(h)) :
            if (h[j][0][0] == 'MSH'):
                lab = str(h[0][4])
                print("Laboratory where test conducted: ",h[0][4])
                g.write("Laboratory where test conducted: ")
                g.write(lab)
                g.write("\n")

            elif (h[j][0][0] == 'PID'):
                print("First Name: ",h[1][5][0][1][0])
                print("Last Name: ",h[1][5][0][0][0])
                g.write("First Name: ")
                fn = str(h[1][5][0][1][0])
                g.write(fn)
                g.write("\n")

                g.write("Last Name: ")
                ln = str(h[1][5][0][0][0])   
                g.write(ln)
                g.write("\n")

                # print("Middle Name: ",h[1][5][0][2][0])
        
                print("Date of Birth: ", h[1][7][0][0])
                print("Patient Age: ", h[1][7][0][1])
                g.write("Date of Birth: ")
                dob= str(h[1][7][0][0])
                g.write(dob)  
                g.write("\n")

                g.write("Patient Age: ") 
                age = str(h[1][7][0][1])
                g.write(age)   
                g.write("\n")

        
                # Print patient gender
                if h[1][8][0][0] == 'M':
                    gender = 'Male'
                else:
                    gender = 'Female'    
                print("Gender:", gender)

                print("Notes: ",h[1][11][0][0],h[1][11][0][1],h[1][11][0][2],h[1][11][0][3])
                g.write("Gender:")
                g.write(gender)
                g.write("\n")

                g.write("Notes: ")
                note1 = str(h[1][11][0][3])
                note2 = str(h[1][11][0][2])
                note3 = str(h[1][11][0][1])
                note4 = str(h[1][11][0][0])
                g.write(note4)
                g.write(note3)
                g.write(note2)
                g.write(note1)
                g.write("\n")

            elif (h[j][0][0] == 'NTE'):
                g.write("Comments: ")
                comment = str(h[j][3][0])
                g.write(comment)
                g.write("\n")
         
            elif (h[j][0][0] == 'ADD'):
                g.write("\n")                
                g.write("Condition: ")
                condition = str(h[j][1][0])
                g.write(condition)
                # g.write("\n")                
                        
            elif (h[j][0][0] == 'OBR'):
                g.write("\n")                
                g.write("\n")                
                g.write("Report: ")
                report = str(h[j][4][0][0])
                g.write(report)
                g.write("\n")                
                g.write("Header: ")
                header = str(h[j][4][0][1])            
                g.write(header)
                g.write("\n") 
                g.write("\n") 

            elif (h[j][0][0] == 'OBX'):              
                # g.write("Report: ")
           
                # g.write("Header: ")
                val = str(h[j][5][0][0])            
                nunit = str(h[j][6]) 
                nrange = str(h[j][7]) 
                parameter = str(h[j][3][0][1])
                g.write("Parameter: ") 
                g.write(parameter) 
                g.write("\n")                               
                g.write("Value    : ")
                g.write(val)
                g.write(" ")                 
                g.write(nunit)
                g.write("\n")                 
                g.write("Normal   : ")
                g.write(nrange)
                g.write("\n")                 
                g.write("\n")                 

            elif (h[j][0][0] == 'FTS'):   
                fend = str(h[j][2])
                g.write("\n")                 
                g.write("\n")                 
                g.write(fend)                 


            # print(h[j][0])
            # else:
                # print("---segment not found---")

    g.close



# def runprev():
#     runcode = "D:\\WORK\\2019winterinternship\\Week3\\handlinghl7fordummydata.py"
#     os.system(runcode)

def runnext():
    
    path = 'D:\\WORK\\2019winterinternship\\Week4\\HL7\\savedata'
    # Path of the parent folder where the savefile is created
    flist = os.listdir(path)
    # flist = os.listdir()
    
    lbox = tk.Listbox(root)
    lbox.grid(row=1,columnspan=100)
    
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
        
    # def opensystem():
    #     x = lbox.curselection()[0]
    #     os.system(lbox.get(x))
 
 
 
    text = tk.Text(root)
    text.grid()
    
    lbox.bind("<<ListboxSelect>>", showcontent)
    # lbox.bind("<Double-Button-1>", opensystem)
# BUTTON


def main():


    # tk.Label(root, text="WELCOME TO TERNA ENGINEERING COLLEGE",font=time, justify = tk.CENTER,pady = (int((root.winfo_screenheight() / 2.5))), padx = (int((root.winfo_screenwidth() / 3)))).grid(row=0,columnspan=100)

    #button_quit = tk.Button(root, 
    #                        text="Quit",  
    #                        command=root.destroy,
    #                        borderwidth=0,
    #                        highlightthickness=0, 
    #                        fg='gray10',
    #                        bg='black').grid(column=1)

    # Lay out widgets in a grid in the frame

    tk.Button(root, text='Run Program', command=programmm).grid(row=12,column=96,sticky=tk.E, pady=4)
    tk.Button(root, text='Show file', command=runnext).grid(row=12,column=97,sticky=tk.E, pady=4)
    tk.Button(root, text='Exit', command=root.quit).grid(row=12,column=98,sticky=tk.E, pady=4)



    # Start in fullscreen mode and run
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()  # <-- move focus to this widget
    root.bind("<Escape>", lambda e: e.widget.quit())
    root.mainloop()


if __name__ == "__main__":
    main()