from bs4 import BeautifulSoup
import requests
import re

class Film:
    def __init__(self, poster, time_slots, reservation):
        self.poster = poster # all data about the movie
        self.time_slots = time_slots # day and time of movie 
        self.reservation = reservation # link for reservate a seat

    def Odd_Movie():
        url = "https://www.victoriacinema.it/victoria_cinema/index.php"
        body = requests.get(url)
        body_text = body.content
        soup = BeautifulSoup(body_text, 'lxml')     
        divsOdd = soup.find_all("div", class_="filmContainer oddFilm")
        messageOdd = ""
        result_list = []

        #oddFilm loop
        for div in divsOdd:
            idfilm = div.find_all("div",  class_="scheda")
            idfilm = re.findall(r"\D(\d{5})\D", str(idfilm))
            poster = ""
            time_slots = []
            reservation = ""

            divs3 = div.find_all("div", class_="datiFilm")
            #Film data
            for div1 in divs3:
                reservation = "https://www.victoriacinema.it/generic/scheda.php?id=" + str(idfilm).strip("['']") + "&idcine=1760&idwt=5103#inside"
                for clean_strip in list (div1.stripped_strings):
                    poster += " " + clean_strip
            
            #getting the day and the time for each film in the theater
            divs2 = div.find_all("ul", class_="orari")
            for div2 in divs2:
                for clean_strip in list(div2.stripped_strings):
                    time_slots.append(clean_strip)

            f = Film(poster, time_slots, reservation)
            messageOdd = f.poster + "\nProiezioni:\n" + "".join(str("\n" + elem + ":\n") if elem.isalpha() else str(elem + "   ") for elem in f.time_slots )+ "\nLink Prenotazione:\n" + f.reservation +"\n\n\n"
            result_list.append(messageOdd)
        return result_list

    def Even_Movie():
        url = "https://www.victoriacinema.it/victoria_cinema/index.php"
        body = requests.get(url)
        body_text = body.content
        soup = BeautifulSoup(body_text, 'lxml')
        divsEven = soup.find_all("div", class_="filmContainer evenFilm")
        messageEven = ""
        result_list = []

        #evenFilm loop
        for div in divsEven:
            idfilm = div.find_all("div",  class_="scheda")
            idfilm = re.findall(r"\D(\d{5})\D", str(idfilm))
            poster = ""
            time_slots = []
            reservation = ""

            divs3 = div.find_all("div", class_="datiFilm")
            #Film data
            for div1 in divs3:
                reservation = "https://www.victoriacinema.it/generic/scheda.php?id=" + str(idfilm).strip("['']") + "&idcine=1760&idwt=5103#inside"
                for clean_strip in list (div1.stripped_strings):
                    poster += " " + clean_strip
            
            #getting the day and the time for each film in the theater
            divs2 = div.find_all("ul", class_="orari")
            for div2 in divs2:
                for clean_strip in list(div2.stripped_strings):
                    time_slots.append(clean_strip)
            
            f = Film(poster, time_slots, reservation)
            messageEven = f.poster + "\nProiezioni:\n" + "".join(str("\n" + elem + ":\n") if elem.isalpha() else str(elem + "   ") for elem in f.time_slots )+ "\nLink Prenotazione:\n" + f.reservation +"\n\n\n"
            result_list.append(messageEven)
        return result_list