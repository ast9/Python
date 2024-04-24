import csv
import os.path
from tkinter import *
from datetime import datetime

window = Tk()
window.geometry("1200x800")
window.title("My To-Do-List")

input1 = StringVar()

window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=9)
window.grid_rowconfigure(0, weight=1)

data = []
fields = ['newtask', 'date']
filepath = 'todo.csv'


def open_csv():
    global data
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    else:
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)


def input_data():
    newtask = input1.get()
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    data.append({"newtask": newtask, "date": date})
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        for row in data:
            writer.writerow([row['newtask'], row['date']])
    input1.set("")


def title_top(text):
    title_top = Label(body, text=text, font=(None, 50, "bold"), fg="#ffffff", bg="#000000")
    title_top.grid(column=0, row=0, columnspan=3, padx=100, pady=(50, 0), sticky="w")

def complete_task():
    pass

def destory_body_frame():
    for i in body.winfo_children():
        i.destroy()


def add_new():
    destory_body_frame()
    title_top("Add New Task")
    title = Label(body, text="Write the desription about your task", bg="#000000", fg="#ffffff",
                  font=(None, 17, "bold"))
    title.grid(column=0, row=1, columnspan=3, sticky="nw", padx=100, pady=(180, 0))

    entry_task_desc = Entry(body, textvariable=input1)
    entry_task_desc.grid(column=0, row=2, columnspan=3, sticky="we", pady=10, padx=100)

    btn_save = Button(body, text="Save Task", bg="#802e2a", fg="#ffffff", command=input_data,
                      highlightbackground="#000000")
    btn_save.grid(column=0, row=3, columnspan=3, padx=100, pady=5, sticky="w")
    entry_task_desc.focus()

def search():
    destory_body_frame()
    title_top("Search")
    title = Label(body,text="Write a keyword",bg="#000000",fg="#ffffff",font=(None,17,"bold"))
    title.grid(column=0,row=1,columnspan=3,sticky="nw",padx=100,pady=(180,0))
    entry_task_desc = Entry(body)
    entry_task_desc.grid(column=0,row=2,columnspan=3,sticky="we",pady=10,padx=100)
    btn_save = Button(body,text="Search",bg="#802e2a",fg="#ffffff",command=input_data,highlightbackground="#000000")
    btn_save.grid(column=0,row=3,columnspan=3,padx=100,pady=5,sticky="w")
    entry_task_desc.focus()

def today():
    destory_body_frame()
    title_top("Today")

    curr_row = 1
    desc_top = Label(body, text="Don't Forget to Do Your Tasks Today!", fg="#b8b8b8", bg="#000000")
    desc_top.grid(column=0, row=curr_row, columnspan=3, sticky="w", padx=(100, 10), pady=(10, 5))
    curr_row += 1

    tasktoday_label = Label(body, text="Today Tasks", fg="#b8b8b8", bg="#000000", font=(None, 16, "bold"))
    tasktoday_label.grid(column=0, row=curr_row, columnspan=3, sticky="w", padx=(100, 10), pady=(10, 5))
    curr_row += 1

    today_task = IntVar()

    dummy = ["Send reports to the manager", "Get a breakfast", "Pick up a coffe", "Meeting with client",
             "Get a lunch", "Watch Godzilla movie"]

    for id, task in enumerate(dummy):
        cb = Radiobutton(body, text=task, variable=today_task, value=id, command=complete_task, bg="#000", fg="#ffffff")
        cb.grid(column=0, row=curr_row, columnspan=3, padx=(100, 10), pady=5, sticky="w")
        curr_row += 1

    for task in data:
        cb = Radiobutton(body, text=task['newtask'], variable=today_task, value=task['newtask'], command=complete_task,
                         bg="#000", fg="#ffffff")
        cb.grid(column=0, row=curr_row, columnspan=3, padx=(100, 10), pady=5, sticky="w")
        curr_row += 1

sidebar = Frame(window, bg="#2d2d2e")
sidebar.grid(column=0, row=0, sticky="nwse")
sidebar.grid_propagate(False)

body = Frame(window, bg="#000000")
body.grid(column=1, row=0, sticky="nwse")
body.grid_propagate(False)

sidebar.grid_columnconfigure(0, weight=1)
sidebar.grid_columnconfigure(1, weight=40)
curr_row = 0

canvas = Canvas(sidebar, height=100, bg="#2d2d2e", bd=0, highlightthickness=0)
img = PhotoImage(file="D:/VSC/PY/todo.png")
canvas.grid(column=0, row=curr_row, columnspan=2, sticky="e")
canvas.create_image(10, 10, image=img, anchor="nw")
curr_row += 1

btn_add = Button(sidebar, text="+ Add New Task", bg="#802e2a", fg="#ffffff", command=add_new)
btn_add.grid(column=0, row=curr_row, columnspan=2, sticky="we", padx=10, pady=10)
curr_row += 1

im1 = PhotoImage(file="D:/VSC/PY/search.png")
btn_search = Button(sidebar,text="",bg="#474747",fg="#fff",image=im1,command=search)
btn_search.grid(column=0,row=curr_row,sticky="w",padx=(10,0))
label_search = Label(sidebar,text="Search",bg="#2d2d2e",fg="#fff")
label_search.grid(column=1,row=curr_row,sticky="w")
curr_row += 1

im2 = PhotoImage(file="D:/VSC/PY/today.png")
btn_today = Button(sidebar,text="",bg="#474747",fg="#fff",image=im2,command=today)
btn_today.grid(column=0,row=curr_row,sticky="w",padx=(10,0))
label_today = Label(sidebar,text="Today",bg="#2d2d2e",fg="#fff")
label_today.grid(column=1,row=curr_row,sticky="w")
curr_row += 1


sidebar.grid_columnconfigure(0, weight=1)
sidebar.grid_columnconfigure(1, weight=40)
curr_row = 0

open_csv()

window.mainloop()
