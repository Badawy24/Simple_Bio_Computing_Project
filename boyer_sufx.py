from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import bisect
from pandastable import Table, TableModel
from itertools import permutations


def boyr_sufix(display_frame):
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
        page_title= Label(part_0, text="Boyer Suffix",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seq_Label = ttk.Label(part_1, text="Enter Sequence :",font=("Arial 14 bold"),background=layout_bg)
        seq_Label.place(x=10,y=10)
        entry_seq = ttk.Entry(part_1,width=40,font=('Arial',14))
        entry_seq.place(x=200,y=10)

        sub_seq_Label = ttk.Label(part_2, text="Enter pattern:",font=("Arial 14 bold"),background=layout_bg)
        sub_seq_Label.place(x=10,y=10)
        entry_sub_seq = ttk.Entry(part_2,width=40,font=('Arial',14))
        entry_sub_seq.place(x=200,y=10)

        boyr_result_btn = ttk.Button(part_3,text="\nView Result\n",cursor="hand2")
        boyr_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_4, text="",font=("Arial 14 bold"),background=layout_bg,wraplength=600)
        indx_match.pack()

        boyr_result_btn.config(command= lambda: result_seq_btn(entry_seq.get(),entry_sub_seq.get()))
        # boyr_result_btn.config(command= lambda: result_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
    # =============== Button Function ===========================
        def result_seq_btn(seq,sub_seq):
            shifts = search(seq, sub_seq)
            # res = query(seq,seq,index)
            indx_match.configure(text="pattern occurs at shift in {}".format(shifts))
            # print("ok")


        def convert_seq_list(seq):
            lst = seq.split("-")
            # print(lst)
            return lst
        
        # =============== Bio Computing Function ===========================

        def preprocess_strong_suffix(shift, bpos, pat, m):

            # m is the length of pattern
            i = m
            j = m + 1
            bpos[i] = j

            while i > 0:

                while j <= m and pat[i - 1] != pat[j - 1]:
                    
                    
                    if shift[j] == 0:
                        shift[j] = j - i

                    # Update the position of next border
                    j = bpos[j]
                    
                
                i -= 1
                j -= 1
                bpos[i] = j

        # Preprocessing for case 2
        def preprocess_case2(shift, bpos, pat, m):
            j = bpos[0]
            for i in range(m + 1):
                
                
                if shift[i] == 0:
                    shift[i] = j
                    
                
                if i == j:
                    j = bpos[j]


        def search(text, pat):

            # s is shift of the pattern with respect to text
            s = 0
            m = len(pat)
            n = len(text)

            bpos = [0] * (m + 1)

            # initialize all occurrence of shift to 0
            shift = [0] * (m + 1)

            # do preprocessing
            preprocess_strong_suffix(shift, bpos, pat, m)
            preprocess_case2(shift, bpos, pat, m)
            shifts = []
            while s <= n - m:
                j = m - 1
                
                while j >= 0 and pat[j] == text[s + j]:
                    j -= 1
                
                if j < 0:
                    shifts.append(s)
                    s += shift[0]
                else:
                    
                    
                    s += shift[j + 1]
            print(shifts)
            return shifts
