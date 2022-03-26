from tkinter import *
from sql import *
from tkinter import messagebox
A=Tk()
A.title("restaurant")
A.geometry("700x500")

frame3 = Frame(A,bg="#fcf36f")
frame2 = Frame(A,)
image = PhotoImage(file="back.gif")

A["background"]="#fcf36f"

def add_sql():
    add(Pizza_search.get(),large.get(),small.get(),medium.get())
    messagebox.showinfo(title="pizza",message="item added successfully")

def view_sql ():
    Menu.delete(0,END)
    for i in view():
        Menu.insert(END,i)

def search_sql():
    Menu.delete(0,END)
    for i in search(Pizza_search.get()):
        Menu.insert(END,i)

def ID (x):
    print("hello")
    global get_id
    F=Menu.curselection()
    get_id=Menu.get(F)
    large.delete(0, END)
    medium.delete(0, END)
    small.delete(0, END)
    Pizza_search.delete(0, END)

    Pizza_search.insert(0, get_id[1])
    large.insert(0, get_id[2])
    medium.insert(0, get_id[3])
    small.insert(0, get_id[4])

def Delete_sql():
    delete(get_id[0])
    messagebox.showinfo(title="item",message="item deleted successfully")


def update_sql():
    update(get_id[0],get_id[1],get_id[2],get_id[3],get_id[4])
    messagebox.showinfo(title="item", message="item updated successfully")









def admin():
    global frame2
    global frame3
    global Menu
    global large
    global small
    global medium
    global Pizza_search
    frame3=Frame(A, bg="#fcf36f")
    frame2 = Frame(A, bg="#fcf36f")
    frame.destroy()
    Add = Button(frame2, text="Add", bg="#6e0000", fg="#ffa200", font=("Itim"),command=add_sql)
    Update = Button(frame2, text="Update", bg="#6e0000", fg="#ffa200", font=("Itim"),command=update_sql)
    Delete = Button(frame2, text="Delete", bg="#6e0000", fg="#ffa200", font=("Itim"),command=Delete_sql)
    Search = Button(frame2, text="search", bg="#6e0000", fg="#ffa200", font=("Itim"),command=search_sql)
    View = Button(frame2, text="view", bg="#6e0000", fg="#ffa200", font=("Itim"),command=view_sql)
    Pizza_search=Entry(frame3,)
    Small_L=Label(frame3,text="small",bg="#fcf36f")
    medium_L = Label(frame3, text=" medium",bg="#fcf36f")
    large_L = Label(frame3, text="large",bg="#fcf36f")
    pizza_type=Label(frame3,text="pizza",bg="#fcf36f")
    Small_L.grid(row=0,column=0)
    medium_L.grid(row=1, column=0)
    large_L.grid(row=2, column=0)
    pizza_type.grid(row=3,column=0)

    back = Button(A,image=image, bd=0, command=Home)
    frame3.pack()
    frame2.pack()
    Menu = Listbox(A, bg="#fcf36f", fg="#ffa200", height=10, width=40)
    large = Entry(frame3, )
    medium = Entry(frame3, )
    small = Entry(frame3, )
    Add.pack(side="left")
    Update.pack(side="left")
    Delete.pack(side="left")
    View.pack(side="left")
    Search.pack(side="left")
    Menu.pack()
    large.grid(row=0,column=1)
    medium.grid(row=1,column=1)
    small.grid(row=2,column=1)
    Pizza_search.grid(row=3,column=1)
    back.place(relx=0, rely=0)
    Menu.bind("<<ListboxSelect>>", ID)
def Client():
    global frame2
    global frame3
    global Menu
    frame3 = Frame(A, bg="#fcf36f")
    frame2 = Frame(A, bg="#fcf36f")
    Pizza_L = Label(frame3, text="pizza", bg="#fcf36f")
    Pizza_L.grid(row=0,column=0)
    frame.destroy()
    back = Button(A, image=image, bd=0, command=Home)
    frame3.pack()
    frame2.pack()
    Menu = Listbox(A, bg="#fcf36f", fg="#ffa200", height=10, width=40)
    Search = Button(frame2, text="search", bg="#6e0000", fg="#ffa200", font=("Itim"),command=search_sql)
    View = Button(frame2, text="view", bg="#6e0000", fg="#ffa200", font=("Itim"),command=view_sql)
    Pizza_search = Entry(frame3, width=40)
    View.pack(side="left")
    Search.pack(side="left")
    Menu.pack()
    Pizza_search.grid(row=0,column=1)
    back.place(relx=0,rely=0)
    Menu.bind("<<ListboxSelect>>", ID)


def Home ():
    global frame
    frame = Frame(A, )
    welcome = Label(A, text="Welcome to our restaurant", bg="#fcf36f", fg="#ffa200", font=("Itim", 30))
    Admin = Button(frame, text="Admin", bg="#6e0000", fg="#ffa200", font=("Itim"), command=admin)
    client = Button(frame, text="client", bg="#6e0000", fg="#ffa200", font=("Itim"), command=Client)
    welcome.pack()
    frame.pack()
    Admin.grid(row=0, column=0)
    client.grid(row=0, column=1)
    print(frame3.winfo_children())
    if len(frame3.winfo_children()) !=0:
         print("ab")
         frame2.destroy()
         frame3.destroy()
         Menu.destroy()
         welcome.destroy()


Home()










A.mainloop()