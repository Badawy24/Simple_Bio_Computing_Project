from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   
import numpy as np
import pandas as pd
import pandastable as pt


def dist_seq(display_frame):
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
        page_title= Label(part_0, text="Distance Between Sequance",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()


        upload_label_seq_1 = Label(part_1, text="Choose Sequance 1 File:",font=('Arial 12 bold'),background=layout_bg)
        upload_btn_seq_1 = ttk.Button(part_1, text="Upload File",cursor="hand2",width=10)
        file_name_seq_1 = Label(part_1,text = "File Explorer path",font=('Arial 10 bold'),foreground="blue",background=layout_bg)
        upload_label_seq_1.place(x=10,y=10)
        upload_btn_seq_1.place(x=210,y=10)
        file_name_seq_1.place(x=320,y=10)
        
        upload_label_seq_2 = Label(part_2, text="Choose Sequance 2 File:",font=('Arial 12 bold'),background=layout_bg)
        upload_btn_seq_2 = ttk.Button(part_2, text="Upload File",cursor="hand2",width=10)
        file_name_seq_2 = Label(part_2,text = "File Explorer path",font=('Arial 10 bold'),foreground="blue",background=layout_bg)
        upload_label_seq_2.place(x=10,y=10)
        upload_btn_seq_2.place(x=210,y=10)
        file_name_seq_2.place(x=320,y=10)

        dist_result_btn = ttk.Button(part_3,text="\nView Result\n",cursor="hand2")
        dist_result_btn.place(x=490,y=10)


        indx_match = ttk.Label(part_4, text="",font=("Arial 14 bold"),background=layout_bg)
        indx_match.pack()


        dist_result_btn.config(command= lambda: result_sub_seq_btn(extract_seq(file_name_seq_1.cget("text")).upper(),file_name_seq_2.cget("text")).upper())
    
        upload_btn_seq_1.config(command= lambda: uploadFiles(1))
        upload_btn_seq_2.config(command= lambda: uploadFiles(2))
    # =============== Button Function ===========================
        def result_sub_seq_btn(seq_1,seq_2):
            dist ,df = dist_seq(seq_1,seq_2)
            indx_match.configure(text="Distance Between 2 DNA Sequences = {}\n".format(dist))
            

            dTDa1 = Toplevel()
            dTDa1.title('Result Data Frame')
            dTDa1.geometry('900x500')
            dTDaPT = pt.Table(dTDa1, dataframe=df, showtoolbar=True, showstatusbar=True)
            dTDaPT.show()

        def uploadFiles(x):
            filename = filedialog.askopenfilename(initialdir = "/",
                title = "Select a File",
                filetypes = (("Text files",
                "*.txt*"),
                ("all files","*.*")))
            if x == 1:
                file_name_seq_1.configure(text=filename)
            elif x == 2:
                file_name_seq_2.configure(text=filename)
            return filename

        def extract_seq(filename):
            file=open(filename)
            l=[i for i in file]
            s=l[1][:-1]
            return s
        # =============== Bio Computing Function ===========================

        def dist_seq(seq_1,seq_2):
            tag=10
            dic={}
            for i in range(0,len(seq_1)-tag):
                dic[seq_1[i:i+tag]]=dic.get(seq_1[i:i+tag],0)+1
            head=['TAG','Count']
            df=pd.DataFrame(dic.items(),columns=head)
            # df.to_csv("tag.csv")

            dic2={}
            for i in range(0,len(seq_2)-tag):
                dic2[seq_2[i:i+tag]]=dic2.get(seq_2[i:i+tag],0)+1

            k=list(dic.keys())
            for i in range(len(k)):
                dic2[k[i]]=(dic2.get(k[i],0)-dic[k[i]])
            d=list(dic2.values())

            Sum=0
            for i in range(len(d)):
                Sum+=d[i]**2
            distance=Sum**(0.5)
            return distance ,df