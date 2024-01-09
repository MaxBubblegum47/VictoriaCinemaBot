import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *

def show():
    connection = sqlite3.connect("movies.db")
    
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM example")

    rows = cursor.fetchall()
    rows.sort(key=lambda e: e[1], reverse=True)

    print(type(rows))

    for i, elem in enumerate(rows, start=1):
        listBox.insert("", "end", values=(i, elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))

def show_time():
    curItem = listBox.focus()
    print(listBox.item(curItem))

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


# main
scores = tk.Tk() 
scores.geometry("2000x650")
#label = tk.Label(scores, text="Film in Sala", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('N.', 'Title', 'Direction', 'Genre', 'Duration')
listBox = ttk.Treeview(scores, columns=cols, show='headings')



# gestion larghezza colonne
listBox.column("N.", width=50)
listBox.column("Title", width=600)
listBox.column("Direction", width=350)
listBox.column("Genre", width=350)
listBox.column("Duration", width=200)

style = ttk.Style()
style.configure(".", font=("Arial",25), foreground="white")
style.configure("Treeview.Heading", font=("Arial",25), foreground="white")
style.configure("Treeview", foreground='black')
style.configure("Treeview.Heading", foreground='black') #<----
style.configure('Treeview', rowheight=40)



# set column headings
for col in cols:
    listBox.heading(col, text=col)    

listBox.grid(row=2, column=3, columnspan=4)


showScores = tk.Button(scores, text="Mostra Film", width=15, command=show, font=("Arial",25)).grid(row=1, column=0)
time = tk.Button(scores, text="Info", width=15, command=show_time, font=("Arial",25)).grid(row=2, column=0)
closeButton = tk.Button(scores, text="Chiudi", width=15, command=exit, font=("Arial",25)).grid(row=3, column=0)


scores.mainloop()


# def first_print():
#     text = "Hello World!"
#     text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
#     text_output.grid(row=0, column=1, sticky="W")

# def second_function():
#     text = "Nuovo Messaggio! Nuova Funzione!"
#     text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
#     text_output.grid(row=1, column=1, padx=50, sticky="W")

# first_button = tk.Button(text="Saluta!", command=first_print)
# first_button.grid(row=0, column=0, sticky="W")

# second_button = tk.Button(text="Seconda Funzione", command=second_function)
# second_button.grid(row=1, column=0, pady=20, sticky="W")


