"""
Klasse für Stockwerke
"""
class floor():

    # Jede floor-Instanz enthält den Namen und Nummer
    def __init__(self, floor_name, *floor_nr):
        self.name = floor_name
        self.nr = floor_nr
        
    # Info-Methode. Wird als Beschreibung angezeigt, wenn der Zugriff auf anderer Infos nicht klappt
    def __repr__(self):
        return "Objekt: " + self.name + " im " + str(self.nr) + ". Stockwerk aus der __repr__"
    
    # Rückgabe des Namens
    def get_name(self):
        return(self.name)

    # Rückgabe der Stockwerknummer (vereinfacht auslesen des Stockewerks und wird für Inventar-Zuweisung wichtig)
    def get_nr(self):
        return(self.nr)

"""
Klasse für Positionsbestimmung / Positionswechsel
"""
class direction():
    def __init__(self, plan):

        # Alle wichtigen benutzten Variablen werden hier der Übersicht wegen aufgelistet, ebenso wie der Zusammenhang
        self.floor_nr = 5
        self.floor_describe = 2
        # Muss aus main.py übernommen werden, da sonst Klassen nicht definiert sind
        self.plan = plan
        # loc = locatoin, es wird aus plan[] der Start ausgewählt
        self.loc = self.plan[self.floor_nr]
        # Zur Anzeige in textvar1/2 muss es in einen eigenen String umgewandelt werden
        self.floorname = self.loc.get_name()
        self.describe = None
        self.stay = None
        # An dieser Stelle können weitere Spezielle Counter,... erstellt werden
        self.assassin = 0
        self.gui = None

        # Einlesen der Beschreibung in Liste, aus description.txt ohne newline = '\n'
        self.textlist = [line.rstrip('\n') for line in open("description.txt", "r")]
        # Festlegen des Startpunkts
        self.describe = self.textlist[2]

        # Definiert, welche Text-Schlaufe gewählt wird, zuerst auf 0 gesetzt, bis update() funktioniert hat
        self.i = 0
        
    # Klasse 'window' kann vorher nicht eingelesen werden, nun darf self.i = 1 werden
    def update(self, gui):
        self.gui = gui
        self.i = 1
        self.get_text()

    """
    Abhängig von self.i werden verschiedene Texte angezeigt / können Aktionen durchgeführt werden
    textvar1 = Location oder Aktion (Titel)
    textvar2 = Beschreibung, wird aus der self.textlist (=description.txt) rausgelesen
    """
    def get_text(self):

        # Standart, ein Normaler Textwechsel wird vorgenommen
        if self.i == 1:
            self.gui.textvar1.set(self.floorname)
            self.gui.textvar2.set(self.describe)

        # Ende von Plan wurde erreicht, bleibt am gleichen Ort, bekommt Hinweis
        elif self.i == 2:
            self.gui.textvar2.set(self.stay)

        # Tod, Spiel ist fertig, kann durch verschiedene Aktionen aufgerufen werden
        elif self.i == 3:
            self.gui.textvar1.set("Gestorben")
            self.gui.textvar2.set(self.textlist[12])
            # Spiel vorbei, Aktionsbuttons verschwinden
            self.gui.b_delete()

        # Spezielles Easteregg, zur Vereinfachung wird hier ein eigenes elif mit festem Namen/Beschreibung definiert  
        elif self.i == 4:
            self.gui.textvar1.set("Assassine")
            self.gui.textvar2.set(self.textlist[13])
            # Spiel vorbei, Aktionsbuttons verschwinden
            self.gui.b_delete()

        # Normales Spielende
        elif self.i == 0:
            self.gui.textvar1.set(self.floorname)
            self.gui.textvar2.set(self.describe)
            # Spiel vorbei, Aktionsbuttons verschwinden
            self.gui.b_delete()

        # Falls Fehler auftritt, wird neu geladen
        else:
            self.gui.textvar1.set(self.floorname)
            self.gui.textvar2.set(self.describe)
            
        # self.i muss für den nächsten Durchlauf zurückgesetzt werden
        self.i = 1

        

    # Zwei Beispielfunktionen: up() = im Plan nach oben, down() = im Plan nach unten    
    def up(self):
        
        # if-else als Begrenzung der möglichen Orte für Standart-Aktion (self.i = 1)
        if self.floor_nr == 4 or self.floor_nr < 2:
            # self.floor_nr wird geändert für neuen Standort in Liste: plan[]
            self.floor_nr += 1
            self.loc = self.plan[self.floor_nr]
            self.floorname = self.loc.get_name()
            self.floor_describe -= 1
            self.describe = self.textlist[self.floor_describe]
            
        # Aktion: Spieler stirbt
        elif self.floor_nr < 4:
            # Da Aktion immer gleich ausgeht, wird lediglich self.i geändert
            self.i = 3
            
        # Aktion: Spezielles
        elif self.floor_nr == 5 and self.assassin == 1:
            # Wieder nur self.i ändern
            self.i = 4
            
        # Für Übersichtlichkeit wird hier self.stay verwendet
        else:
            self.stay = self.textlist[9]
            self.floor_nr = 5
            self.i = 2
            self.assassin = 1

        self.get_text()

            
    def down(self):
        
        # if-else als Begrenzung der möglichen Orte für Standart-Aktion (self.i = 1)
        if self.floor_nr > 1:
            self.floor_nr -= 1
            self.loc = self.plan[self.floor_nr]
            self.floorname = self.loc.get_name()
            self.floor_describe += 1
            self.describe = self.textlist[self.floor_describe]

        # Durch ändern von self.floor_nr = 0 kann jederzeit das normale Ende aufgerufen werden
        elif self.floor_nr == 1:
            self.loc = self.plan[0]
            self.floorname = self.loc.get_name()
            self.describe = self.textlist[7]
            self.i = 0
            
        # Für Übersichtlichkeit wird hier self.stay verwendet
        else:
            self.stay = self.textlist[10]
            self.floor_nr = 0
            self.i = 2
            
        self.get_text()
