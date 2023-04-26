from tkinter import *
from PIL import Image, ImageTk
import tkinter as  tk
from  tkinter import  ttk
from pymongo import  *

cnx = MongoClient("mongodb://localhost:27017")
db = cnx.devowf

root=tk.Tk()
root.title("Note Management ofppt")
img=PhotoImage(file="C:\\Users\\Dell PC\\PycharmProjects\\Project_PYMONGO_G202\\school.png")
root.iconphoto(False,img)

screen_height = root.winfo_screenheight()

window_width = 1038
window_height = screen_height
window_geometry = f"{window_width}x{window_height}"
root.geometry(window_geometry)

red = 239
green = 65
blue = 102
color_code = f'#{red:02x}{green:02x}{blue:02x}'
root.configure(background=color_code)

image_file = Image.open('bg3.jpg')
image = ImageTk.PhotoImage(image_file)

label = tk.Label(root, image=image)
label.grid(row=0,column=0)

title=Label(root,text='Note Management OFPPT',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg=color_code)
title.place(x=490,y=60)

lFisrtname=Label(root,text='Fisrt name',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
lFisrtname.place(x=470,y=100)
eFisrtname=Entry(root,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg=color_code)
eFisrtname.place(x=470,y=130)

llastname=Label(root,text='last name',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
llastname.place(x=470,y=170)
elastname=Entry(root,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg=color_code)
elastname.place(x=470,y=200)

lGroup=Label(root,text='Group',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
lGroup.place(x=470,y=240)
eGroup=Entry(root,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg=color_code)
eGroup.place(x=470,y=270)

lmodulle=Label(root,text='modulle',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
lmodulle.place(x=470,y=310)
emodulle=Entry(root,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg=color_code)
emodulle.place(x=470,y=340)

lNote=Label(root,text='Note',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
lNote.place(x=470,y=380)
eNote=Entry(root,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg=color_code)
eNote.place(x=470,y=410)

tree=ttk.Treeview(root,columns=(1,2,3,4,5),height=5,show="headings")
tree.place(x=0,y=530,width=783,height=175)

tree.heading(1,text="First name")
tree.heading(2,text="Last name")
tree.heading(3,text="Group")
tree.heading(4,text="Modulle")
tree.heading(5,text="Note")



tree.column(1,width=50)
tree.column(2,width=100)
tree.column(3,width=100)
tree.column(4,width=100)
tree.column(5,width=100)


def ADD():
    cnx = MongoClient("mongodb://localhost:27017")
    db = cnx.OFPPT

    dfirstname=eFisrtname.get()
    dlastname=elastname.get()
    dgroup=eGroup.get()
    dmodulle = emodulle.get()
    dnote=eNote.get()


    data={"firstname":dfirstname,"lastname":dlastname,"group":dgroup,"modulle":dmodulle,"note":dnote}

    db.devowf.insert_one(data)


    tree.insert('', END, values=f"{data['firstname']} {data['lastname']} {data['group']} {data['modulle']} {data['note']}")

    eFisrtname.delete(0, END)
    elastname.delete(0, END)
    eGroup.delete(0, END)
    emodulle.delete(0, END)
    eNote.delete(0, END)


def DELETE():
    cnx = MongoClient("mongodb://localhost:27017")
    db = cnx.OFPPT
    selected_row = tree.selection()[0]
    values = tree.item(selected_row, 'values')
    first_column_value = values[1]
    db.devowf.delete_one({'lastname': first_column_value})
    print(f" {first_column_value}")

    selection = tree.selection()
    if selection:
        for itemm in selection:
            tree.delete(itemm)

def DELETE_ALL():
    cnx = MongoClient("mongodb://localhost:27017")
    db = cnx.OFPPT
    for data in tree.get_children():
        tree.delete(data)
    db.devowf.delete_many({})



def show():
    cnx = MongoClient("mongodb://localhost:27017")
    db = cnx.OFPPT
    donnee = db.devowf.find()

    for data in tree.get_children():
        tree.delete(data)

    for elt in donnee:
        tree.insert('', END, values=f"{elt['firstname']} {elt['lastname']} {elt['group']} {elt['modulle']} {elt['note']}")


def update():
    cnx = MongoClient("mongodb://localhost:27017")
    db = cnx.OFPPT
    donnee=db.devowf.find()

    dfirstname = eFisrtname.get()
    dlastname = elastname.get()
    dgroup = eGroup.get()
    dmodulle = emodulle.get()
    dnote = eNote.get()

    db.devowf.update_one({"lastname":dlastname},{"$set":{"modulle":dmodulle,"note":dnote,"group":dgroup}})

    for data in tree.get_children():
        tree.delete(data)

    for elt in donnee:
      tree.insert('', END, values=f"{elt['firstname']} {elt['lastname']} {elt['group']} {elt['modulle']} {elt['note']}")

    eFisrtname.delete(0, END)
    elastname.delete(0, END)
    eGroup.delete(0, END)
    emodulle.delete(0, END)
    eNote.delete(0, END)

def select():
    selected_row = tree.selection()[0]
    values = tree.item(selected_row, 'values')
    eFisrtname.insert(0, values[0])
    elastname.insert(0, values[1])
    eGroup.insert(0, values[2])
    emodulle.insert(0, values[3])
    eNote.insert(0, values[4])






addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,bd=5, font=('Arial', 15), bg="#84F894" ,command=ADD)
addBtn.place(x=785, y=0)

deletBtn = Button(
    root, text="delet", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999" ,command=DELETE)
deletBtn.place(x=785, y=200,)

showBtn = Button(
    root, text="All Data", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82",command=show)
showBtn.place(x=785, y=300,)

delet_allBtn = Button(
    root, text="delet all", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF",command=DELETE_ALL)
delet_allBtn.place(x=785, y=400,)

updateBtn = Button(
    root, text="update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8" ,command=update)
updateBtn.place(x=785, y=100,)

selectBtn = Button(
    root, text="select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8",command=select)
selectBtn.place(x=785, y=500,)

BY1=Label(root,text='BY souhayb Ajelian G202',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
BY1.place(x=785,y=600)
BY2=Label(root,text='AND abdeslam Afellad G202',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg=color_code)
BY2.place(x=785,y=630)

root.mainloop()

