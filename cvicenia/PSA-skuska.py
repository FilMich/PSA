#!/usr/bin/env python

import tkinter
import requests

def pridajKnihu():
    nazovAPopis = pole.get().split(" ")
    requests.post('http://localhost:8888/knihy', json={"nazov":nazovAPopis[0], "popis":nazovAPopis[1]})

root = tkinter.Tk()
nazov = tkinter.Label(root, text="Zadaj nazov a popis knihy : ")
nazov.pack()
pole = tkinter.Entry(root, width=100)
pole.pack()
tlacitko = tkinter.Button(root, text='Pridaj novu knihu', command=pridajKnihu)
tlacitko.pack()
root.mainloop()