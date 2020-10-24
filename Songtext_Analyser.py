import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import Text


def open_file():
    datei = filedialog.askopenfilename(initialdir="/", title="select File", filetypes=(("text", ".txt"), ("PDF", ".pdf"))) #returns filepath
    pass 

def test_URL():
    test=str(input.get())
    if (test[0:8]=="https://"):
        print("ok")
    else:
        master.quit

def open_URL (URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="lyrics").get_text()
    wortliste(title)

def wordlist (Text):
    pass

def graph():
    pass

    

if __name__ == "__main__":
    URL = ""
    frage = "Bitte URL der Liedtextseite eingeben:"
    master = tk.Tk()
    Label(master, text="URL").grid(row=0)
    input = Entry(master)
    input.grid(row=0, column=1)
    Button(master, text='Open File', command=open_file).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Open URL', command=test_URL).grid(row=3, column=1, sticky=W, pady=4)
    #text_auslesen(URL)
    #text_auslesen("https://www.songtexte.com/songtext/manowar/black-wind-fire-and-steel-3bdf508c.html")
    master.mainloop()
    
