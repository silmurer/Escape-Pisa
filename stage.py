# Alle Klassen die im Hauptprogramm verwendet werden

# Definition der Klasse
# des = description

class stage():
    def __init__(self, stage_name):
        self.name = stage_name
        self.des = None
        self.stair = {}

    def get_name(self):
        return self.name

    def set_des(self, stage_des):
        self.des = stage_des

    def get_des(self):
        return self.des

    def get_details(self):
        print(self.name)
        print("\n")
        print(self.des)

    def connect_stage(self, next_stage, direction):
        self.stair = next_stage

######################################################################

    def stair(self, next_stage, des):
        self.stair["Treppe runter"] = next_stage
        print(self.name + "Mögliche Stockwerke:" + rep(self.stair))

    def get_detail(self):
        print(self.name)
        print(self.des)
        for direction in self.stair:
            a=0

    def move(self, stair):
        if ... in self.stair(direction):
            return self.stair[direction]
        else:
            print("Dieser Weg ist versperrt")
            return self
    

#class inventory():
#    def __init__(self, xxx):

#class view():
#    def __init__(self, disc_place, undis_place):

