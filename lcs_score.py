from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import bisect
from pandastable import Table, TableModel
from itertools import permutations
import pandastable as pt



def LCS_score(display_frame):
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
        page_title= Label(part_0, text="LCS Score",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seq_1_Label = ttk.Label(part_1, text="Enter First Sequence:",font=("Arial 14 bold"),background=layout_bg)
        seq_1_Label.place(x=10,y=10)
        entry_seq_1 = ttk.Entry(part_1,width=35,font=('Arial',14))
        entry_seq_1.place(x=240,y=10)

        seq_2_Label = ttk.Label(part_2, text="Enter Second Sequence:",font=("Arial 14 bold"),background=layout_bg)
        seq_2_Label.place(x=10,y=5)
        entry_seq_2 = ttk.Entry(part_2,width=35,font=('Arial',14))
        entry_seq_2.place(x=240,y=10)

        mismatch_Label = ttk.Label(part_3, text="Enter Miss Match:",font=("Arial 14 bold"),background=layout_bg)
        mismatch_Label.place(x=10,y=10)
        entry_mismatch = ttk.Entry(part_3,width=3,font=('Arial',14))
        entry_mismatch.place(x=180,y=10)

        match_Label = ttk.Label(part_3, text="Enter Match:",font=("Arial 14 bold"),background=layout_bg)
        match_Label.place(x=250,y=10)
        entry_match = ttk.Entry(part_3,width=3,font=('Arial',14))
        entry_match.place(x=375,y=10)

        gab_Label = ttk.Label(part_3, text="Gab Benality:",font=("Arial 14 bold"),background=layout_bg)
        gab_Label.place(x=450,y=10)
        entry_gab = ttk.Entry(part_3,width=3,font=('Arial',14))
        entry_gab.place(x=580,y=10)

        LCS_result_btn = ttk.Button(part_4,text="\nView Result\n",cursor="hand2")
        LCS_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_5, text="",font=("Arial 14 bold"),background=layout_bg,wraplength=600)
        indx_match.pack()

        LCS_result_btn.config(command= lambda: result_seq_btn(entry_seq_1.get(),entry_seq_2.get(),int(entry_mismatch.get()),int(entry_match.get()),int(entry_gab.get())))
        #LCS_result_btn.config(command= lambda: result_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
    # =============== Button Function ===========================
        def result_seq_btn(Seq1, Seq2, mismatch, match, gap):
            res = LCS_score_bio(Seq1, Seq2, mismatch, match, gap)
            indx_match.configure(text="Result : {}\n ".format(res[len(Seq1)][len(Seq2)]))
        # =============== Bio Computing Function ===========================

        def LCS_score_bio(Seq1, Seq2, mismatch, match, gap):
    
            L = [[0 for x in range(len(Seq2)+1)] for x in range(len(Seq1)+1)]
            prev_1=0
            prev_2=0

            # intialize 1st row by gap incremental value 
            for i in range(len(Seq1)+1):
                L[i][0] =prev_2
                prev_2=gap+prev_2 
            
            # intialize 1st colomn by gap incremental value 
            for j in range(len(Seq2)+1):
                L[0][j] =prev_1
                prev_1=gap+prev_1
                
            # Building the scoring matrix
            for i in range(1,len(Seq1)+1):
                for j in range(1,len(Seq2)+1):
                

                        
                    if ((L[i-1][j]  == L[i][j-1]) and (Seq1[i-1] == Seq2[j-1])) :
                        L[i][j] = L[i-1][j-1] + match
                        
                    elif  (Seq1[i-1] == Seq2[j-1]) and  (L[i-1][j]  != L[i][j-1]):
                        L[i][j] = L[i-1][j-1] + match
                        
                    elif  (Seq1[i-1] != Seq2[j-1]) and  (L[i-1][j]  == L[i][j-1]):
                        L[i][j] = L[i-1][j-1] + mismatch 
                        
                    else :
                        L[i][j] = max(L[i-1][j], L[i][j-1])+gap
                        
                        
            return L   