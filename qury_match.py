from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import bisect
from pandastable import Table, TableModel

def qury(display_frame):
        # ======> Button Style
        btn_style = ttk.Style()
        btn_style.theme_use('vista')
        btn_style.configure('TButton',width=15, height =10,font=('Arial 12 bold'),wraplength=100,foreground="red")

        # ===> layout
        w = 650
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
        page_title= Label(part_0, text="Quray Match Index",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        sub_seqLabel = ttk.Label(part_1, text="Enter Sub Sequence:",font=("Arial 14 bold"),background=layout_bg)
        sub_seqLabel.place(x=10,y=10)
        entry_sub_seq = ttk.Entry(part_1,width=20,font=('Arial',14))
        entry_sub_seq.place(x=230,y=10)
        
        k_Label = ttk.Label(part_1, text="Enter K:",font=("Arial 14 bold"),background=layout_bg)
        k_Label.place(x=490,y=10)
        entry_k = ttk.Entry(part_1,width=5,font=('Arial',14))
        entry_k.place(x=580,y=10)

        upload_label_seq = Label(part_2, text="Choose File:",font=('Arial 12 bold'),background=layout_bg)
        upload_btn_seq = ttk.Button(part_2, text="Upload File",cursor="hand2",width=10)
        file_name_seq = Label(part_2,text = "File Explorer path",font=('Arial 10 bold'),foreground="blue",background=layout_bg)
        upload_label_seq.place(x=10,y=10)
        upload_btn_seq.place(x=120,y=10)
        file_name_seq.place(x=220,y=10)

        qry_match_result_btn = ttk.Button(part_3,text="\nView Result\n",cursor="hand2")
        qry_match_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_4, text="",font=("Arial 14 bold"),background=layout_bg)
        indx_match.pack()

        table_match = ttk.Label(part_5, text="",font=("Arial 14 bold"),background=layout_bg)
        table_match.pack()

        qry_match_result_btn.config(command= lambda: result_sub_seq_btn(extract_seq(file_name_seq.cget("text")).upper(),entry_sub_seq.get(),entry_k.get()))
        # qry_match_result_btn.config(command= lambda: result_sub_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
        upload_btn_seq.config(command= lambda: uploadFiles())
    # =============== Button Function ===========================
        def result_sub_seq_btn(seq, sub_seq,k):
            index = IndexSorted(seq,3)
            res = query(seq,sub_seq,index)
            indx_match.configure(text="Index of Matching: "+str(res)+"\n")


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
        
        # =============== Bio Computing Function ===========================

        def IndexSorted(seq,k):
            index = []
            for i in range(len(seq)-k+1):
                index.append((seq[i:i+k], i))
            index.sort() 
            return index

        def query(t,p,index):
            keys = [r[0] for r in index]
            st = bisect.bisect_left(keys,p[:len(keys[0])])
            en = bisect.bisect(keys,p[:len(keys[0])])
            hits = index[st:en] 
            l=[h[1] for h in hits ]
            offsets=[]
            for i in l:
                if t[i:i+len(p)]==p:
                    offsets.append(i)
            return offsets