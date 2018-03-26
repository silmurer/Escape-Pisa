"""
Main erstellt alle Instanzen, hier starte man auch das Game
"""
# Import der Klassen, müssen sich in gleichem Ordner befinden
from floor import *
from gui import *

"""
Alle benötigten Orte werden erstellt und verknüpft
"""
# Erstellen der Stockwerk-Klassen aus 'floor'
dach = floor("Dach", 4)
glockenstube = floor("Glockenstube", 3)
restaurant = floor("Restaurant", 2)
erdgeschoss = floor("Erdgeschoss", 1)
vorplatz = floor("Vorplatz", 0)
ende = floor("Ende")

# plan[] muss hier erstellt werden, kann jederzeit erweitert werden
plan = [ende, vorplatz, erdgeschoss, restaurant, glockenstube, dach]

# Erstellen der Position-Klasse aus 'floor'
direction = direction(plan)

"""
GUI und somit Schleife und Spiel an sich werden gestartet
"""
# Erstellen der Grafische Oberfäche-Klasse aus 'gui' mit Master: 'main'
main = tk.Tk()
window = gui(main, direction.up, direction.down)

# Instanz der Klasse direction() muss durch diese Funktion mit der Instanz der Klasse gui() upgedatet werden
direction.update(window)

# GUI-Loop starten, ab jetzt sind alle Änderungen nur noch aktiv
main.mainloop()
