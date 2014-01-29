import script
import os
currentroom = 0
rswitch = 0


###ROOM CLASS###
class room(object):
        def __init__(self, rtype, itemyn, itype):
                self.rtype = rtype
                self.itemyn = itemyn
                self.itype = itype
        def rchoice(self):
                global rswitch
                print self.rtype
                if self.itemyn == 1:
                        print "There appears to be a %s in here." % (self.itype)
                print script.lscriptReg()
                rchoice = input("> ")
                if rchoice == 1: # Room choice begins.
                        rswitch = 1
                        print "\n" * 100
                        roomLogic()
                elif rchoice == 2: # Item description begins.
                        self.itemlogic()
        def itemlogic(self):
                if self.itemyn == 1:
                        print "\n" * 100
                        if self.itype == "box":
                                print script.iscript001()
                                print "\n" * 3
                                
                else:
                        print "error"


###ROOM DEFINITIONS###

ex1 = room(script.rscript001(), 1, "box")
ex2 = room(script.rscript002(), 1, 1)



###ITEM DEFINITIONS###



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
