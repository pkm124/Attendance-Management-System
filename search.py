#import library
#import library for creating GUI
from tkinter import *
import tkinter.ttk as ttk
#import library for handling SQLite database
import sqlite3
#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("800x200")
    display_screen.state('zoomed')
    display_screen.resizable(0, 0)
    #setting title for window
    display_screen.title("Searching")
    global tree
    global SEARCH
    global SEARCH1
    global SEARCH2
    SEARCH = StringVar()
    SEARCH1 = StringVar()
    SEARCH2 = StringVar()
    #creating frame
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(display_screen, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Database Student Attencance Records", font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    #1st
    lbl_txtsearch = Label(LeftViewForm, text="Search Date", font=('verdana', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W,pady= 15)
    #2nd
    lbl_txtsearch1 = Label(LeftViewForm, text="Search Roll No.", font=('verdana', 15))
    lbl_txtsearch1.pack(side=TOP, anchor=W,pady=25)
    #3rd
    lbl_txtsearch2 = Label(LeftViewForm, text="Search Subject", font=('verdana', 15))
    lbl_txtsearch2.pack(side=TOP, anchor=W)

    #1st
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.place(x=5,y=45)
    #2nd
    search1 = Entry(LeftViewForm, textvariable=SEARCH1, font=('verdana', 15), width=10)
    search1.place(x=5,y=114)
    #3rd
    search2 = Entry(LeftViewForm, textvariable=SEARCH2, font=('verdana', 15), width=10)
    search2.place(x=5,y=180)
    
    #1st
    btn_search = Button(LeftViewForm, text="Search Date", command=SearchRecord,width=15)
    btn_search.place(x=200,y=50)
    #btn_search.pack(side=TOP, padx=200, pady=10, fill=X)
    #2nd
    btn_search1 = Button(LeftViewForm, text="Search Roll No.", command=SearchRecord1,width=15)
    btn_search1.place(x=200,y=120)
    #3rd
    btn_search2 = Button(LeftViewForm, text="Search Subject", command=SearchRecordSubject,width=15)
    btn_search2.pack(side=TOP, padx=200, pady=10, fill=X)

    btn_search = Button(LeftViewForm, text="View All", command=DisplayData,width=20)
    btn_search.place(x=50,y=250)

    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Contact", "Email","Rollno","Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Student Roll No.", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Date", anchor=W)
    tree.heading('Email', text="Status", anchor=W)
    tree.heading('Rollno', text="Subject", anchor=W)
    #tree.heading('Branch', text="Branch", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
#function to search data
def SearchRecord():
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        conn = sqlite3.connect('SchoolManagement.db')
        #select query with where clause
        cursor=conn.execute("SELECT * FROM data_attend WHERE date LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def SearchRecord1():
    #checking search text is empty or not
    if SEARCH1.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        conn = sqlite3.connect('SchoolManagement.db')
        #select query with where clause
        cursor=conn.execute("SELECT * FROM data_attend WHERE rollno LIKE ?", ('%' + str(SEARCH1.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def SearchRecordSubject():
    #checking search text is empty or not
    if SEARCH2.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #open database
        conn = sqlite3.connect('SchoolManagement.db')
        #select query with where clause
        cursor=conn.execute("SELECT * FROM data_attend WHERE subject LIKE ?", ('%' + str(SEARCH2.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

#defining function to access data from SQLite database
def DisplayData():
    #clear current data
    tree.delete(*tree.get_children())
    # open databse
    conn = sqlite3.connect('SchoolManagement.db')
    #select query
    cursor=conn.execute("SELECT * FROM data_attend")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#calling function
DisplayForm()

mainloop()