from sys import maxsize
from tkinter import *
import backend
from PIL import Image, ImageTk

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(food_name.get(),type.get(),cost.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(food_name.get(),type.get(),cost.get())
    list1.delete(0,END)
    list1.insert(END,(food_name.get(),type.get(),cost.get()))

def delete_command():
    backend.delete(selected_tuple[0])

# def update_command():
#     backend.update(selected_tuple[0],food_name.get(),type.get(),cost.get())

# window2=Tk()

# list1=Listbox(window2, height=20,width=50)
# list1.grid(row=2,column=0,rowspan=6,columnspan=2)

# sb1=Scrollbar(window2)
# sb1.grid(row=2,column=2,rowspan=6)

# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

# list1.bind('<<ListboxSelect>>',get_selected_row)



window=Tk()
window.geometry("520x300")
window.wm_title("Restaurent")
window.maxsize(520, 250)

# Read the Image
image = Image.open("restaurant.jpeg")
 
# Resize the image using resize() method
resize_image = image.resize((100, 100))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.grid(row=7,column=3)


l1=Label(window,text="FOODNAME",fg = "RED")
l1.grid(row=1,column=0,padx=5, pady=5)

l2=Label(window,text="TYPE",fg = "RED")
l2.grid(row=1,column=2,padx=5, pady=5)

l3=Label(window,text="COST",fg = "RED")
l3.grid(row=2,column=0,padx=5, pady=5)

food_name=StringVar()
e1=Entry(window,textvariable=food_name,bd=5)
e1.grid(row=1,column=1,padx=5, pady=5)

type=StringVar()
e2=Entry(window,textvariable=type,bd=5)
e2.grid(row=1,column=3,padx=5, pady=5)

cost=StringVar()
e3=Entry(window,textvariable=cost,bd=5)
e3.grid(row=2,column=1,padx=5, pady=5)


list1=Listbox(window, height=6,width=30,activestyle = 'dotbox', font = "Helvetica",fg = "RED")
list1.grid(row=6,column=0,rowspan=7,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=6,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,bg='green',command=view_command)
b1.grid(row=0,column=0,padx=5, pady=5)

b2=Button(window,text="Search entry", width=12,bg='blue',command=search_command)
b2.grid(row=0,column=1,padx=5, pady=5)

b3=Button(window,text="Add entry", width=12,bg='YELLOW',command=add_command)
b3.grid(row=0,column=2,padx=5, pady=5)

# b4=Button(window,text="Update selected", width=12,command=update_command)
# b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,bg='PINK',command=delete_command)
b5.grid(row=0,column=3,padx=5, pady=5)

b6=Button(window,text="Close", width=12,bg='red',command=window.destroy)
b6.grid(row=6,column=3,padx=5, pady=5)


window.mainloop()
