#rule: no import re
import os
import requests
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import Text


def open_file (): # next: implement PDF/txt read
    datei = filedialog.askopenfilename(initialdir="/", title="select File", filetypes=(("text", ".txt"), ("PDF", ".pdf"))) #returns filepath
    pass 



def test_URL (): # next: test "no text" case
    test=str(input.get())
    if (test[0:26]=="https://www.songtexte.com/"): 
        open_URL(test)
    else:
        master.quit()



def dic_cleaner(dic):
    most_common = ["the", "be", "to" , "of", "and", "a", "in", "that", "have", "I", "in", "for", "not", "on", "with", "he", "as",
                   "you", "do", "at" , "this", "but", "his", "by", "from", "they", "we", "say", "he" , "she", "or", "an", "will",
                   "my", "one", "all", "would","there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which",
                   "go", "me", "when", "make", "can", "like", "no", "just", "him", "into", "your", "some", "could", "tham", "then",
                   "than", "now", "it's", "its", "within", "is", "i'm", "am", "i", "where", "was", "them", "", "we're", "us"]
    new_dic=dic.copy()
    for i in dic:
        if i in most_common:
            del new_dic[i]
    ac_dic=new_dic.copy()
    for j in new_dic:
        if dic[j] < 3:
            del ac_dic[j] 
    print(ac_dic)
    Diagram(ac_dic)



def open_URL (URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    text = soup.find(id="lyrics").get_text()
    print(text)
    print("\n\n")
    print("\n\n")
    LetterToWord(text)



def LetterToWord (text):
    songtext = text.lower()
    text_string1 = ""
    text_string2 = ""
    text_string3 = ""
    text_string4 = ""
    list1 = songtext.split("\n")
    for element in list1:
        text_string1 += (element + " ")
    list2 = text_string1.split(",")
    for element in list2:
        text_string2 += (element + " ")
    list3 = text_string2.split("?")
    for element in list3:
        text_string3 += (element + " ")
    list4 = text_string3.split("!")
    for element in list4:
        text_string4 += (element + " ")
    list_return = text_string4.split(" ")
    wordlist(list_return)



def wordlist (list):
    words_dic = {}
    for word in list:
        if word in words_dic:
            words_dic[word] += 1
        else:
            words_dic[word] = 1
    print(words_dic)
    print("\n\n")
    print("\n\n")
    dic_cleaner(words_dic)



def Diagram (dic):# next: delete and/the/with etc 
    words = []
    counter = []
    keys = dic.keys()
    values = dic.values()
    for i in keys:
        words.append(i)
    for j in values:
        counter.append(j)
    s = pd.Series(counter, index=words)
    s.plot(kind="bar", rot=0)
    plt.plot()
    plt.show()


   
if __name__ == "__main__":
    URL = ""
    frage = "Bitte URL der Liedtextseite eingeben:"
    master = tk.Tk()
    Label(master, text="URL").grid(row=0)
    input = Entry(master)
    input.grid(row=0, column=1)
    Button(master, text='Open File', command=open_file).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Open URL', command=test_URL).grid(row=3, column=1, sticky=W, pady=4)
    master.mainloop()
    
