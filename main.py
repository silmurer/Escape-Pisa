from stage import *
import tkinter

dach = stage("Dach")
dach.set_des("Platzhalter Infotext für Dach")

dach.get_name()
dach.get_des()



glockenstube = stage("Penthouse")
glockenstube.set_des("""Du kommst in einen dreckigen, stinkenden Raum.
Durch die dreckigen Fensterscheiben fÃ¤llt kaum Licht.
Langsam kannst du den Raum als ehemaliges Penthouse identifizieren.
An der Wand hÃ¤ngen GemÃ¤lde, der Boden besteht aus zerfezztem Teppich.""")

glockenstube.get_name
glockenstube.get_des()


restaurant = stage("Restaurant")
restaurant.set_des("Platzhalter Infotext für Restaurant")

restaurant.get_name()
restaurant.get_details()

dach.connect_stage(glockenstube, "down")
