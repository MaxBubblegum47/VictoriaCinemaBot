# saved as greeting-server.py
import hashlib
import Pyro4
import sqlite3
from tkinter import *
from movie import web_scraping, Even_Movie, Odd_Movie
import os

@Pyro4.expose
class Tofu(object):
    def get_film(self):
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

        return rows
    
    def db_update(self):
        web_scraping()
        Even_Movie()
        Odd_Movie()
        
def main():
    daemon = Pyro4.Daemon()                # make a Pyro daemon
    ns = Pyro4.locateNS()                  # find the name server
    uri = daemon.register(Tofu)   # register the greeting maker as a Pyro object
    ns.register("example.greeting", uri)   # register the object with a name in the name server

    print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
    daemon.requestLoop()                   # start the event loop of the server to wait for calls

if __name__ == "__main__":
    main()