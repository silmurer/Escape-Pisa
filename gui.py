"""
Klasse für Grafische Oberfläche

Abkürzungen:
l = lable
m = message (mehrzeiliges Lable)
b = button
"""

# Importieren der benötigten Klassen, zur vereinfachung als 'tk'
import tkinter as tk
from tkinter import *

class gui():
    def __init__(self, master, up, down):
        
        # Übernehmen der Variablen
        self.master = master
        self.up = up
        self.down = down
        
        # Definieren einer Font vereinfacht und vereinheitlicht
        self.fdefault = "Consolas"

        # Definieren eines Abstands
        self.padydefault = 3

        # Definieren der Textvariablen, damit Labeltext geändert werden kann
        self.textvar1 = StringVar()
        self.textvar2 = StringVar()

        # Definieren der Grundsätze des Frame
        master.title("Escape Pisa - Informatik-Projekt von Silas Murer")
        master.geometry("400x650")
        master.resizable(0, 0)

        
        # Frame 1 (einziges Frame): Wird erstellt mit master = main
        self.frame = Frame(master)
        self.frame.pack()

        
        # Titelbild: Einlesen aus tower-picture.txt (ASCII (Text) Version von background.jpg)
        self.titletxt = open("tower-picture.txt", "r")
        self.titletxt = self.titletxt.read()
        self.ltitle = tk.Label(self.frame, text = self.titletxt, font = "Courier 3")
        # An dieser Stelle separat nötig, damit gelöscht werden kann
        self.ltitle.pack()

        # Button: Verlassen des Titelbildschirms, öffnen der anderen Objekte, lambda:[] zum ausführen mehrerer Befehle
        self.bstart = tk.Button(self.frame, text = "Spiel starten", font = self.fdefault,
                                command = lambda:[self.ltitle.pack_forget(), self.bstart.pack_forget(),
                                                  self.l1.pack(pady = self.padydefault), self.m1.pack(pady = self.padydefault), self.b1.pack(pady = self.padydefault), self.b2.pack(pady = self.padydefault),
                                                  bexit.pack(pady = self.padydefault),master.geometry("400x300")]
                                )
        self.bstart.pack(pady = 10)

        # Lable: Standortausgabe, textvarible wird verändert in floor.py --> direction()
        self.l1 = tk.Label(self.frame, textvariable = self.textvar1, font = self.fdefault)
        # Message: Informationsausgabe, textvarible wird verändert in floor.py --> direction()
        self.m1 = tk.Message(self.frame, textvariable = self.textvar2, font = self.fdefault, width = 400)

        # Button 1/2: Aktionsknöpfe, text und command können bei mehr Möglichkeiten durch Variablen ersezt werden
        self.b1 = tk.Button(self.frame, text = "Hoch", font = self.fdefault, command = self.up)
        self.b2 = tk.Button(self.frame, text = "Runter", font = self.fdefault, command = self.down)

        # Button exit: Schliessen des Programms
        bexit = tk.Button(self.frame, text = "Schliessen", font = self.fdefault, command = master.destroy)

    # Methode ausserhalb von __init__, damit aus direction() ausgelöst werden kann
    def b_delete(self):
            self.b1.destroy()
            self.b2.destroy()
