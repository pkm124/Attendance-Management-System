#from cgitb import text
from datetime import date
from tkinter import * 
import sqlite3
import time
from tkinter import ttk
from tkinter import font
import tkinter.messagebox as mb
from PIL import ImageTk, Image


def admin():
    exec(open("admin.py").read())
def search():
    exec(open("search.py").read())
app = Tk()
#app.geometry("500x500")
#code for application size
#app.attributes('-fullscreen', True)
app.state('zoomed')
app.resizable(0, 0)

img = ImageTk.PhotoImage(Image.open("College1.jpg"))
label = Label(app, image = img,height=100,width=100)
label.place(x=10,y=0)

app.configure(bg="wheat")
app.title("Attendence Management System")
#code for heading
heading = Label(text="Attendence Management System",fg="#fff",bg="DarkRed",width="500",height="3",font="10")
heading.pack()

img = ImageTk.PhotoImage(Image.open("pcelogo.jpeg"))
label = Label(app, image = img,bg='White')
label.place(x=10,y=5)

DateofOrder = StringVar()
Date = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))
#print(DateofOrder.get)
frame=Frame(app,width=10,height=500,bg="white",highlightbackground="grey",highlightthickness=2)
frame.pack(padx=50,pady=40,side=LEFT,fill="y")

menu= StringVar()
menu.set("Select Any Subject")

drop= OptionMenu(app, menu,"DAA", "Java","Python","WP","OS","DBMS","MATHS","TOC")
drop.place(x=450,y=65)

#tree = ttk.Treeview(frame,selectmode=BROWSE,height=100)
"""tree = ttk.Treeview(frame, height=100, selectmode=BROWSE,columns=('Student ID', "Name", "Email Address","Status"))

tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Status', text='Status', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=70, stretch=NO)
#tree.column('#3', width=100, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)"""
#code for database connectivity
conn = sqlite3.connect('SchoolManagement.db')
c=conn.cursor()
c.execute("SELECT * FROM SCHOOL_MANAGEMENT")
r=c.fetchall()
num=4
j=0
array=[]
# img = ImageTk.PhotoImage(Image.open("College1.jpg"))

# Create a Label Widget to display the text or Image
Date=Entry(app,textvariable=DateofOrder)
Date.place(x=1200,y=20)
rno=Label(frame,text="Roll No",font=25,bg="white")
rno.grid(row=num,column=0)

n=Label(frame,text="Name",font=25,bg="white",padx=60)
n.grid(row=num,column=1)

s=Label(frame,text="Stream",font=25,bg="white",padx=60)
s.grid(row=num,column=2)

stat=Label(frame,text="Status",font=25,bg="white",padx=60)
stat.grid(row=num,column=3)
num=5
for i in r:
    rollno=Label(frame,text=i[0],font=25,bg="white",fg="grey")
    rollno.grid(row=num,column=0)

    name=Label(frame,text=i[1],font=25,bg="white",fg="grey")
    name.grid(row=num,column=1)
    #tree.insert('',END,values=i)

    stream=Label(frame,text=i[6],font=25,bg="white",fg="grey")
    stream.grid(row=num,column=2)
    """tree.insert('', END, values=(i[0],i[1],i[2]))"""

    array.append(1)
    array[j]=StringVar()
    a=Radiobutton(frame,text="A",variable=array[j],value="A",bg="white",fg="grey")
    a.grid(row=num,column=3)
    #tree.insert('',END,values=array[j])
    a.select()
    p=Radiobutton(frame,text="P",variable=array[j],value="P",bg="white",fg="grey")
    p.grid(row=num,column=4)
    p.deselect()
    
    dummy=Label(frame,text="",width=55,bg="white")
    dummy.grid(row=num,column=5)
    j=j+1
    num=num+1

def submit():
    num=0
    for i in r:
        temp=array[num].get()
        t=Date.get()
        sub=menu.get()
        c.execute("insert into data_attend values('"+str(i[0])+"','"+i[1]+"','"+t+"','"+temp+"','"+sub+"')")
        num=num+1
    mb.showinfo('Attendence recorded', f"Attendance of students marked !!!")
    conn.commit()


buttonSubmit = Button(app,text="Submit Data",command=submit,width="30",height="2",bg="#ad8910",borderwidth = 0)
buttonSubmit.place(x=800,y=600)
conn.commit()

#buttonSubmit = Button(app,text="Submit Data",width="30",height="2",bg="#288BA8",borderwidth = 0)
#buttonSubmit.place(x=650,y=400)

# buttonShow = Button(app,text="Show Data",width="30",height="2",bg="#ad8910",borderwidth = 0)
# buttonShow.place(x=1200,y=600)

buttonadmin = Button(app,text="Admin Data",command=admin,width="30",height="2",bg="#ad8910",borderwidth = 0)
buttonadmin.place(x=1100,y=150)

buttonsearch = Button(app,text="Search Data",command=search,width="30",height="2",bg="#ad8910",borderwidth = 0)
buttonsearch.place(x=1100,y=350)


mainloop()