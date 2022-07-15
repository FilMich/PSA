#!/usr/bin/env python3

from flask import Flask

KNIHY = [
    {"id": 0, "nazov": "Harry potter 1", "popis": "Harry Potter a kamen mudrcov"},
    {"id": 1, "nazov": "Harry potter 2", "popis": "Harry Potter a tajomna komnata"},
    {"id": 2, "nazov": "Python for dummies", "popis": "starting with python"}
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>zuvakkkkk</h1> \n <h2>je picovina</h2>"

@app.route("/knihy", methods=["GET"])
def dajKnihy():
    vystup = ""
    for kniha in KNIHY:
        vystup += "Nazov: {}, popis: {}\n".format(kniha["nazov"], kniha["popis"])
    return vystup, 200

@app.route("/knihy/<int:paID>", methods=["GET"])
def dajKnihu(paID):
    vystup = ""
    for kniha in KNIHY:
        if(paID == kniha["id"]):
            vystup += "Nazov: {}, popis: {}\n".format(kniha["nazov"], kniha["popis"])
            return vystup, 200
    return "NOT FOUND", 404


if __name__ == "__main__":
    app.run("0.0.0.0", 8888)