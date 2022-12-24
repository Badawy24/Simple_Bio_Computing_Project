from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import bisect
from pandastable import Table, TableModel
from itertools import permutations


def ovr_lab(display_frame):
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
        part_1 = Frame(display_frame, width=w,height=100,bg= layout_bg)
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
        page_title= Label(part_0, text="Over Lab",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seq_Label = ttk.Label(part_1, text="Enter Sequence Separated ' - ':",font=("Arial 14 bold"),background=layout_bg)
        seq_Label.place(x=10,y=10)
        entry_seq = ttk.Entry(part_1,width=25,font=('Arial',14))
        entry_seq.place(x=300,y=10)
        
        hint = ttk.Label(part_1, text="Ex: ACGGTA-GGTACC-GCATACG",font=("Arial 11 bold"),background=layout_bg,foreground="red")
        hint.place(x=10,y=40)

        k_Label = ttk.Label(part_2, text="Enter K:",font=("Arial 14 bold"),background=layout_bg)
        k_Label.place(x=10,y=10)
        entry_k = ttk.Entry(part_2,width=5,font=('Arial',14))
        entry_k.place(x=110,y=10)

        ovr_lab_result_btn = ttk.Button(part_3,text="\nView Result\n",cursor="hand2")
        ovr_lab_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_4, text="",font=("Arial 14 bold"),background=layout_bg,wraplength=600)
        indx_match.pack()

        ovr_lab_result_btn.config(command= lambda: result_seq_btn(convert_seq_list(entry_seq.get()),int(entry_k.get())))
        # ovr_lab_result_btn.config(command= lambda: result_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
    # =============== Button Function ===========================
        def result_seq_btn(seq,k):
            res = native_overlap(seq,k)
            # res = query(seq,seq,index)
            indx_match.configure(text=res)
            # print("ok")


        def convert_seq_list(seq):
            lst = seq.split("-")
            # print(lst)
            return lst
        
        # =============== Bio Computing Function ===========================

        def overlap(a, b, min_length=3):
            start=0
            while True:
                start=a.find(b[:min_length], start)
                if start == -1:
                    return 0
                if b.startswith(a[start:]):
                    return len(a)-start
                start += 1
                    
        def native_overlap(reads, k):
            olap={}
            for a,b in permutations(reads, 2):
                olen=overlap(a, b, k)
                if olen > 0:
                    olap[(a, b)]=olen
            return olap
