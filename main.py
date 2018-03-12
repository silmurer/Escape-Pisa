# Import der Klassen, müssen sich in gleichem Ordner befinden
from floor import *
from gui import *


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

# Starten der Spielschlaufe
while True:
    main = tk.Tk()
    window = gui(main, vorplatz.get_name(), vorplatz.describe())
    main.mainloop()
