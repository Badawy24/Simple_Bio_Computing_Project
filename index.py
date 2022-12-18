# ==========================================================
# ============= Import =====================================
from tkinter import * # GUI Library 
from tkinter import ttk # Have Layout Of Screen [Button, Label, TextBox, ........]
from PIL import ImageTk, Image
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# =========== Main Window ==================================
frame = Tk() # To make Window Which Hold Layout
frame.title("Bio Computing Project")
frame.geometry("800x600") # Re-size Window
frame.resizable(False,False) 
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# =========== Style ==================================
style = ttk.Style()
# print(style.theme_names())
style.theme_use('vista')
style.configure('TButton',width=15,font=('Arial 11 bold'),wraplength=100)

bg = Image.open('bgDna.jpg')
bg_resize = bg.resize((800,600),Image.ANTIALIAS)
bgImg = ImageTk.PhotoImage(bg_resize)
backgroundFrame = Label(frame, image=bgImg)
backgroundFrame.place(x = 0,y = 0)
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# ================ Heading =================================
welcomeText= ttk.Label(frame, text="Welcome To Our System",font=('Arial 20 bold'),background="#01183B",foreground="#FFFFFF")
welcomeText.grid(row=0,column=0,padx=(0,600),pady=30, sticky='E')

# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# ================ Buttons =================================
btn1 = ttk.Button(frame,text="Extract File")
btn1.grid(row=1,column=0,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
btn2 = ttk.Button(frame,text="Seqence Operation")
btn2.grid(row=1,column=0,padx=300,pady=30,ipadx=15,ipady=15,sticky='W')
btn3 = ttk.Button(frame,text="Section 3")
btn3.grid(row=1,column=0,padx=500,pady=30,ipadx=15,ipady=15 ,sticky='W')

btn4 = ttk.Button(frame,text="Section 4")
btn4.grid(row=2,column=0,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
btn5 = ttk.Button(frame,text="Section 5")
btn5.grid(row=2,column=0,padx=300,pady=30,ipadx=15,ipady=15,sticky='W')
btn6 = ttk.Button(frame,text="Section 6")
btn6.grid(row=2,column=0,padx=500,pady=30,ipadx=15,ipady=15 ,sticky='W')

btn7 = ttk.Button(frame,text="Section 7")
btn7.grid(row=3,column=0,padx=100,pady=30,ipadx=15,ipady=15 ,sticky='W')
btn8 = ttk.Button(frame,text="Section 8")
btn8.grid(row=3,column=0,padx=300,pady=30,ipadx=15,ipady=15,sticky='W')

# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# ============= Functions =================================
def btn_click(x):
    if x == 1:
        from sec1 import ConvertFasta2CSV
        print("click")
        newFrame = ConvertFasta2CSV()
    elif x==2:
        from sec2 import seqOpr
        print("click")
        newFrame = seqOpr()
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# ============== Events ===================================
btn1.config(command= lambda: btn_click(1))
btn2.config(command= lambda: btn_click(2))
btn3.config(command= lambda: btn_click(3))
btn4.config(command= lambda: btn_click(4))
btn5.config(command= lambda: btn_click(5))
btn6.config(command= lambda: btn_click(6))
btn7.config(command= lambda: btn_click(7))
btn8.config(command= lambda: btn_click(8))


frame.mainloop() # To Display Run Of Code
# ==========================================================
# ++++++++++++++++++++++++++++++++++++++++
# ==========================================================