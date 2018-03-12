# Klasse für Stockwerke

# Definition der Klasse
class floor():
    def __init__(self, floor_name, floor_nr, floor_description):
        self.name = floor_name
        self.nr = str(floor_nr)
        self.description = floor_description
        self.next_floor = {}

    # Info-Methode
    def __repr__(self):
        return "Objekt: " + self.name + " im " + self.nr + ". Stockwerk"

    # Rückgabe des Namens (für GUI)
    def get_name(self):
        return(self.name)

    # Rückgabe der Beschreibung (für GUI)
    def describe(self):
        return(self.description)        

    # Verbindung der Etagen
    def stair(self):
        self.next_floor[direction] = connected
        print(self.name + "Mögliche Stockwerke:" + rep(self.stair))
        if self.nr == 1:
            return self.next_floor[direction]
        else:
            print("Du kannst hier nicht lang gehen")
            return self

######################################################################

#class inventory():
#    def __init__(self, xxx):

#class view():
#    def __init__(self, disc_place, undis_place):

