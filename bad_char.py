from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
from pandastable import Table, TableModel

def bad_character(display_frame):
        # ======> Button Style
        btn_style = ttk.Style()
        btn_style.theme_use('vista')
        btn_style.configure('TButton',width=15, height =10,font=('Arial 12 bold'),wraplength=100,foreground="red")

        # ===> layout
        w = 700
        h = 100
        m = 20
        layout_bg = "#629c80"
        part_0 = Frame(display_frame, width=600,height=70,bg= layout_bg)
        part_1 = Frame(display_frame, width=w,height=50,bg= layout_bg)
        part_2 = Frame(display_frame, width=w,height=80,bg= layout_bg)
        part_3 = Frame(display_frame, width=w,height=80,bg= layout_bg)
        part_4 = Frame(display_frame, width=w,height=80,bg= layout_bg)
        part_5 = Frame(display_frame, width=w,height=260,bg= layout_bg)

        part_0.pack()
        part_1.place(x=m,y=h)
        part_2.place(x=m,y=h*1.75)
        part_3.place(x=m,y=h*2.2)
        part_4.place(x=m,y=h*3.2)
        part_5.place(x=m,y=h*4.2)

        # ===> Title
        page_title= Label(part_0, text="Bad Characters",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        sub_seqLabel = ttk.Label(part_1, text="Enter Sub Sequence:",font=("Arial 14 bold"),background=layout_bg)
        sub_seqLabel.place(x=20,y=10)
        entry_sub_seq = ttk.Entry(part_1,width=40,font=('Arial',14))
        entry_sub_seq.place(x=230,y=10)

        upload_label_seq = Label(part_2, text="Choose File:",font=('Arial 12 bold'),background=layout_bg)
        upload_btn_seq = ttk.Button(part_2, text="Upload File",cursor="hand2",width=10)
        file_name_seq = Label(part_2,text = "File Explorer path",font=('Arial 10 bold'),foreground="blue",background=layout_bg)
        upload_label_seq.place(x=10,y=10)
        upload_btn_seq.place(x=120,y=10)
        file_name_seq.place(x=220,y=10)

        bad_char_result_btn = ttk.Button(part_3,text="\nView Result\n",cursor="hand2")
        bad_char_result_btn.place(x=550,y=10)


        indx_match = ttk.Label(part_4, text="",font=("Arial 14 bold"),background=layout_bg)
        indx_match.pack()

        table_match = ttk.Label(part_5, text="",font=("Arial 14 bold"),background=layout_bg)
        table_match.pack()

        bad_char_result_btn.config(command= lambda: result_sub_seq_btn(extract_seq(file_name_seq.cget("text")).upper(),entry_sub_seq.get()))
        # bad_char_result_btn.config(command= lambda: result_sub_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
        upload_btn_seq.config(command= lambda: uploadFiles())
    # =============== Button Function ===========================
        def result_sub_seq_btn(seq, sub_seq):
            res, table ,rows = Badchars(seq, sub_seq)
            indx_match.configure(text="Index of Matching: "+str(res)+"\n")
            cols = return_cols(sub_seq)

        def uploadFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
                title = "Select a File",
                filetypes = (("Text files",
                "*.txt*"),
                ("all files","*.*")))
            file_name_seq.configure(text=filename)
            return filename

        def extract_seq(filename):
            file=open(filename)
            l=[i for i in file]
            s=l[1][:-1]
            return s
        
        
        def return_cols(sub_seq):
            col = []
            col[:0] = sub_seq
            return col
        # =============== Bio Computing Function ===========================

        def Badchars(seq,sub_seq):
            table=np.zeros([4,len(sub_seq)])
            row=["A","C","G","T"]
            for i in range (4):
                num=-1
                for j in range (len(sub_seq)):
                    if row[i]==sub_seq[j]:
                        table[i,j]=-1
                        num=-1
                    else:
                        num+=1
                        table[i,j]=num
            x=-1
            i=0
            while(i<len(seq)-len(sub_seq)+1):
                if sub_seq==seq[i:i+len(sub_seq)]:
                    x=i
                
                else:
                    for j in range(len(sub_seq)-1,-1,-1):
                        if seq[i+j] != sub_seq[j]:
                            k=row.index(seq[i+j])
                            i+=table[k,j]
                            break
                        
                i=int(i+1)
                    
            return x , table, row

            
