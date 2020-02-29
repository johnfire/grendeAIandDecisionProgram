#!/usr/bin/python3
# main grendel one AI loop, drives all higher level thinking
# by Christopher Rehm christopherrehm@web.de
# released under the gnu public license number 3
# started 15 feb 2020

import os
import sys
import time
import json
import grendelconfig as gc

#######################################
#main decision program for grendel the robot
class thing():

    def __init__(self):
        gc.debugBreakPoint("in init for thing ", "decisionProgram.py")
        self.name = ""
        self.currentLocation = ""
        self.mass = ""
        self.living = ""
        self.intellegent = ""
        self.tangible = ""
        self.dims = []

#######################################
class person(thing):

    def __init__(self):
        gc.debugBreakPoint("in init for person ", "decisionProgram.py")
        self.number = ""
        self.sex = ""
        self.job = ""
        self.trustRating = ""
        self.HomeLocation = ""
        self.WorkLocation = ""
        self.picture = ""
        self.height = ""
        self.weight = ""
        self.color = ""
        self.hairColor = ""
        self.eyeColor = ""
        self.relationship2Me = ""
        self.importantIdeas = []
        self.importantThoughts = []
        self.hobbies = []
        self.likes = []
        self.dislikes = []
        self.loves = []
        self.favoritePlaces = []
        self.history = []
        self.school = []
        self.degrees = []
        self.skills = []
        self.experience = []
        self.family = []
        self.friends = []
        self.conversatons = []
        self.commonExperiences = []

#####################################
class anObject(thing):

    def __init__(self):
        gc.debugBreakPoint("in init for anObject ", "decisionProgram.py")
        self.function = ""
        self.color = ""
        self.size = ""
        self.dims = []
        self.dangers = []
        self.uses = []

######################################
class animal(thing):

    def __init__(self):
        gc.debugBreakPoint("in init for animal ", "decisionProgram.py")
        self.family = ""

######################################
class plant(thing):

    def __init__(self):
        gc.debugBreakPoint("in init for plant ", "decisionProgram.py")
        self.family = ""

######################################
class otherLife(thing):

    def __init__(self):
        gc.debugBreakPoint("in init for otherLife ", "decisionProgram.py")
        self.family = ""

######################################
class idea(thing):

    def __init__(self):
        gc.debugBreakPoint("in init for idea ", "decisionProgram.py")
        self.discription = ""

######################################
class myMorals(idea):

    def __init__(self):
        gc.debugBreakPoint("in init for myMorals ", "decisionProgram.py")
        self.listOfMorals = []

######################################
class myGoals(idea):

    def __init__(self):
        gc.debugBreakPoint("in init for myGoals ", "decisionProgram.py")
        self.listOfShortTermGoals = []
        self.listOfMedTermGoals = []
        self.listOfLongTermGoals = []

######################################
class aPlace(thing):

    def __init__(self):
        gc.debugBreakPoint("in init aPlace ", "decisionProgram.py")
        #size, numpy array
        self.vectorFromHome = []
        self.otherVectorList = []

######################################
######################################
class myWorld (thing):

    ###################################

    def __init__(self):
        gc.debugBreakPoint("in init for myWorld ", "decisionProgram.py")
        self.currentModelTime =""
        self.peopleList = []
        self.objectList = []
        self.placeList = []
        self.animalList = []
        self.plantList = []
        self.otherLifeList = []
        self.currentPlace = "home"

    ###################################
    def firstInit(self):
        gc.debugBreakPoint("in init for first initialisation myWorld ", "decisionProgram.py")
        dummy0 = person("empty person")
        self.peopleList.append(dummy0)
        dummy1 = anObject("blank object")
        self.objectList.append/dummy1
        dummy2 = aPlace("empty place")
        self.placeList.append(dummy2)
        dummy3 = animal("blank animal")
        self.animalList.append(dummy3)
        dummy4 = plant("blank plant")
        self.plantList.append(dummy4)
        dummy5 = otherLife("blank other")
        self.otherLifeList.append(dummy5)

    ###################################
    def addNew(self, theType, name):
        gc.debugBreakPoint("in init for myWorld.addNew ", "decisionProgram.py")
        if theType == "people":
            newPerson = person(name)
            self.peopleList.append(newPerson)

        elif theType == "object":
            newObject = anObject(name)
            self.objectList.append(newObject)

        elif theType == "animal":
            newAnimal = animal(name)
            self.animalList.append(newAnimal)

        elif theType == "plant":
            newPlant = plant(name)
            self.plantList.append(newPlant)

        elif theType == "otherlife":
            newOtherLife = otherLife(name)
            self.otherLifeList.append(newOtherLife)

        elif theType == "aplace":
            newPlace = aPlace(name)
            self.placeList.append(newPlace)

    ######################################
    def changeLocation(self,name):
        gc.debugBreakPoint("in init for myWorld.changeLocation ", "decisionProgram.py")
        self.currentLocation = name

    ######################################
    def loadWorld(self):
        gc.debugBreakPoint("in init for myWorld.loadWorld ", "decisionProgram.py")
        gc.debugBreakPoint("AI.myworld.loadWorld")
        os.chdir(gc.grendelWorldData)
        #global peopleList
        #global objectList
         #needs data structure for saved data, prossble folder w people and one with objects
         #read from json file
        with open("peopleIknow", "r") as content:
            self.peopleList = json.loads(content)
            #self.peopleList.append(datastuff)
        with open("objectsIknow", "r") as content:
            self.objectList = json.load(content)
            #self.objectList.append(datastuff)
        with open("animalsIknow", "r") as content:
            self.animalList = json.load(content)
            #self.animalList.append(datastuff)
        with open("plantsIknow", "r") as content:
            self.lantlist = json.load(content)
            #self.plantList.append(datastuff)
        with open("otherLifeIknow", "r") as content:
            self.otherLifeList = json.load(content)
            #self.otherLifeList.append(datastuff)

    #####################################
    def updateWorld():
        gc.debugBreakPoint("in init for myWorld.updateWorld", "decisionProgram.py")
        pass

    #####################################
    def saveWorld(self):
        gc.debugBreakPoint("in init for myWorld.saveWorld", "decisionProgram.py")
        os.chdir(gc.grendelWorldData)
        for each in self.peopleList:
            mydata = [each]
            jsonData = json.dumps(mydata, sort_keys = True,  indent = 4, separators = (",", ": "))
            with open("peopleIknow", 'w+') as f:
                 f.write(jsonData)

        for each in self.objectList:
            mydata = [each]
            jsonData = json.dumps(mydata, sort_keys = True,  indent = 4, separators = (",", ": "))
            with open("objectsIknow", 'w+') as f:
                 f.write(jsonData)

        for each in self.animalList:
            mydata = [each]
            jsonData = json.dumps(mydata, sort_keys = True,  indent = 4, separators = (",", ": "))
            with open("animalsIknow", 'w+') as f:
                 f.write(jsonData)

        for each in self.plantList:
            mydata = [each]
            jsonData = json.dumps(mydata, sort_keys = True,  indent = 4, separators = (",", ": "))
            with open("plantsIknow", 'w') as f:
                f.write(jsonData)

        for each in self.otherLifeList:
            mydata = [each]
            jsonData = json.dumps(mydata, sort_keys = True,  indent = 4, separators = (",", ": "))
            with open("otherlifeIknow", 'w') as f:
                f.write(jsonData)

    ########################################
    def getinfo(self,name):
        gc.debugBreakPoint("in init for getInfo", "decisionProgram.py")
        #ask humanabout a thing
        pass

#######################################
def analyseStatement():
    gc.debugBreakPoint("in init for analyseStatement", "decisionProgram.py")
    pass

#def makeMsg(title, text, primeRecipient, priority, otherRecievers, files):
#    mytime = time.time()
#    mymessage = gc.message()
#    mymessage.write(mytime, title, text, primeRecipient, priority, "AI", otherRecievers, files)

def makeAnswer():
    gc.debugBreakPoint("in init for amakeAnswer", "decisionProgram.py")
    pass

def processTask():
    gc.debugBreakPoint("in init for processTask", "decisionProgram.py")
    pass

def processToDo():
    gc.debugBreakPoint("in init for processToDo", "decisionProgram.py")
    pass

def makeDecisions():
    gc.debugBreakPoint("in init for makeDecisions", "decisionProgram.py")
    pass

def implementActions():
    gc.debugBreakPoint("in init for implementActions", "decisionProgram.py")
    pass

def shutdownGrendel():
    gc.debugBreakPoint("in init for shutdownGrendel", "decisionProgram.py")
    os.chdir(gc.grendelLogData)
    os.rename("masterlog.log", ("masterlog.log" + str(time.time())))
    #save world()
    sys.exit()
    pass

def startMycroft():
    gc.debugBreakPoint("in init for startMycroft", "decisionProgram.py")
    #simple start commmand , or link to what is happeing on the mycroft computer
    pass

def loadOtherData():
    gc.debugBreakPoint("in init for loadOtherDatat", "decisionProgram.py")
    pass


 ################################################################
 #initialze grendal world
 #need a function to create  basic json files on system first run -- birth point

#####################################################################
gc.debugBreakPoint("---------------entered startup routine-----------------------", "decisionProgram.py")
startMycroft()

grendelsworld = myWorld()
answer = input("you can reset grendel to his inital learning state here with yes. if you do old data files will be saved to filename.old. do you wish to start from no memory of the world?")
if answer == "yes":
    #move existing files to .old
    grendelsworld.firstInit
else: # do not reset, load  current data
    grendelsworld.loadWorld()
loadOtherData()
#startConversationWindow()
#startEye1()  ???
#startEye2()

###########################################################
firsttime =  True
run = True
while (run == True):

    gc.debugBreakPoint("in while loop main desionProgram ", "decisionProgram.py")
    # check for incoming inf
    if firsttime == True:
        os.chdir(gc.msgPathPY)
        gc.makeMsg("AI","AI startup","starting AI program","PY", "3" ,"NOONE", "NONE")
        firsttime = False
        gc.debugBreakPoint("AI1", "decisonProgram.py")
    newMsgs = os.listdir(gc.msgPathAI)
    print(newMsgs)
    for each in newMsgs:
        #getfirst message, need priority system
        damessage  = gc.message()
        damessage.read(each ,"AI")
        if  damessage.title == "sendVerbalAnswer":
            analyseStatement()
            makeAnswer()
        if  damessage.title == "needsProcessing":
            processTask()
        if  damessage.title ==  "needsUpdateWorld":
            myWorld.updateWorld()
        if  damessage.title == "shutdown":
            #myWorld.saveWorld()
            shutdownGrendel()
            break
        gc.makeMsg("AI","test","blahblahblah and blah","PY", "!" ,"NOONE", "NONE")
        gc.debugBreakPoint("leaving loop after updating messages processed", " decisionProgram.py" )
        #move message to processed folder

    #myWorld.updateWorld() #not sure about this call
    processToDo()
    makeDecisions()
    implementActions()
    #repeat