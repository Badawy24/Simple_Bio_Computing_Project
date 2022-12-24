from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import random
import pandastable as pt

def extract_data(display_frame):
    # ======> Button Style
    btn_style = ttk.Style()
    btn_style.theme_use('vista')
    btn_style.configure('TButton',width=20,font=('Arial 12 bold'),wraplength=150,foreground="red")

    # ===> layout
    w = 650
    h = 100
    m = 15
    layout_bg = "#629c80"
    part_0 = Frame(display_frame, width=600,height=70,bg= layout_bg)
    part_1 = Frame(display_frame, width=w,height=200,bg= layout_bg)
    part_2 = Frame(display_frame, width=w,height=200,bg= layout_bg)

    part_0.pack()
    part_1.place(x=m,y=h)
    part_2.place(x=m,y=h*3+20)

    # ===> Title
    page_title= Label(part_0, text="Extract Information From File",font=('Arial 20 bold'),foreground="#000000",background=layout_bg,pady=20)
    page_title.pack()

    # ===> Label of Types 
    type_1_label = Label(part_1, text="Extract Information Using Split Character:",font=('Arial 14 bold'),foreground="#000000",background=layout_bg,pady=20)
    type_2_label = Label(part_2, text="Extract Information With ID:",font=('Arial 14 bold'),foreground="#000000",background=layout_bg,pady=20)
    type_1_label.place(x=1,y=1)
    type_2_label.place(x=1,y=1)

    # ==> Entery Type 1 
    upload_label_type_1 = Label(part_1, text="Choose File:",font=('Arial 12 bold'),foreground="blue",background=layout_bg)
    upload_btn_type_1 = ttk.Button(part_1, text="Upload File",cursor="hand2",width=10)
    hint_upload_type_1 = Label(part_1,text = "",font=('Arial 8 bold'),foreground="red",background=layout_bg)
    file_name_type_1 = Label(part_1,text = "File Explorer path",font=('Arial 8 bold'),foreground="black",background=layout_bg)
    split_label_type_1 = Label(part_1, text="Enter Split Character:",font=('Arial 12 bold'),foreground="blue",background=layout_bg)
    split_input_type_1 = ttk.Entry(part_1,width=24,font=('Arial',12))

    view_btn_type_1 = ttk.Button(part_1, text="Review Result",cursor="hand2")
    extract_btn_type_1 = ttk.Button(part_1, text="Convert To CSV",cursor="hand2")

    # ==> Display Type 1 Element  
    upload_label_type_1.place(x=10,y=70)
    file_name_type_1.place(x=15,y=100)
    upload_btn_type_1.place(x=120,y=70)
    split_label_type_1.place(x=250,y=70)
    split_input_type_1.place(x=420 ,y=70)
    view_btn_type_1.place(x=250,y=130)
    extract_btn_type_1.place(x=450 ,y=130)
    hint_upload_type_1.place(x=450,y=180)

    # ==> Entery Type 2 
    upload_label_type_2 = Label(part_2, text="Choose File:",font=('Arial 12 bold'),foreground="blue",background=layout_bg)
    upload_btn_type_2 = ttk.Button(part_2, text="Upload File",cursor="hand2",width=10)
    hint_upload_type_2 = Label(part_2,text = "",font=('Arial 8 bold'),foreground="red",background=layout_bg)
    file_name_type_2 = Label(part_2,text = "File Explorer path",font=('Arial 8 bold'),foreground="black",background=layout_bg)
    view_btn_type_2 = ttk.Button(part_2, text="Review Result",cursor="hand2")
    extract_btn_type_2 = ttk.Button(part_2, text="Convert To CSV",cursor="hand2")

    # ==> Display Type 2 Element  
    upload_label_type_2.place(x=10,y=70)
    file_name_type_2.place(x=15,y=100)
    upload_btn_type_2.place(x=120,y=70)
    view_btn_type_2.place(x=250,y=70)
    extract_btn_type_2.place(x=450 ,y=70)
    hint_upload_type_2.place(x=450,y=110)


    # ==> Buttons Function When Clicked ====
    def view_type_1_btn(file_name,spilt_char=""): # Type 1
        view_data(file_name,spilt_char,"Sequence","Hemolytic",1)

    def fas2csv_type_1_btn(file_name,spilt_char):   # Type 1
        convert2csv(file_name,spilt_char,"Sequence","Hemolytic",1)

    def view_type_2_btn(file_name):   # Type 2
        view_data(file_name,"","ID","Sequence",2)

    def fas2csv_type_2_btn(file_name):   # Type 2
        convert2csv(file_name,"","ID","Sequence",2)

    # ===> Functions Bio Computing
    def ext_data_split_char(file_name,spilt_char): # FUnction to Extract Data From File [Type 1 ]
        infile = open(file_name)
        flag=0
        lst=[]
        for line in infile:
            if flag==0:
                s=line.split(spilt_char)
                # print(s[3])
                flag=1
            else:
                # print(line[:-1])
                flag=0
                if s[3]=='non-hemolytic' or s[3]=='non-hemolytic\n':
                    lst.append([line[:-1],0])
                else:
                    lst.append([line[:-1],1])
        return lst

    def ext_data_with_id(file_name):   # Function TO Extract Data From File With ID [Type 2 ]
        infile = open(file_name)
        tb=[]
        for line in infile:
            if line[0]==">":
                x=line[1:-1]
            else:
                seq=line[:-1]
                tb.append([x,seq])
        return tb

    def view_data(file_name,spilt_char,head1,head2,type_fun):  # Functio to Display Data In Table 
            lst = []
            w = 0
            if type_fun == 1:
                lst = ext_data_split_char(file_name,spilt_char)
                w = 50
            elif type_fun == 2:
                lst = ext_data_with_id(file_name)
                w = 30

            data_extract = pd.DataFrame(lst,dtype=int,columns= [head1,head2])

            dTDa1 = Toplevel()
            dTDa1.title('Result Data Frame')
            dTDa1.geometry('900x500')
            dTDaPT = pt.Table(dTDa1, dataframe=data_extract, showtoolbar=True, showstatusbar=True)
            dTDaPT.show()
        # Display Table Of Some Data  
            # newWindow = Toplevel(display_frame)
            # newWindow.title("Review Data")
            # newWindow.geometry("600x600")
            # total_columns = len(lst[0])

            # # Head Of Table
            # h1 = Entry(newWindow,width =w,fg="red",font=('Arial',10,'bold'))
            # h1.grid(row=0, column=0)
            # h1.insert(END, head1)
            # h2 = Entry(newWindow,width =w,fg="red",font=('Arial',10,'bold'))
            # h2.grid(row=0, column=1)
            # h2.insert(END, head2)

            # for i in range(25):
            #     for j in range(total_columns):
            #         e = Entry(newWindow,width= w,font=('Arial',10,'bold'))
            #         e.grid(row=i+1, column=j)
            #         e.insert(END, lst[i][j])

    def convert2csv(file_name,spilt_char,head1,head2,type_fun): # function To Extract CSV File
        head=[head1,head2]
        lst = []
        if type_fun == 1:
            lst = ext_data_split_char(file_name,spilt_char)
            hint_upload_type_1.configure(text="File Converted")
        elif type_fun == 2:
            lst = ext_data_with_id(file_name)
            hint_upload_type_2.configure(text="File Converted")

        df=pd.DataFrame(lst,columns=head)
        df.to_csv(file_name+str(random.randint(1,50))+".csv")

    def uploadFiles(x):
        filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Text files",
            "*.txt*"),
            ("all files","*.*")))
        if x == 1:
            file_name_type_1.configure(text=filename)
        elif x == 2:
            file_name_type_2.configure(text=filename)
        return filename

    # ==> Click Buttons
    upload_btn_type_1.config(command= lambda: uploadFiles(1))
    view_btn_type_1.config(command= lambda: view_type_1_btn(file_name_type_1.cget("text"),split_input_type_1.get()))
    extract_btn_type_1.config(command= lambda: fas2csv_type_1_btn(file_name_type_1.cget("text"),split_input_type_1.get()))
    upload_btn_type_2.config(command= lambda: uploadFiles(2))
    view_btn_type_2.config(command= lambda: view_type_2_btn(file_name_type_2.cget("text")))
    extract_btn_type_2.config(command= lambda: fas2csv_type_2_btn(file_name_type_2.cget("text")))
