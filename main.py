import script
currentroom = 0
rswitch = 0

###ROOM CLASS###
class room(object):
    def __init__(self, rtype):
        self.rtype = rtype
    def rchoice(self):
        global rswitch
        print self.rtype
        print script.lscriptReg()
        rchoice = input("> ")
        if rchoice == 1: # Room choice begins.
            rswitch = 1
            roomLogic()
        
        
        


###ROOM DEFINITIONS###
ex1 = room("test")
ex2 = room("test2")


###ROOM LOGIC###
def roomLogic():
    global currentroom
    global rswitch
    if rswitch == 0: # Room switch is not necessary. Begin room description.
        if currentroom == 0:
            ex1.rchoice()
        else:
            ex2.rchoice()
    else: # Room switch is necessary. Begin room switch.
        rswitch = 0
        if currentroom == 0:
            currentroom = 1
        else:
            currentroom = 0
        roomLogic()

###BEGIN###
roomLogic()
