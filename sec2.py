# ==========================================================
# ============= Import =====================================
from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from tkinter import messagebox
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# =========== Main Window ==================================
class seqOpr:
    def __init__(self,Sec2frame):
        seqLabel = ttk.Label(Sec2frame, text="Enter Sequence",font=("Arial 14 bold"))
        seqLabel.grid(row=0, column=0, padx=10, pady=20)
        entryseq = ttk.Entry(Sec2frame,width=50,font=('Arial',12))
        entryseq.grid(row=0, column=1, columnspan=2, pady=10,ipady=5)

        # s='ACTGTA'
        # s="GAGCTGGGCTGAGCCACCCGGGGGGCAGAGCCTGAAGAGAAACTGACTGG"
        # print("GC Content",self.GC_Content(seq))
        # print("Reverse Complement",self.Reverse_Complement(seq))
        # print("Translation Table",self.Translation_Table(seq))
        GC_Content_btn = ttk.Button(Sec2frame,text="GC Content")
        GC_Content_btn.grid(row=1, column=0, padx=10, pady=20,ipadx=15,ipady=15 )

        Complement_btn = ttk.Button(Sec2frame,text="Complement")
        Complement_btn.grid(row=1, column=1, padx=10, pady=20,ipadx=15,ipady=15)

        Reverse_btn = ttk.Button(Sec2frame,text="Reverse")
        Reverse_btn.grid(row=1, column=2, padx=10, pady=20,ipadx=15,ipady=15)
    
        Reverse_Complement_btn = ttk.Button(Sec2frame,text="Reverse Complement")
        Reverse_Complement_btn.grid(row=1, column=3, padx=10,pady=20,ipadx=15,ipady=15 )


        GC_Content_btn.config(command= lambda: self.content_btn(entryseq.get().upper()))
        Complement_btn.config(command= lambda: self.complement_btn(entryseq.get().upper()))
        Reverse_btn.config(command= lambda: self.reverse_btn(entryseq.get().upper()))
        Reverse_Complement_btn.config(command= lambda: self.reverse_complement_btn(entryseq.get().upper()))

    # =============== Button Function ===========================
    def content_btn(self,seq):
        messagebox.showinfo(title="CG Ratio", message="CG Ratio = "+str(self.GC_Content(seq)))
        # self.GC_Content(seq)

    def complement_btn(self,seq):
        messagebox.showinfo(title="Sequence Complement", message="Complement : "+str(self.Complement(seq)))
        # self.Complement(seq)
    
    def reverse_btn(self,seq):
        messagebox.showinfo(title="Reverse Sequence", message="Reverse : "+str(self.Reverse(seq)))
        # self.Reverse(seq)

    def reverse_complement_btn(self,seq):
        messagebox.showinfo(title="Reverse Complement Sequence", message="Reverse Complement : "+str(self.Reverse_Complement(seq)))
        # self.Reverse_Complement(seq)



    # =============== Button Function ===========================

    def GC_Content(self,seq):
        l=len(seq)
        num_G=seq.count("G")
        num_C=seq.count("C")
        total=num_C+num_G
        return round(total/l , 2)
        
    def Complement(self, seq):
        dic={"G":"C","C":"G","A":"T","T":"A"}
        s=list(seq)
        for i in range(len(seq)):
            s[i]=dic[seq[i]]
        s="".join(s)
        return s

    def Reverse(self, seq):
        s=list(seq)
        s=reversed(s)
        s="".join(s)
        return s

    def Reverse_Complement(self,seq):
        seq= self.Reverse(seq)
        seq= self.Complement(seq)
        return seq

    def Translation_Table(self,seq):
        dic = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
            "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
            "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
            "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
            "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
            "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
            "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
            "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
            "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
            "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
            "TAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
            "TAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
            "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
            "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
            "TGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
            "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
            }
        s=""
        for i in range(0,len(seq),3):
            if i+3>len(seq):
                break
            s+=dic[seq[i:i+3]]
        return s
            



Sec2frame = Tk() # To make Window Which Hold Layout
Sec2frame.title("Convert Fasta File To CSV")
Sec2frame.geometry("800x600") # Re-size Window
Sec2frame.resizable(False,False) 
t = seqOpr(Sec2frame)
Sec2frame.mainloop()





# tkinter.messagebox.showinfo(title=None, message=None, **options)