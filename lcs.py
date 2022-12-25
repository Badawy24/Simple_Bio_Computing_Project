from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import bisect
from pandastable import Table, TableModel
from itertools import permutations
import pandastable as pt



def LCS(display_frame):
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
        page_title= Label(part_0, text="LCS",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seq_1_Label = ttk.Label(part_1, text="Enter First Sequence:",font=("Arial 14 bold"),background=layout_bg)
        seq_1_Label.place(x=10,y=10)
        entry_seq_1 = ttk.Entry(part_1,width=35,font=('Arial',14))
        entry_seq_1.place(x=240,y=10)

        seq_2_Label = ttk.Label(part_2, text="Enter Second Sequence:",font=("Arial 14 bold"),background=layout_bg)
        seq_2_Label.place(x=10,y=10)
        entry_seq_2 = ttk.Entry(part_2,width=35,font=('Arial',14))
        entry_seq_2.place(x=240,y=10)

        LCS_result_btn = ttk.Button(part_3,text="\nView Result\n",cursor="hand2")
        LCS_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_4, text="",font=("Arial 14 bold"),background=layout_bg,wraplength=600)
        indx_match.pack()

        LCS_result_btn.config(command= lambda: result_seq_btn(entry_seq_1.get(),entry_seq_2.get()))
        #LCS_result_btn.config(command= lambda: result_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
    # =============== Button Function ===========================
        def result_seq_btn(seq1,seq2):
            LCS_lenght, CommSub = LCS(seq1, seq2)
            indx_match.configure(text="Common Subseq : {}\n length of Common Subseq : {}\n".format(CommSub,LCS_lenght))
        # =============== Bio Computing Function ===========================

        def LCS(Seq1, Seq2):

            L = [[0 for x in range(len(Seq2)+1)] for x in range(len(Seq1)+1)]

            # Building the LCS matrix
            for i in range(len(Seq1)+1):
                for j in range(len(Seq2)+1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif Seq1[i-1] == Seq2[j-1]:
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])
                        
            
            index = L[i][j]
            lcs_algo = [''] * (index+1)
            lcs_algo[index] =''
            
            i = len(Seq1)
            j = len(Seq2)
            
            #backward proceeding 
            while i > 0 and j > 0:

                if Seq1[i-1] == Seq2[j-1]:
                    lcs_algo[index] = Seq1[i-1]
                    i -= 1
                    j -= 1
                    index -= 1

                elif L[i-1][j] > L[i][j-1]:
                    i -= 1
                else:
                    j -= 1
                    
            CommSub=''
            for i in lcs_algo :
                CommSub=CommSub+i

            return L[len(Seq1)][len(Seq2)], CommSub
