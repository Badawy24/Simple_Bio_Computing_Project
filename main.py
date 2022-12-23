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
    sec4_ind.config(bg=side_bar_bg)
    sec5_ind.config(bg=side_bar_bg)
    sec6_ind.config(bg=side_bar_bg)
    sec7_ind.config(bg=side_bar_bg)
    sec8_ind.config(bg=side_bar_bg)

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

def bad_char():
    from bad_char import bad_character
    bad_character(display_frame)
    
def menu_page():
    meun_frame = Frame(display_frame)
    lb = Label(meun_frame,text="meun Page")
    lb.pack()
    meun_frame.pack(pady=20)
def cont_page():
    cont_frame = Frame(display_frame)
    lb = Label(cont_frame,text="contact Page")
    lb.pack()
    cont_frame.pack(pady=20)


layout_bg = "#629c80"
side_bar_bg = "#c3c3c3"
# =====> Options Side Bar Toggle
options_side_bar = Frame(main,background=side_bar_bg)
options_side_bar.pack(side=LEFT)
options_side_bar.pack_propagate(False)
options_side_bar.configure(width=150,height=700)

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
y_section = 30
increment = 80
ind_w = 10

ext_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
ext_btn.place(x=15,y=y_section)
ext_ind = Label(options_side_bar,text='',background=side_bar_bg)
ext_ind.place(x=3,y=y_section,width=ind_w,height=50)
ext_btn.config(command=lambda: ind(ext_ind,extract_data))

seq_opr_btn = Button(options_side_bar,text="Sequence Operations",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
seq_opr_btn.place(x=15,y=y_section+increment)
seq_opr_ind = Label(options_side_bar,text='',background=side_bar_bg)
seq_opr_ind.place(x=3,y=y_section+increment,width=ind_w,height=50)
seq_opr_btn.config(command=lambda: ind(seq_opr_ind,seq_opration))

bad_char_btn = Button(options_side_bar,text="Bad Characters",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
bad_char_btn.place(x=15,y=y_section+increment*2)
bad_char_ind = Label(options_side_bar,text='',background=side_bar_bg)
bad_char_ind.place(x=3,y=y_section+increment*2,width=ind_w,height=50)
bad_char_btn.config(command=lambda: ind(bad_char_ind,bad_char))

sec4_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
sec4_btn.place(x=15,y=y_section+increment*3)
sec4_ind = Label(options_side_bar,text='',background=side_bar_bg)
sec4_ind.place(x=3,y=y_section+increment*3,width=ind_w,height=50)
sec4_btn.config(command=lambda: ind(sec4_ind,menu_page))

sec5_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
sec5_btn.place(x=15,y=y_section+increment*4)
sec5_ind = Label(options_side_bar,text='',background=side_bar_bg)
sec5_ind.place(x=3,y=y_section+increment*4,width=ind_w,height=50)
sec5_btn.config(command=lambda: ind(sec5_ind,menu_page))

sec6_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
sec6_btn.place(x=15,y=y_section+increment*5)
sec6_ind = Label(options_side_bar,text='',background=side_bar_bg)
sec6_ind.place(x=3,y=y_section+increment*5,width=ind_w,height=50)
sec6_btn.config(command=lambda: ind(sec6_ind,menu_page))

sec7_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
sec7_btn.place(x=15,y=y_section+increment*6)
sec7_ind = Label(options_side_bar,text='',background=side_bar_bg)
sec7_ind.place(x=3,y=y_section+increment*6,width=ind_w,height=50)
sec7_btn.config(command=lambda: ind(sec7_ind,menu_page))

sec8_btn = Button(options_side_bar,text="Extract Data From File",font=("bold 13"),bg=side_bar_bg,bd=0,wraplength=100,cursor="hand2")
sec8_btn.place(x=15,y=y_section+increment*7)
sec8_ind = Label(options_side_bar,text='',background=side_bar_bg)
sec8_ind.place(x=3,y=y_section+increment*7,width=ind_w,height=50)
sec8_btn.config(command=lambda: ind(sec8_ind,menu_page))


main.mainloop() 