from tkinter import * 
# =====> Main Page
main = Tk()
main.geometry("900x700+300+50")
main.title("Bio Computing Project")
main.resizable(FALSE,FALSE)

# ==> Functions Of Code 
def ind(lb,page):
    hide_ind()
    lb.config(bg=layout_bg)
    delete_page()
    page()

def hide_ind():
    ext_ind.config(bg=side_bar_bg)
    seq_opr_ind.config(bg=side_bar_bg)
    bad_char_ind.config(bg=side_bar_bg)
    trns_table_ind.config(bg=side_bar_bg)
    qury_match_ind.config(bg=side_bar_bg)
    ovar_lab_ind.config(bg=side_bar_bg)
    sufix_arr_ind.config(bg=side_bar_bg)
    boyr_ind.config(bg=side_bar_bg)
    fibo_ind.config(bg=side_bar_bg)
    lcs_ind.config(bg=side_bar_bg)
    lcs_score_ind.config(bg=side_bar_bg)
    dist_ind.config(bg=side_bar_bg)
    # sec13_ind.config(bg=side_bar_bg)
    # sec14_ind.config(bg=side_bar_bg)
    # sec15_ind.config(bg=side_bar_bg)

def delete_page():
    for frame in display_frame.winfo_children():
        frame.destroy()

# ==> Bio Computing Functions 
def extract_data():
    from extract_data import extract_data
    extract_data(display_frame)
    
def seq_opration():
    from seq_operation import seq_oper
    seq_oper(display_frame)

def table_trans():
    from trans_table import tran_table
    tran_table(display_frame)
    

def bad_char():
    from bad_char import bad_character
    bad_character(display_frame)

def qury_match():
    from qury_match import qury
    qury(display_frame)

def over_lab():
    from ovrlab import ovr_lab
    ovr_lab(display_frame)

def sufix_arr():
    from sufix_arr import suffix_arr
    suffix_arr(display_frame)

def menu_page():
    meun_frame = Frame(display_frame)
    lb = Label(meun_frame,text="meun Page")
    lb.pack()
    meun_frame.pack(pady=20)



layout_bg = "#629c80"
side_bar_bg = "#c3c3c3"
# =====> Options Side Bar Toggle
options_side_bar = Frame(main,background=side_bar_bg)
options_side_bar.pack(side=LEFT)
options_side_bar.pack_propagate(False)
options_side_bar.configure(width=200,height=700)

# =====> Displaying Screen
display_frame = Frame(main,highlightbackground="black",highlightthickness=2,background=layout_bg)
display_frame.pack(side=LEFT)
display_frame.pack_propagate(False)
display_frame.configure(height=700,width=750)

# =====> Welcome Page
welcome = Frame(display_frame,bg=layout_bg)
lb1 = Label(welcome,text="Welcome To\n",font=("bold", 36),fg='red',bg=layout_bg)
lb2 = Label(welcome,text="Bio Computing\n",font=("bold", 36),fg='red',bg=layout_bg)
lb3 = Label(welcome,text="System\n",font=("bold", 36),fg='red',bg=layout_bg)
welcome.place(x=190, y =115)
lb1.pack()
lb2.pack()
lb3.pack()



#=======> Buttons Of Side Bar
y_section = 15
x_section = 3
increment = 50
ind_w = 10
ind_h=25

ext_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
ext_btn.place(x=15,y=y_section)
ext_ind = Label(options_side_bar,text='',background=side_bar_bg)
ext_ind.place(x=x_section,y=y_section,width=ind_w,height=ind_h)
ext_btn.config(command=lambda: ind(ext_ind,extract_data))

seq_opr_btn = Button(options_side_bar,text="Sequence Operations",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
seq_opr_btn.place(x=15,y=y_section+increment)
seq_opr_ind = Label(options_side_bar,text='',background=side_bar_bg)
seq_opr_ind.place(x=x_section,y=y_section+increment,width=ind_w,height=ind_h)
seq_opr_btn.config(command=lambda: ind(seq_opr_ind,seq_opration))

trns_table_btn = Button(options_side_bar,text="Translation Table",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
trns_table_btn.place(x=15,y=y_section+increment*2)
trns_table_ind = Label(options_side_bar,text='',background=side_bar_bg)
trns_table_ind.place(x=x_section,y=y_section+increment*2,width=ind_w,height=ind_h)
trns_table_btn.config(command=lambda: ind(trns_table_ind,table_trans))

bad_char_btn = Button(options_side_bar,text="Bad Characters",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
bad_char_btn.place(x=15,y=y_section+increment*3)
bad_char_ind = Label(options_side_bar,text='',background=side_bar_bg)
bad_char_ind.place(x=x_section,y=y_section+increment*3,width=ind_w,height=ind_h)
bad_char_btn.config(command=lambda: ind(bad_char_ind,bad_char))

qury_match_btn = Button(options_side_bar,text="Quray index Matching",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
qury_match_btn.place(x=15,y=y_section+increment*4)
qury_match_ind = Label(options_side_bar,text='',background=side_bar_bg)
qury_match_ind.place(x=x_section,y=y_section+increment*4,width=ind_w,height=ind_h)
qury_match_btn.config(command=lambda: ind(qury_match_ind,qury_match))

ovar_lab_btn = Button(options_side_bar,text="Ovar Lab",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
ovar_lab_btn.place(x=15,y=y_section+increment*5)
ovar_lab_ind = Label(options_side_bar,text='',background=side_bar_bg)
ovar_lab_ind.place(x=x_section,y=y_section+increment*5,width=ind_w,height=ind_h)
ovar_lab_btn.config(command=lambda: ind(ovar_lab_ind,over_lab))


sufix_arr_btn = Button(options_side_bar,text="Suffix Array",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
sufix_arr_btn.place(x=15,y=y_section+increment*6)
sufix_arr_ind = Label(options_side_bar,text='',background=side_bar_bg)
sufix_arr_ind.place(x=x_section,y=y_section+increment*6,width=ind_w,height=ind_h)
sufix_arr_btn.config(command=lambda: ind(sufix_arr_ind,sufix_arr))

boyr_btn = Button(options_side_bar,text="Boyer Suffix",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
boyr_btn.place(x=15,y=y_section+increment*7)
boyr_ind = Label(options_side_bar,text='',background=side_bar_bg)
boyr_ind.place(x=x_section,y=y_section+increment*7,width=ind_w,height=ind_h)
boyr_btn.config(command=lambda: ind(boyr_ind,menu_page))

fibo_btn = Button(options_side_bar,text="Fibonacci Sequence",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
fibo_btn.place(x=15,y=y_section+increment*8)
fibo_ind = Label(options_side_bar,text='',background=side_bar_bg)
fibo_ind.place(x=x_section,y=y_section+increment*8,width=ind_w,height=ind_h)
fibo_btn.config(command=lambda: ind(fibo_ind,menu_page))


lcs_btn = Button(options_side_bar,text="LCS",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
lcs_btn.place(x=15,y=y_section+increment*9)
lcs_ind = Label(options_side_bar,text='',background=side_bar_bg)
lcs_ind.place(x=x_section,y=y_section+increment*9,width=ind_w,height=ind_h)
lcs_btn.config(command=lambda: ind(lcs_ind,menu_page))


lcs_score_btn = Button(options_side_bar,text="LCS Score",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
lcs_score_btn.place(x=15,y=y_section+increment*10)
lcs_score_ind = Label(options_side_bar,text='',background=side_bar_bg)
lcs_score_ind.place(x=x_section,y=y_section+increment*10,width=ind_w,height=ind_h)
lcs_score_btn.config(command=lambda: ind(lcs_score_ind,menu_page))

dist_btn = Button(options_side_bar,text="Distance Between Sequance",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
dist_btn.place(x=15,y=y_section+increment*11)
dist_ind = Label(options_side_bar,text='',background=side_bar_bg)
dist_ind.place(x=x_section,y=y_section+increment*11,width=ind_w,height=ind_h)
dist_btn.config(command=lambda: ind(dist_ind,menu_page))

# sec13_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
# sec13_btn.place(x=15,y=y_section+increment*12)
# sec13_ind = Label(options_side_bar,text='',background=side_bar_bg)
# sec13_ind.place(x=x_section,y=y_section+increment*12,width=ind_w,height=ind_h)
# sec13_btn.config(command=lambda: ind(sec13_ind,menu_page))

# sec14_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
# sec14_btn.place(x=15,y=y_section+increment*13)
# sec14_ind = Label(options_side_bar,text='',background=side_bar_bg)
# sec14_ind.place(x=x_section,y=y_section+increment*13,width=ind_w,height=ind_h)
# sec14_btn.config(command=lambda: ind(sec14_ind,menu_page))

# sec15_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,cursor="hand2")
# sec15_btn.place(x=15,y=y_section+increment*14)
# sec15_ind = Label(options_side_bar,text='',background=side_bar_bg)
# sec15_ind.place(x=x_section,y=y_section+increment*14,width=ind_w,height=ind_h)
# sec15_btn.config(command=lambda: ind(sec15_ind,menu_page))


main.mainloop() 