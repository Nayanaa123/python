import mysql.connector
from tkinter import *
import tkinter.messagebox as message
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="infoo")
cur=conn.cursor()
def save():
  n=e1.get()
  a=e2.get()
  p=e3.get()
  if n=="" or a==""or p=="":
    message.showinfo("insert data","please fill all fields")
  cur.execute("INSERT INTO PERSONALINFO VALUE('%s','%s','%s');"%(n,a,p))
  conn.commit()
  print("save data sucessfully")
def delete():
  n=e1.get()
  if n=="":
    message.showinfo( "insert data","please fill all fields")
    
window=Tk()
window.title("welcome")
window.geometry("220x300")  
window.resizable(False,False)
window.configure(background="pink")
window.attributes("-topmost",True)
window.attributes("-alpha",0.9)
window.iconbitmap("favicon.ico")
lbl1=Label(text=" name:-  ")
lbl1.place(x=20,y=30)
lbl2=Label(text="address:-")
lbl2.place(x=20,y=50)
lbl3=Label(text=" phone:- ")
lbl3.place(x=20,y=70)
e1=Entry()
e1.place(x=80,y=30)
e2=Entry()
e2.place(x=80,y=50)
e3=Entry()
e3.place(x=80,y=70)
btn=Button(text="  save  ",command=save)
btn.place(x=85,y=100)
btn1=Button(text="  del  ",command=delete)
btn1.place(x=150,y=100)
window.mainloop()
