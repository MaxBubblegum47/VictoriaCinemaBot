import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *
import Pyro4
import csv
from ttkwidgets import CheckboxTreeview
import hashlib
from functools import partial


class tofu(tk.Frame):
    def __init__(self, root):
        root.geometry("2000x650")

        # create Treeview with 3 columns
        cols = ('N.', 'Title', 'Direction', 'Genre', 'Duration')
        self.listBox = ttk.Treeview(root, columns=cols, selectmode='browse', show='headings')
        self.listBox.pack(side='right', fill='y')

        # Create a Scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        # gestion larghezza colonne
        self.listBox.column("N.", width=50)
        self.listBox.column("Title", width=600)
        self.listBox.column("Direction", width=350)
        self.listBox.column("Genre", width=350)
        self.listBox.column("Duration", width=220)

        # fonts
        style = ttk.Style()
        style.configure(".", font=("Arial",25), foreground="white")
        style.configure("Treeview.Heading", font=("Arial",25), foreground="white")
        style.configure("Treeview", foreground='black')
        style.configure("Treeview.Heading", foreground='black') #<----
        style.configure('Treeview', rowheight=40)

        # gestione della scelta del giorno
        options = [ 
            "Tutti",
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
        self.clicked = StringVar() 
        # initial menu text 
        self.clicked.set( "Tutti" ) 
        # Create Label for day
        self.label = Label( root , text = "" )  

        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)    

        self.favourites_list = []

        self.T1 = Text(root, height = 5, width = 52)
        self.l1 = Label(root, text = "username")
        self.l1.config(font =("Arial",25))

        self.T2 = Text(root, height = 5, width = 52)
        self.l2 = Label(root, text = "password")
        self.l2.config(font =("Arial",25))

        self.T1.pack()
        self.T2.pack()

        self.l1.pack()
        self.l2.pack()

        self.login_label = Label(root, text = "utente")
        self.login_label.config(font =("Arial",25))
        self.login_label.pack()

        # old buttons
        # self.ApplyDayButton = tk.Button(root , text = "Applica giorno" , command = self.choose_day, font=("Arial",25)).pack(side='top', fill='x') # show film with particualr day
        # self.PrintUser = tk.Button(root, text = 'Printuser', command = tofu.print_all_user,font=("Arial",25)).pack(side='top', fill='x')
        # self.Login_Register_Button = tk.Button(root, text = 'Login/Register', command = tofu.login_register_window,font=("Arial",25)).pack(side='top', fill='x')    
        
        # buttons
        self.showroot = tk.Button(root, text="Mostra Film", width=15, command=self.show_all, font=("Arial",25))
        self.showroot.pack(side='top', fill='x') # show all film
        self.time = tk.Button(root, text="Info", width=15, command=self.show_info, font=("Arial",25))
        self.time.pack(side='top', fill='x') # show times slots for film
        self.closeButton = tk.Button(root, text="Chiudi", width=15, command=exit, font=("Arial",25))
        self.closeButton.pack(side='bottom') # close the app
        self.drop = tk.OptionMenu(root , self.clicked , *options)
        self.drop.pack(side='top', fill='x') # choice menu with days
        self.RefreshButton = tk.Button(root, text = 'Aggiorna Database', command = self.db_update,font=("Arial",25))
        self.RefreshButton.pack(side='top', fill='x')
        self.DumpButton = tk.Button(root, text = 'Dump Database', command = self.dump_treeview,font=("Arial",25))
        self.DumpButton.pack(side='top', fill='x')
        self.RegisterButton = tk.Button(root, text = 'Register', command = self.register,font=("Arial",25))
        self.RegisterButton.pack(side='top', fill='x')
        self.LoginButton = tk.Button(root, text = 'Login', command = self.login,font=("Arial",25))
        self.LoginButton.pack(side='top', fill='x')
        self.AddFavourite = tk.Button(root, text = 'Add Favourites', command = self.add_favourites,font=("Arial",25))
        self.AddFavourite.pack(side='top', fill='x')
        
    def show_all_helper(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
        rows = greeting_maker.get_film()

        self.listBox.delete(*self.listBox.get_children())

        for i, elem in enumerate(rows, start=0):
            self.listBox.insert("", tk.END, values=(i, elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))
        
    def show_all(self):
        self.listBox.delete(*self.listBox.get_children())

        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
        rows = greeting_maker.get_film()


        self.label.config( text = self.clicked.get() ) 
        day = self.label.cget('text')

        if day == 'Tutti':
            self.show_all_helper()
            return

        for i, elem in enumerate(rows, start=0):
            if day in str(elem):
                self.listBox.insert("", "end", values=(i, elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))

    def show_info(self):
        curItem = self.listBox.focus()
        newWindow = tk.Tk()

        # sets the title of the
        # Toplevel widget
        newWindow.title("Info")
    
        # sets the geometry of toplevel
        newWindow.geometry("700x500")
    
        # A Label widget to show in toplevel
        text= Text(newWindow,wrap=WORD, font=("Arial",25))
        text.insert(INSERT,self.listBox.item(curItem))
        text.pack()

    def db_update(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
        greeting_maker.db_update()

    def dump_treeview(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
        greeting_maker.db_dump()

    def register(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")

        username = self.T1.get("1.0", "end")
        password_hashed = self.T2.get("1.0", "end")
        password_hashed = hashlib.sha256(password_hashed.encode('utf-8')).hexdigest()

        print("username: ", username)
        print("hash: ", password_hashed)

        greeting_maker.user_registration(username, password_hashed, str(self.favourites_list))    

    def login(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")


        username = self.T1.get("1.0", "end")
        password_hashed = self.T2.get("1.0", "end")
        password_hashed = hashlib.sha256(password_hashed.encode('utf-8')).hexdigest()

        print("username: ", username)
        print("hash: ", password_hashed)

        res = greeting_maker.user_login(username, password_hashed, str(self.favourites_list))
        if res:
            print("utente loggato correttamente")
            self.login_label.config(text=username)

            self.l1.destroy()
            self.l2.destroy()
            self.T1.destroy()
            self.T2.destroy()
            self.RegisterButton.destroy()
            self.LoginButton.destroy()

        else:
            print("utente non loggato")

    def print_all_user(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")

        greeting_maker.user_print_all()

    def add_favourites(self):
        greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")

        curItem = self.listBox.focus()
        self.favourites_list.append(self.listBox.item(curItem))

def main():
    root = Tk()
    app = tofu(root)
    root.mainloop()

if __name__ == '__main__':
    main()



