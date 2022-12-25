from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import bisect
from pandastable import Table, TableModel
from itertools import permutations


def fibo_index(display_frame):
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
        part_3 = Frame(display_frame, width=w,height=260,bg= layout_bg)

        part_0.pack()
        part_1.place(x=m,y=h)
        part_2.place(x=m,y=h*1.75)
        part_3.place(x=m,y=h*3.2)


        # ===> Title
        page_title= Label(part_0, text="Fibonacci Number",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seq_Label = ttk.Label(part_1, text="Enter Fibonacci Index :",font=("Arial 14 bold"),background=layout_bg)
        seq_Label.place(x=10,y=10)
        entry_num = ttk.Entry(part_1,width=5,font=('Arial',14))
        entry_num.place(x=250,y=10)


        fibo_result_btn = ttk.Button(part_2,text="\nView Result\n",cursor="hand2")
        fibo_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_3, text="",font=("Arial 14 bold"),background=layout_bg,wraplength=600)
        indx_match.pack()

        fibo_result_btn.config(command= lambda: result_seq_btn(int(entry_num.get())))
        # fibo_result_btn.config(command= lambda: result_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
    # =============== Button Function ===========================
        def result_seq_btn(num):
            res = fib(num)
            # res = query(seq,seq,index)
            indx_match.configure(text="Fibonacci Number: {}".format(res))
            # print("ok")

        # =============== Bio Computing Function ===========================

        def fib(num):
            if (num < 0) :
                return ("invalid input")
            elif (num == 0):
                return (0)
            elif (num==1 or num==2):
                return (1)
            else :
                return (fib(num-1)+fib(num-2))