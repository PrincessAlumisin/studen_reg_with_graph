from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from regformdb import Database
import matplotlib.pyplot as plt

db = Database("student.db")
root = Tk()
root.title("Junior High School Olympics Registration")
root.geometry('1150x800')
root.config(bg="#f0c59f")

student_number = StringVar()
first_name = StringVar()
last_name = StringVar()
middle_name = StringVar()
sex = StringVar()
yearlevel = StringVar(value="0")
sports = StringVar()
sp1 = StringVar(value='')
sp2 = StringVar(value='')
sp3 = StringVar(value='')
sp4 = StringVar(value='')
sp5 = StringVar(value='')
sp6 = StringVar(value='')


# Entries Frame
entries_frame = Frame(root, bg="#f0c59f")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Junior High School Olympics Registration", font=("Calibri", 18, "bold"), bg="#EDCDBB", fg="black")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblNumber = Label(entries_frame, text="Student Number:", font=("Calibri", 16), bg="#EDCDBB", fg="black")
lblNumber.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtNumber = Entry(entries_frame, textvariable=student_number, font=("Calibri", 16), width=30)
txtNumber.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Student Name:", font=("Calibri", 16), bg="#EDCDBB", fg="black")

lblName.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txt_last_name = Entry(entries_frame, textvariable=last_name, font=("Calibri", 16), width=15)
txt_last_name.insert(0, 'Last_Name') #inserts string value, pseudo-placeholder
txt_last_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")


txt_first_name = Entry(entries_frame, textvariable=first_name, font=("Calibri", 16), width=15)
txt_first_name.insert(0, 'First_Name') #inserts string value, pseudo-placeholder
txt_first_name.grid(row=2, column=2, padx=10, pady=10, sticky="w")


txt_middle_name = Entry(entries_frame, textvariable=middle_name, font=("Calibri", 16), width=15)
txt_middle_name.insert(0, 'Middle_Name') #inserts string value, pseudo-placeholder
txt_middle_name.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblSex = Label(entries_frame, text="Sex:", font=("Calibri", 16), bg="#EDCDBB", fg="black")
lblSex.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboSex = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=sex, state="readonly")
comboSex['values'] = ("Male", "Female")
comboSex.grid(row=3, column=1, padx=10, sticky="w")

lblRecord = Label(entries_frame, text="Student Record", font=("Calibri", 17, "bold"), bg="#EDCDBB", fg="black")
lblRecord.grid(row=15, column=1, padx=10, pady=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    # print(row)
    student_number.set(row[0])
    last_name.set(row[1])
    first_name.set(row[2])
    middle_name.set(row[3])
    sex.set(row[4])
    yearlevel.set(row[5])
    sports.set(row[6])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_stud():
    if txtNumber.get() == "" or txt_last_name.get() == "" or txt_first_name.get() == "" or txt_middle_name.get() == "" or comboSex.get() == "" or yearlevel.get() == False or sp1.get() == \
            False and sp2.get() == False and sp3.get() == False and sp4.get() == False and sp5.get() == False and sp6.get() == False:
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    sports = sp1.get() + ' ' + sp2.get() + ' ' + sp3.get() + ' ' + sp4.get() + ' ' + sp5.get() + ' ' + sp6.get()
    db.insert(txtNumber.get(), txt_last_name.get(), txt_first_name.get(), txt_middle_name.get(), comboSex.get(), yearlevel.get(), sports)
    messagebox.showinfo("Success","Record Successfully Saved")
    clearAll()

def update_stud():
    if txtNumber.get() == "" or txt_last_name.get() == "" or txt_first_name.get() == "" or txt_middle_name.get() == "" or comboSex.get() == "" or yearlevel.get() == False or sp1.get() == \
            False and sp2.get() == False and sp3.get() == False and sp4.get() == False and sp5.get() == False and sp6.get() == False:
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    sports = sp1.get() + ' ' + sp2.get() + ' ' + sp3.get() + ' ' + sp4.get() + ' ' + sp5.get() + ' ' + sp6.get()

    db.update(txtNumber.get(), txt_last_name.get(), txt_first_name.get(), txt_middle_name.get(), comboSex.get(), yearlevel.get(), sports)
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    dispalyAll()

def delete_stud():
    delete_stud = messagebox.askyesno("Junior High School Olympics Registration", "Are you sure you want to delete this item?")
    if delete_stud > 0:
        db.remove(student_number.get())
        clearAll()
        dispalyAll()
    else:
        return


def clearAll():
    first_name.set("")
    last_name.set("")
    middle_name.set("")
    student_number.set("")
    sex.set("")
    yearlevel.set(False)
    sp1 = StringVar(value='')
    sp2 = StringVar(value='')
    sp3 = StringVar(value='')
    sp4 = StringVar(value='')
    sp5 = StringVar(value='')
    sp6 = StringVar(value='')

def iExit():
    iExit = messagebox.askyesno("Junior High School Olympics Registration", "Do you want to exit?")
    if iExit > 0:
        root.destroy()
        return


btn_frame = Frame(entries_frame, bg="#FFEDDB")
btn_frame.grid(row=5, column=0, columnspan=20, sticky="w", rowspan=10)

#save
Button(entries_frame, command=add_stud, text="Save", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#e9aa73", bd=0).grid(row=4, column=2, padx=10, pady=10, sticky='w')
#update
Button(entries_frame, command=update_stud, text="Edit", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#f3d2b5",
       bd=0).grid(row=4, column=3, padx=10,pady=10,sticky='w')
#delete
Button(entries_frame, command=delete_stud, text="Delete", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#c2c2c2",
       bd=0).grid(row=4, column=4, padx=10,pady=10,sticky='w')

#radiobutton
Label(btn_frame, text="Year Level:", font=("Calibri", 16), bg="#EDCDBB", fg="black").grid(row=0, column=0, pady=10, padx=10, sticky='w')

Radiobutton(btn_frame, text="Grade 7", value="Grade 7", width=15, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0).grid(row=1, column=0,padx=10, pady=10,sticky='w')

Radiobutton(btn_frame, text="Grade 8", value="Grade 8", width=15, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB",bd=0).grid(row=1,column=1,padx=10,pady=10,sticky='w')

Radiobutton(btn_frame, text="Grade 9", value="Grade 9", width=20, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB",bd=0).grid(row=1,column=2,padx=10,pady=10,sticky='w')

Radiobutton(btn_frame, text="Grade 10", value="Grade 10", width=20, variable=yearlevel,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB",bd=0).grid(row=1,column=3,padx=10,pady=10,sticky='w')

# checkbutton
Label(btn_frame, text="Sports:", font=("Calibri", 16), bg="#EDCDBB", fg="black").grid(row=2, column=0, pady=10,
                                                                                               padx=10, sticky='w')

Checkbutton(btn_frame, text="Badminton", offvalue="", onvalue="Badminton", variable=sp1, width=18,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, anchor='w',
            padx=20).grid(row=3, column=0, sticky='w')
Checkbutton(btn_frame, text="Volleyball", offvalue="", onvalue="Volleyball",  variable=sp2, width=18,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, anchor='w',
            padx=20).grid(row=3, column=1, sticky='w')
Checkbutton(btn_frame, text="Basketball", offvalue="", onvalue="Basketball",  variable=sp3, width=18,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, anchor='w',
            padx=20).grid(row=3, column=2, sticky='w')
Checkbutton(btn_frame, text="Gymnastics", offvalue="", onvalue="Gymnastics",  variable=sp4, width=18,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, anchor='w',
            padx=20).grid(row=4, column=0, sticky='w')
Checkbutton(btn_frame, text="Swimming", offvalue="", onvalue="Swimming",  variable=sp5, width=18,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, anchor='w',
            padx=20).grid(row=4, column=1, sticky='w')
Checkbutton(btn_frame, text="Soccer", offvalue="", onvalue="Soccer",  variable=sp6, width=18,
            font=("Calibri", 16, "bold"), fg="black", selectcolor="#EDCDBB", bg="#FFEDDB", bd=0, anchor='w',
            padx=20).grid(row=4, column=2, sticky='w')

#View
Button(entries_frame, command=dispalyAll, text="View", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#B85C38", bd=0).grid(row=15, column=4, padx=10, pady=10, sticky="w")

#Close
Button(entries_frame, command=iExit, text="Close", width=15, font=("Calibri", 16, "bold"),
       fg="white", bg="#B85C38",
       bd=0).grid(row=1, column=4, padx=10,pady=10,sticky='w')

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=10, y=600, width=1076, height=200)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))

scrolly = Scrollbar(tree_frame, orient="vertical")
scrolly.pack(side="right", fill="y")
scrollx = Scrollbar(tree_frame, orient="horizontal")
scrollx.pack(side="bottom", fill="x")
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

tv.heading("1", text="Student Number")
tv.heading("2", text="Last Name")
tv.heading("3", text="First Name")
tv.heading("4", text="Middle Name")
tv.heading("5", text="Sex")
tv.heading("6", text="Year Level")
tv.heading("7", text="Sports")
tv.column("7", width=300)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)
scrolly.config(command=tv.yview)
scrollx.config(command=tv.xview)



#graphs
def filterYearLevel():
    keys = []
    values = []
    datas = db.filterYearLevel()

    for x in datas:
        print(x)
        keys.append(x[0])
        values.append(x[1])

    fig, ax = plt.subplots()

    year_level_label = ax.bar(keys, values)

    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Year Level')
    ax.set_title('Number of students per Year Level')
    ax.legend()
    ax.bar_label(year_level_label)
    plt.show()


def filterSports():
    keys = []
    values = []
    datas = db.filterSports()

    for x in datas:
        print(x)
        keys.append(x[0])
        values.append(x[1])

    fig,ax = plt.subplots()

    sports = ax.bar(keys, values)

    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Sports')
    ax.set_title('Number of students per Sports')
    ax.legend()
    ax.bar_label(sports)
    plt.show()

def filterSex():
    keys = []
    values = []
    datas = db.filterSex()

    for x in datas:
        print(x)
        keys.append(x[0])
        values.append(x[1])

    fig, ax = plt.subplots()


    sex = ax.bar(keys, values)

    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Sex')
    ax.set_title('Number of students per Sex')
    ax.legend()
    ax.bar_label(sex)
    plt.show()




Button(entries_frame, command=filterYearLevel, text="Year Level", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#B85C38", bd=0).grid(row=15, column=1, padx=10, pady=10, sticky="w")
Button(entries_frame, command=filterSports, text="Sports", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#B85C38", bd=0).grid(row=15, column=2, padx=10, pady=10, sticky="w")
Button(entries_frame, command=filterSex, text="Sex", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#B85C38", bd=0).grid(row=15, column=3, padx=10, pady=10, sticky="w")

#hello
root.mainloop()