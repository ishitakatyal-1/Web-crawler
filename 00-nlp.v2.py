
def plot_graph():
    response = urllib.request.urlopen(webadd.get())
    contents = response.read()
    #print(contents)

    soup = BeautifulSoup(contents,'html5lib')
    text = soup.get_text(strip = True)
    #print(text)

    tokens = [t for t in text.split()]
    #print(tokens)

    from nltk.corpus import stopwords
    sr = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
            freq = nltk.FreqDist(clean_tokens)
            #for key,val in freq.items():
            #    print(str(key) + ':' + str(val))

    a = freq.plot(30, cumulative=False)
    label01 = tk.Label(mainframe1, text=a)    
    
    canvas = FigureCanvasTkAgg(a)
    canvas.show()
    canvas.get_tk_widget().pack()
    label01.grid(row=3, column=0, sticky=tk.EW)
    
    
import nltk
#nltk.download()

import tkinter as tk
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import urllib.request
from bs4 import BeautifulSoup


window = tk.Tk()
window.title("Web-crawler")
window.geometry("300x300")
window.config(background="white")

mainframe1 = tk.Frame(window)
mainframe1.pack()

label00 = tk.Label(mainframe1, text="Enter the web address: ")
webadd = tk.Entry(mainframe1, background="white", width=25)
webadd.insert("end", " ")
webadd.configure(justify="right")

button00 = tk.Button(mainframe1, text="Plot", command=plot_graph)
label01 = tk.Label(mainframe1)

label00.grid(row=0, column=0, sticky=tk.EW, pady=4)
webadd.grid(row=1, column=0, columnspan=5, sticky=tk.EW)

#canvas = FigureCanvasTkAgg(a)

button00.grid(row=2, column=3, sticky=tk.EW)
label01.grid(row=3, column=0, sticky=tk.EW)
#canvas.get_tk_widget().pack()

window.mainloop()


