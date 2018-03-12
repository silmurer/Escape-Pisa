# Import der Klassen, müssen sich in gleichem Ordner befinden
from floor import *
from gui import *


def up():
    global floor_nr
    floor_nr+=1

def down():
    global floor_nr
    floor_nr = floor_nr - 1
    

# Erstellen der Stockwerk-Klassen
dach = floor("Dach", 4, "Platzhalter Infotext für Dach")
#dach.stair(glockenstube, "runter")

glockenstube = floor("Glockenstube", 3, "Platzhalter")
#glockenstube.stair()

restaurant = floor("Restaurant", 2, "Platzhalter Infotext für Restaurant")
#restaurant.stair()

erdgeschoss = floor("Erdgeschoss", 1, "Platzhalter")
#erdgeschoss.stair()

vorplatz = floor("Vorplatz", 0, "Der Vorplatz besteht aus Steinplatten. In der Mitte befindet sich ein Springbrunnen.")

plan = {4:dach, 3:glockenstube, 2:restaurant, 1:erdgeschoss, 0:vorplatz}

# Starten der Spielschlaufe
floor_nr = 4
next_floor_nr =3

loop=1

if loop == 1:
    loc = plan[floor_nr]
    next_loc = plan[next_floor_nr]
    # Grafische Oberfäche mit Klasse Window
    main = tk.Tk()
    window = gui(main, down())

    # Info zu Standort
    window.tk_l1(loc.get_name(), 0, 0)
    window.tk_l1(loc.describe(), 0, 1)

    if loc < next_loc:
        window.tk_b1("hoch", up(), 0, 2)
    else:
        window.tk_b2("runter", 1, 2)
        print(floor_nr)


    # Button für Standortwechsel


    # GUI startet
    main.mainloop()
