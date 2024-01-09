import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *
import Pyro4
import csv

def show_all():
    listBox.delete(*listBox.get_children())
    
    for i, elem in enumerate(rows, start=0):
        listBox.insert("", "end", values=(i, elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))

def show_info():
    curItem = listBox.focus()
    newWindow = Toplevel(scores)
     
    # sets the title of the
    # Toplevel widget
    newWindow.title("Info")
 
    # sets the geometry of toplevel
    newWindow.geometry("700x500")
 
    # A Label widget to show in toplevel
    text= Text(newWindow,wrap=WORD, font=("Arial",25))
    text.insert(INSERT,listBox.item(curItem))
    text.pack()

def choose_day(): 
    
    # clear the treeview
    listBox.delete(*listBox.get_children())

    label.config( text = clicked.get() ) 
    day = label.cget('text')

    for i, elem in enumerate(rows, start=0):
        if day in str(elem):
            listBox.insert("", "end", values=(i, elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))

def db_update():
    greeting_maker.db_update()



# this function creates a file that dumps the db
def dump_treeview():
    greeting_maker.db_dump()

def login_register():
    print("sono dentro login register")
    print(T1.get("1.0", "end"), T2.get("1.0", "end"), T3.get("1.0", "end"))

    greeting_maker.user_login_or_registration(T1.get("1.0", "end"), T2.get("1.0", "end"), T3.get("1.0", "end"))    

def print_all_user():
    greeting_maker.user_print_all()

    

# main
# connecting to the server
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
rows = greeting_maker.get_film()

scores = tk.Tk() 
scores.geometry("2000x650")

# create Treeview with 3 columns
cols = ('N.', 'Title', 'Direction', 'Genre', 'Duration')
listBox = ttk.Treeview(scores, columns=cols, selectmode='browse', show='headings')
listBox.pack(side='right', fill='y')

# Create a Scrollbar
scrollbar = ttk.Scrollbar(scores, orient="vertical", command=listBox.yview)
listBox.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# gestion larghezza colonne
listBox.column("N.", width=50)
listBox.column("Title", width=600)
listBox.column("Direction", width=350)
listBox.column("Genre", width=350)
listBox.column("Duration", width=220)

# fonts
style = ttk.Style()
style.configure(".", font=("Arial",25), foreground="white")
style.configure("Treeview.Heading", font=("Arial",25), foreground="white")
style.configure("Treeview", foreground='black')
style.configure("Treeview.Heading", foreground='black') #<----
style.configure('Treeview', rowheight=40)

# gestione della scelta del giorno
options = [ 
    "Lunedì", 
    "Martedì", 
    "Mercoledì", 
    "Giovedì", 
    "Venerdì", 
    "Sabato", 
    "Domenica",
    "n.d."
] 
# datatype of menu text 
clicked = StringVar() 
# initial menu text 
clicked.set( "Lunedì" ) 
# Create Label for day
label = Label( scores , text = "" )  

# set column headings
for col in cols:
    listBox.heading(col, text=col)    

# bottoni per login
T1 = Text(scores, height = 5, width = 52)
l1 = Label(scores, text = "username")
l1.config(font =("Arial",25))
T2 = Text(scores, height = 5, width = 52)
l2 = Label(scores, text = "password")
l2.config(font =("Arial",25))
T3 = Text(scores, height = 5, width = 52)
l3 = Label(scores, text = "favourite lists")
l3.config(font =("Arial",25))
T1.pack()
T2.pack()
T3.pack()

l1.pack()
l2.pack()
l3.pack()

#buttons
showScores = tk.Button(scores, text="Mostra Film", width=15, command=show_all, font=("Arial",25)).pack()
time = tk.Button(scores, text="Info", width=15, command=show_info, font=("Arial",25)).pack()
closeButton = tk.Button(scores, text="Chiudi", width=15, command=exit, font=("Arial",25)).pack(side='bottom')
drop = tk.OptionMenu(scores , clicked , *options).pack()
ApplyDayButton = tk.Button(scores , text = "Applica giorno" , command = choose_day, font=("Arial",25)).pack()
RefreshButton = tk.Button(scores, text = 'Aggiorna Database', command = db_update,font=("Arial",25)).pack()
DumpButton = tk.Button(scores, text = 'Dump Database', command = dump_treeview,font=("Arial",25)).pack()
LoginButton = tk.Button(scores, text = 'Login/Register', command = login_register,font=("Arial",25)).pack()
PrintUser = tk.Button(scores, text = 'Printuser', command = print_all_user,font=("Arial",25)).pack()

scores.mainloop()




