import sqlite3
import tkinter  as tk 
from tkinter import * 

main = tk.Tk()
main.geometry("400x250") 

conn = sqlite3.connect('attendanceStudent1.db')
c=conn.cursor()
c.execute("SELECT * FROM DataAttendance1")
r=c.fetchall()
num=2
array=[]
for i in r:
    date=Label(main,text=i[0])
    date.grid(row=num,column=0,padx=10,pady=10)

    name=Label(main,text=i[1])
    name.grid(row=num,column=1,padx=10,pady=10)

    rollno=Label(main,text=i[2])
    rollno.grid(row=num,column=2,padx=10,pady=10)

    # status=Label(main,text=i[3])
    # status.grid(row=num,column=3,padx=10,pady=10)

    radio_label=Label(main,text="A/P")
    radio_label.grid(row=num,column=4)

    radio=StringVar()
    a=Radiobutton(main,text="A",variable=radio,value="A")
    a.grid(row=num,column=5)
    a.deselect()
    p=Radiobutton(main,text="P",variable=radio,value="P")
    p.grid(row=num,column=6)
    p.deselect()
    array.append(radio.get())
    num=num+1

def submit():
    num=0
    for i in r:
        c.execute("insert into Test values('"+i[0]+"','"+i[1]+"','"+i[2]+"','"+array[num]+"')")
        num=num+1
    conn.commit()


buttonSubmit = Button(main,text="Submit Data",command=submit,width="30",height="2",bg="#288BA8",borderwidth = 0)
buttonSubmit.place(x=550,y=500)
conn.commit()
conn.close()
main.mainloop()