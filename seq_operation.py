from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import filedialog   

def seq_oper(display_frame):
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
        page_title= Label(part_0, text="Sequence Operations",font=('Arial 20 bold'),background=layout_bg,pady=20)
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

        GC_Content_btn = ttk.Button(part_3,text="\nGC Content\n",cursor="hand2")
        GC_Content_btn.place(x=10,y=10)

        Complement_btn = ttk.Button(part_3,text="\nComplement\n",cursor="hand2")
        Complement_btn.place(x=170,y=10)

        Reverse_btn = ttk.Button(part_3,text="\nReverse\n",cursor="hand2")
        Reverse_btn.place(x=330,y=10)
        
        Reverse_Complement_btn = ttk.Button(part_3,text="    Reverse Complement",padding=10,cursor="hand2")
        Reverse_Complement_btn.place(x=490,y=10)

        seq_before = ttk.Label(part_4, text="",wraplength=650,font=("Arial 14 bold"),background=layout_bg,width=500)
        seq_before.pack()
        seq_after = ttk.Label(part_4, text="",wraplength=650,font=("Arial 14 bold"),background=layout_bg,foreground="red",width=500)
        seq_after.pack()

        GC_Content_btn.config(command= lambda: content_btn(seq_priority().upper()))
        Complement_btn.config(command= lambda: complement_btn(seq_priority().upper()))
        Reverse_btn.config(command= lambda: reverse_btn(seq_priority().upper()))
        Reverse_Complement_btn.config(command= lambda: reverse_complement_btn(seq_priority().upper()))
        upload_btn_seq.config(command= lambda: uploadFiles())
    # =============== Button Function ===========================
        def content_btn(seq):
            seq_before.configure(text="Sequence: "+seq+"\n")
            seq_after.configure(text="CG Ratio: "+str(GC_Content(seq)))
            # messagebox.showinfo(title="CG Ratio", message="CG Ratio = "+str(GC_Content(seq)))
            # GC_Content(seq)

        def complement_btn(seq):
            seq_before.configure(text="Sequence: "+seq+"\n")
            seq_after.configure(text="Complement: "+str(Complement(seq)))
            # messagebox.showinfo(title="Sequence Complement", message="Complement : "+str(Complement(seq)))
            # Complement(seq)

        def reverse_btn(seq):
            seq_before.configure(text="Sequence: "+seq+"\n")
            seq_after.configure(text="Reverse: "+str(Reverse(seq)))
            # messagebox.showinfo(title="Reverse Sequence", message="Reverse : "+str(Reverse(seq)))
            # Reverse(seq)

        def reverse_complement_btn(seq):
            seq_before.configure(text="Sequence: "+seq+"\n")
            seq_after.configure(text="Reverse Complement: "+str(Reverse_Complement(seq)))
            # messagebox.showinfo(title="Reverse Complement Sequence", message="Reverse Complement : "+str(Reverse_Complement(seq)))
            # Reverse_Complement(seq)

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

        def GC_Content(seq):
            l=len(seq)
            num_G=seq.count("G")
            num_C=seq.count("C")
            total=num_C+num_G
            return round(total/l , 2)
            
        def Complement( seq):
            dic={"G":"C","C":"G","A":"T","T":"A"}
            s=list(seq)
            for i in range(len(seq)):
                s[i]=dic[seq[i]]
            s="".join(s)
            return s

        def Reverse( seq):
            s=list(seq)
            s=reversed(s)
            s="".join(s)
            return s

        def Reverse_Complement(seq):
            seq= Reverse(seq)
            seq= Complement(seq)
            return seq