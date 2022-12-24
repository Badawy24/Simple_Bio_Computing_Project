from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
from pandastable import Table, TableModel
import pandastable as pt


def suffix_arr(display_frame):
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
        part_1 = Frame(display_frame, width=w,height=80,bg= layout_bg)
        part_2 = Frame(display_frame, width=w,height=80,bg= layout_bg)


        part_0.pack()
        part_1.place(x=m,y=h)
        part_2.place(x=m,y=h*1.75)

        # ===> Title
        page_title= Label(part_0, text="Suffix Array",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seq_Label = ttk.Label(part_1, text="Enter Sub Sequence:",font=("Arial 14 bold"),background=layout_bg)
        seq_Label.place(x=20,y=10)
        entry_seq = ttk.Entry(part_1,width=40,font=('Arial',14))
        entry_seq.place(x=230,y=10)


        sufx_result_btn = ttk.Button(part_2,text="\nView Result\n",cursor="hand2")
        sufx_result_btn.place(x=490,y=10)


        sufx_result_btn.config(command= lambda: sufx_arr_btn(entry_seq.get()))
        # sufx_result_btn.config(command= lambda: result_seq_btn("TTTGTTTCGAGCCTTACCGACACTGATGAGCCAAGAGGAACTTGGAGGCACCCAGGAATTTCACCCGGGTCGACCTGGGCGGCTAGGAGCCGTGCACAGGGCGTCGCTGTGGAGCGAGCCTGGCCTCCAAGGGGCCTGGAGGCGAAACTAACGGTCTGTTGGGACCACTCGGACCATCAGTCATCGTGCTCCGGCAGCTT","GCGTCGCTGTGGAG"))
    # =============== Button Function ===========================
        def sufx_arr_btn(seq):
            sufix, index = get_Suffix_Array(seq)
            seprator = ['-'] * len(seq)
            letters = [i for i in seq]
            data = np.array([sufix, index, seprator, letters])
            new_data = pd.DataFrame({"Suffixes" : data[0, :], "Indexes" : data[1, :], "Seperator" : data[2, :] ,"Letters" : data[3, :] })
            prefix_doubling_construction(seq,new_data)
            print(new_data)

            dTDa1 = Toplevel()
            dTDa1.title('Result Data Frame')
            dTDa1.geometry('900x500')
            dTDaPT = pt.Table(dTDa1, dataframe=new_data, showtoolbar=True, showstatusbar=True)
            dTDaPT.show()
    # =============== Bio Computing Function ===========================
        
        def get_Suffix_Array(s):
            list = []
            for i in range(0, len(s)):
                list.append((s[i:], i))
            list.sort()
            suffixs, indexs = [], []
            for i in list:
                suffixs.append(i[0])
                indexs.append(i[1])
            return suffixs, indexs

        def tt(str_x):
            set_of_letters = set(str_x)  # make a set of letters in a string
            sorted_list = sorted(set_of_letters) # make a sorted list of all letters
            enum_object = enumerate(sorted_list)
            dict_element = {a: i+1 for i,a in enum_object}  #conver enumerate list into dict with index +1
            # print(dict_element)
            
            list_letter_pos = [dict_element[a] for a in str_x]
            
            return list_letter_pos, len(dict_element)+1
            

        def get_rank(rank: list[int], i: int) -> int:
            return rank[i] if i < len(rank) else 0

        def bsort(sa: list[int], rank: list[int], out: list[int],
                k: int, z: int) -> None:
            
            buckets = [0] * z  # [0,0,0,0,0,0]
            
            for i in sa:  # sa = [0,1,2,3,4,5,6]
                r = get_rank(rank, i + k)   # [2,2,5,3,3,4,1] , 1 + 1 = 2  ===> return 2
                buckets[r] += 1             # [0,0,1,0,0,0]
            acc = 0
            for i, b in enumerate(buckets):
                buckets[i] = acc
                acc += b
            for i in sa:
                r = get_rank(rank, i + k)
                out[buckets[r]] = i
                buckets[r] += 1

        def update_rank(sa: list[int], rank: list[int],
                        out: list[int], k: int) -> int:
        
            z = 1  # leave 0 for sentinel
            out[sa[0]] = z
            prev_rank = (rank[sa[0]], get_rank(rank, sa[0] + k))
            for i in sa[1:]:
                this_rank = (rank[i], get_rank(rank, i + k))
                z += (prev_rank != this_rank)
                prev_rank = this_rank
                out[i] = z
            return z + 1

        def prefix_doubling_construction(x: str,new_data) -> list[int]:
            
            rank, z = tt(x)
            new_data['Iteration 0'] = rank
            # get list of indexes of string [0,1,2,3,4,5,6]
            sa = list(range(len(x)))
            # get an zero list of length of string  [0,0,0,0,0,0,0]
            buf = [0] * len(x)
            
            k = 1
            y = 1
            while z < len(x) + 1:  # 6 < len of string + 1
                
                bsort(sa, rank, buf, k, z)   
                bsort(buf, rank, sa, 0, z)
                # compute the new ranks
                z = update_rank(sa, rank, buf, k)
                rank, buf = buf, rank  # switch buffers to get new ranks in ranks
                # print(rank, buf)
                new_data['Iteration ' + str(y)] = rank
                y+=1
                
                k *= 2
            return sa