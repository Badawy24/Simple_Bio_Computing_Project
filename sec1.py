# ==========================================================
# ============= Import =====================================
from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
import pandas as pd
import random
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# =========== Main Window ==================================
class ConvertFasta2CSV:
    def __init__(self,Sec1frame):

        # =============== View Type 1 ==========================

        fileName = ttk.Label(Sec1frame, text="Enter Fasta File Without Extension")
        fileName.grid(row=0, column=0, padx=10, pady=10)
        entryFileName = ttk.Entry(Sec1frame,width=30,font=('Arial',12))
        entryFileName.grid(row=0, column=1, columnspan=2, pady=10)
        # ==========

        spilt = ttk.Label(Sec1frame, text="Enter Split Character")
        spilt.grid(row=1, column=0, padx=10, pady=10)
        splitChar = ttk.Entry(Sec1frame,width=30,font=('Arial',12))
        splitChar.grid(row=1, column=1, columnspan=2, pady=10)

        # =================
        # Type 1 
        Type1 = ttk.Label(Sec1frame, text="Display Type Of Sequence",font=("Arial 15 bold "),foreground="Blue")
        Type1.grid(row=3, column=0, padx=5, pady=10)

        btnEX = ttk.Button(Sec1frame,text="Review Data")
        btnEX.grid(row=4,column=0,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
        btnEX.config(command= lambda: self.view_btn(entryFileName.get(),splitChar.get()))

        btnCSV = ttk.Button(Sec1frame,text="Convert To CSV File")
        btnCSV.grid(row=4,column=1,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
        btnCSV.config(command= lambda: self.fas2csv_btn(entryFileName.get(),splitChar.get()))

        # =============== View Type 2 ===========================
        lineSplite = ttk.Label(Sec1frame, text="--------------------------------------------")
        lineSplite.grid(row=5, column=0, padx=5, pady=10)


        Type2 = ttk.Label(Sec1frame, text="Display ID OF Sequence ",font=("Arial 15 bold "),foreground="Blue")
        Type2.grid(row=6, column=0, padx=5, pady=10)

        btnEX = ttk.Button(Sec1frame,text="Review Data")
        btnEX.grid(row=7,column=0,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
        btnEX.config(command= lambda: self.view_btn_T2(entryFileName.get()))

        btnCSV = ttk.Button(Sec1frame,text="Convert To CSV File")
        btnCSV.grid(row=7,column=1,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
        btnCSV.config(command= lambda: self.fas2csv_btn_T2(entryFileName.get()))

    # =============== Button Function ===========================
    def view_btn(self,file_name,spilt_char):   # Type 1
        self.view_data(file_name,spilt_char,"Sequence","Hemolytic",1)

    def fas2csv_btn(self,file_name,spilt_char):   # Type 1
        self.convert2csv(file_name,spilt_char,"Sequence","Hemolytic",1)
    
    def view_btn_T2(self,file_name):   # Type 2
        self.view_data(file_name,"","ID","Sequence",2)

    def fas2csv_btn_T2(self,file_name):   # Type 2
        self.convert2csv(file_name,"","ID","Sequence",2)
    # =============== Button Function ===========================

    def extract_data(self, file_name,spilt_char): # FUnction to Extract Data From File [Type 1 ]
        infile = open(file_name+'.fasta')
        flag=0
        lst=[]
        for line in infile:
            if flag==0:
                s=line.split(spilt_char)
                # print(s[3])
                flag=1
            else:
                # print(line[:-1])
                flag=0
                if s[3]=='non-hemolytic' or s[3]=='non-hemolytic\n':
                    lst.append([line[:-1],0])
                else:
                    lst.append([line[:-1],1])
        return lst
    
    def orderSeq(self,file_name):   # Function TO Extract Data From File With ID [Type 2 ]
        infile = open(file_name+'.fasta')
        tb=[]
        for line in infile:
            if line[0]==">":
                x=line[1:-1]
            else:
                seq=line[:-1]
                tb.append([x,seq])
        return tb
    
    def view_data(self,file_name,spilt_char,head1,head2,type_fun):  # Functio to Display Data In Table 
            lst = []
            w = 0
            if type_fun == 1:
                lst = self.extract_data(file_name,spilt_char)
                w = 50
            elif type_fun == 2:
                lst = self.orderSeq(file_name)
                w = 30

        # Display Table Of Some Data  
            newWindow = Toplevel(Sec1frame)
            newWindow.title("Review Data")
            newWindow.geometry("600x600")
            total_columns = len(lst[0])

            # Head Of Table
            h1 = Entry(newWindow,width =w,fg="red",font=('Arial',10,'bold'))
            h1.grid(row=0, column=0)
            h1.insert(END, head1)
            h2 = Entry(newWindow,width =w,fg="red",font=('Arial',10,'bold'))
            h2.grid(row=0, column=1)
            h2.insert(END, head2)

            for i in range(25):
                for j in range(total_columns):
                    e = Entry(newWindow,width= w,font=('Arial',10,'bold'))
                    e.grid(row=i+1, column=j)
                    e.insert(END, lst[i][j])

    def convert2csv(self,file_name,spilt_char,head1,head2,type_fun): # function To Extract CSV File
        head=[head1,head2]
        lst = []
        if type_fun == 1:
            lst = self.extract_data(file_name,spilt_char)
        elif type_fun == 2:
            lst = self.orderSeq(file_name)
        df=pd.DataFrame(lst,columns=head)
        df.to_csv(file_name+str(random.randint(1,50))+".csv")

    
Sec1frame = Tk() # To make Window Which Hold Layout
Sec1frame.title("Convert Fasta File To CSV")
Sec1frame.geometry("800x600") # Re-size Window
Sec1frame.resizable(False,False) 
t = ConvertFasta2CSV(Sec1frame)
Sec1frame.mainloop()