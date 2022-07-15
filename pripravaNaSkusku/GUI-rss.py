#!/usr/bin/env python
import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
import urllib.request as URL_Req
import xml.etree.cElementTree as XML_Tree

def parsujRSS(paURL):
    otvorene_rss = URL_Req.urlopen(paURL)
    stranka = otvorene_rss.read()

    koren = XML_Tree.fromstring(stranka)
    retazec = ""
    for channel in koren:
        for item in channel:
            if item.tag != "item":
                continue
            title = ""
            desc = ""
            link = ""
            date = ""
            for polozka in item:
                if polozka.tag == "title":
                    title = polozka.text
                elif polozka.tag == "description":
                    desc = polozka.text
                elif polozka.tag == "link":
                    link = polozka.text
                elif polozka.tag == "pubDate":
                    date = polozka.text
            retazec += "Nadpis: {} . {}, URL: {}. {}\n\n".format(title, desc, link, date)
    return retazec