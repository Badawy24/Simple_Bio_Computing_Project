from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   

def tran_table(display_frame):
        # ======> Button Style
        btn_style = ttk.Style()
        btn_style.theme_use('vista')
        btn_style.configure('TButton',width=15, height =10,font=('Arial 12 bold'),wraplength=100,foreground="red")

        # ===> layout
        w = 650
        h = 100
        m = 10
        layout_bg = "#629c80"
        part_0 = Frame(display_frame, width=600,height=70,bg= layout_bg)
        part_1 = Frame(display_frame, width=w,height=50,bg= layout_bg)
        part_2 = Frame(display_frame, width=w,height=80,bg= layout_bg)
        part_3 = Frame(display_frame, width=w,height=80,bg= layout_bg)
        part_4 = Frame(display_frame, width=w,height=300,bg= layout_bg)

        part_0.pack()
        part_1.place(x=m,y=h)
        part_2.place(x=m,y=h*1.75)
        part_3.place(x=m,y=h*2.5)
        part_4.place(x=m,y=h*3.5)

        # ===> Title
        page_title= Label(part_0, text="Translation Table",font=('Arial 20 bold'),background=layout_bg,pady=20)
        page_title.pack()

        seqLabel = ttk.Label(part_1, text="Enter Sequence:",font=("Arial 14 bold"),background=layout_bg)
        seqLabel.place(x=20,y=10)
        entryseq = ttk.Entry(part_1,width=40,font=('Arial',14))
        entryseq.place(x=190,y=10)

        upload_label_seq = Label(part_2, text="Choose File:",font=('Arial 12 bold'),background=layout_bg)
        upload_btn_seq = ttk.Button(part_2, text="Upload File",cursor="hand2",width=10)
        file_name_seq = Label(part_2,text = "File Explorer path",font=('Arial 10 bold'),foreground="blue",background=layout_bg)
        upload_label_seq.place(x=10,y=10)
        upload_btn_seq.place(x=120,y=10)
        file_name_seq.place(x=220,y=10)

        
        
        trans_table_btn = ttk.Button(part_3,text="    Reverse Complement",padding=10,cursor="hand2")
        trans_table_btn.place(x=490,y=10)

        protin = ttk.Label(part_4, text="",wraplength=650,font=("Arial 14 bold"),background=layout_bg,width=500)
        protin.pack()
        seq_after = ttk.Label(part_4, text="",wraplength=650,font=("Arial 14 bold"),background=layout_bg,foreground="red",width=500)
        seq_after.pack()

        trans_table_btn.config(command= lambda: tran_table_btn(seq_priority().upper()))
        upload_btn_seq.config(command= lambda: uploadFiles())
    # =============== Button Function ===========================

        def tran_table_btn(seq):
            res = trans_table(seq)
            protin.configure(text="Sequnce After Translation: "+res+"\n")
            # seq_after.configure(text="Reverse Complement: "+str(trans_table(seq)))
            # messagebox.showinfo(title="Reverse Complement Sequence", message="Reverse Complement : "+str(trans_table(seq)))
            # trans_table(seq)

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
        
        def seq_priority():
            y = entryseq.get()
            x = file_name_seq.cget("text")
            if y:
                return y
            elif x:
                return extract_seq(x)
        # =============== Button Function ===========================

        def trans_table(seq):
            dic = {
                    "TTT" : "F",
                    "CTT" : "L",
                    "ATT" : "I",
                    "GTT" : "V",
                    "TTC" : "F",
                    "CTC" : "L",
                    "ATC" : "I",
                    "GTC" : "V",
                    "TTA" : "L",
                    "CTA" : "L",
                    "ATA" : "I",
                    "GTA" : "V",
                    "TTG" : "L",
                    "CTG" : "L",
                    "ATG" : "M",
                    "GTG" : "V",
                    "TCT" : "S",
                    "CCT" : "P",
                    "ACT" : "T",
                    "GCT" : "A",
                    "TCC" : "S",
                    "CCC" : "P",
                    "ACC" : "T",
                    "GCC" : "A",
                    "TCA" : "S",
                    "CCA" : "P",
                    "ACA" : "T",
                    "GCA" : "A",
                    "TCG" : "S",
                    "CCG" : "P",
                    "ACG" : "T",
                    "GCG" : "A",
                    "TAT" : "Y",
                    "CAT" : "H",
                    "AAT" : "N",
                    "GAT" : "D",
                    "TAC" : "Y",
                    "CAC" : "H",
                    "AAC" : "N",
                    "GAC" : "D",
                    "TAA" : "*",
                    "CAA" : "Q",
                    "AAA" : "K",
                    "GAA" : "E",
                    "TAG" : "*",
                    "CAG" : "Q",
                    "AAG" : "K",
                    "GAG" : "E",
                    "TGT" : "C",
                    "CGT" : "R",
                    "AGT" : "S",
                    "GGT" : "G",
                    "TGC" : "C",
                    "CGC" : "R",
                    "AGC" : "S",
                    "GGC" : "G",
                    "TGA" : "*",
                    "CGA" : "R",
                    "AGA" : "R",
                    "GGA" : "G",
                    "TGG" : "W",
                    "CGG" : "R",
                    "AGG" : "R",
                    "GGG" : "G" 
                }
            if len(seq)%3 != 0:
                seq = seq[:-1]
                if len(seq)%3 !=0 :
                    seq = seq[:len(seq)-1]
            s=""
            for i in range(0,len(seq),3):
                s+=dic[seq[i:i+3]]+" "
            return s