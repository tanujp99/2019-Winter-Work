import hl7
from tkinter import *
import sys
import os

# from hl7.xml import MSH
def main():    
    root = Tk()
    #demo="C:\\Users\\tanuj\\Desktop\\demo2.txt"
    data="D:\\WORK\\2019winterinternship\\Week4\\HL7\\dummydata.hl7"
    f = open(data,"r")
    #g = open(demo,"w+")
    g = open("ddddd.txt", "w+")
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

        # tk.Button(root, text='Exit', command=root.quit).grid(row=12,column=98,sticky=tk.E, pady=4)


    # root = Tk()

    # with open(demo, "r") as e:
    #     Label(root, text=e.read()).place(x=0,y=0)

    #     #         # Start in fullscreen mode and run
    # root.overrideredirect(True)
    # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))    
    # root.focus_set()  # <-- move focus to this widget
    # root.bind("<Escape>", lambda e: e.widget.quit())
    # #w.pack()
    # root.mainloop()

            # print(h[j][0])
            # else:
                # print("---segment not found---")

    # g.close
if __name__ == "__main__":
    main()