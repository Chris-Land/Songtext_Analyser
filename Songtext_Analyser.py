import requests
from bs4 import BeautifulSoup
import tkinter as tk

def text_auslesen (URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="lyrics").get_text()
    wortliste(title)

def wortliste (Text):
    pass

def Graphausgabe():
    pass

def tkinter_starteingabe():
    URL = ""
    frage = "Bitte URL der Liedtextseite eingeben:"
    master = tk.Tk()
    canvas = tk.Canvas(master, height=700, width=700, bg="green")
    canvas.pack( )
    frame = tk.Frame(master, bg="white") 
    frame.place(relwidth = 0.8, relheigh = 0.8,relx = 0.1, rely = 0.1 )
    
    #entry.grid()
    
    #text_auslesen(URL)
    #text_auslesen("https://www.songtexte.com/songtext/manowar/black-wind-fire-and-steel-3bdf508c.html")
    master.mainloop()

if __name__ == "__main__":
    tkinter_starteingabe()
    