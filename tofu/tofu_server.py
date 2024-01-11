# saved as greeting-server.py
import hashlib
import Pyro4
import sqlite3
from tkinter import *
from movie import web_scraping, Even_Movie, Odd_Movie, delete_old_db
import os
import csv
from db import db_insert_user

class Tofu(object):
    @Pyro4.expose
    def get_film(self):
        print("funzione get film")
        if os.path.exists("movies.db"):
            print("DB presente")
        else:
            web_scraping()
            Even_Movie()
            Odd_Movie()

        connection = sqlite3.connect("movies.db")

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM example")

        rows = cursor.fetchall()
        rows.sort(key=lambda e: e[1], reverse=True)

        connection.close()

        return rows
    
    @Pyro4.expose
    def db_update(self):
        print("funzione update")
        delete_old_db()
        web_scraping()
        Even_Movie()
        Odd_Movie()
    
    @Pyro4.expose
    def db_dump(self):
        print("funzione dump")
        if os.path.exists("movies.db"):
            print("DB presente")
        else:
            web_scraping()
            Even_Movie()
            Odd_Movie()

        connection = sqlite3.connect("movies.db")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM example")

        with open('output.csv','w') as out_csv_file:
            csv_out = csv.writer(out_csv_file)
            # write header                        
            csv_out.writerow([d[0] for d in cursor.description])
            # write data                          
            for result in cursor:
              csv_out.writerow(result)

        connection.close()
    
    @Pyro4.expose
    def user_registration(self, name, password, favourites):
        
        try:
            # check prima di inserire i dati 
            users = Tofu.get_all_user(self)
            # elem is a tuple
            for elem in users:
                if elem[0] == name:
                    print("Utente gia' presente all'interno del database: ", elem)
                    # procedura di login
                    # chiama funzione che fa check sull'hash. Se l'hash e' corretto allora procedi a ritornare
                    # un valore che mi poi mi porta a loggare correttamente all'interno della mia interfaccia
                else:
                    db_insert_user(name, password, favourites)

            Tofu.user_print_all(self)
        except:
            print("Nuovo elemento inserito")
            db_insert_user(name, password, favourites)
        
    @Pyro4.expose
    def user_login(self, name, password, favourites):
        try:
            all_data = Tofu.user_print_all(self)
            users = Tofu.get_all_user(self)
            passwords = Tofu.get_all_hash(self)
            for elem in users:
                if elem[0] == name:
                    for elem2 in passwords:
                        if elem2[0] == password:
                            print("user logged as: ", name)

                            # print(users)
                            # print(all_data)
                            
                            connection = sqlite3.connect("users.db")

                            cursor = connection.cursor()
                            cursor.execute("UPDATE users SET favourites = ? WHERE name = ?", (favourites, name))

                            connection.close()

                            return 1
        except:
            return 0
        
        return 0

    @Pyro4.expose        
    def user_print_all(self):
        try:
            print("Sono dentro user print all")
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            print(rows)
            connection.close()
        except:
            print("Database non ancora creato")
        
    def get_all_user(self):
        try:
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM users")
            users = cursor.fetchall()
            connection.close()
        except:
            print("Database non ancora creato")
        return users
    
    def get_all_hash(self):
        try:
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM users")
            users = cursor.fetchall()
            connection.close()
        except:
            print("Database non ancora creato")
        return users
     
def main():
    daemon = Pyro4.Daemon()                # make a Pyro daemon
    ns = Pyro4.locateNS()                  # find the name server
    uri = daemon.register(Tofu)   # register the greeting maker as a Pyro object
    ns.register("example.greeting", uri)   # register the object with a name in the name server

    print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
    daemon.requestLoop()                   # start the event loop of the server to wait for calls

if __name__ == "__main__":
    main()