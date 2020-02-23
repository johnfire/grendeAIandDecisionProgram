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
    name = ""
    currentLocation = ""
    mass = ""
    living = ""
    intellegent = ""
    tangible = ""
    dims = []

#######################################
class person(thing):
    sex = ""
    job = ""
    trustRating = ""
    HomeLocation = ""
    WorkLocation = ""
    picture = ""
    height = ""
    weight = ""
    color = ""
    hairColor = ""
    eyeColor = ""
    relationship2Me = ""
    importantIdeas = []
    importantThoughts = []
    hobbies = []
    likes = []
    dislikes = []
    loves = []
    favoritePlaces = []
    history = []
    school = []
    degrees = []
    skills = []
    experience = []
    family = []
    friends = []
    conversatons = []
    commonExperiences = []

#####################################
class anObject(thing):
    function = ""
    color = ""
    size = ""
    dims = []
    dangers = []
    uses = []

######################################
class animal(thing):
    family = ""
    pass

######################################
class plant(thing):
    family = ""
    pass

######################################
class otherLife(thing):
    family = ""
    pass

######################################
class idea(thing):
    discription = ""

######################################
class myMorals(idea):
    listOfMorals = []
    pass

######################################
class myGoals(idea):
    listOfShortTermGoals = []
    listOfMedTermGoals = []
    listOfLongTermGoals = []
    pass

######################################
class aPlace(thing):
    #size, numpy array
    vectorFromHome = []
    otherVectorList = []

######################################

######################################
class myWorld (thing):
    currentModelTime =""
    peopleList = []
    objectList = []
    placeList = []
    animalList = []
    plantList = []
    otherLifeList = []
    currentPlace = "home"

    def addNew(theType, name):
        if theType == "people":
            newPerson = person(name)
            peopleList.append(newPerson)

        elif theType == "object":
            newObject = anObject(name)
            objectList.append(newObject)

        elif theType == "animal":
            newAnimal = animal(name)
            animalList.append(newAnimal)

        elif theType == "plant":
            newPlant = plant(name)
            plantList.append(newPlant)

        elif theType == "otherlife":
            newOtherLife = otherLife(name)
            otherLifeList.append(newOtherLife)

        elif theType == "aplace":
            newPlace = "name"
            placeList.append(newPlace)

    def changeLocation(self,name):
        self.currentLocation = name

    def loadWorld():
        global peopleList
        global objectList
         #needs data structure for saved data, prossble folder w people and one with objects
         #read from json file
        with open("peopleIknow", "r") as content:
            datastuff = json.load(content)
            peopleList.append(datastuff)
        with open("objectsIknow", "r") as content:
            datastuff = json.load(content)
            objectList.append(datastuff)
        with open("animalsIknow", "r") as content:
            datastuff = json.load(content)
            animalList.append(datastuff)
        with open("plantsIknow", "r") as content:
            datastuff = json.load(content)
            plantList.append(datastuff)
        with open("otherLifeIknow", "r") as content:
            datastuff = json.load(content)
            otherLifeList.append(datastuff)

    def updateWorld():
        pass

    def saveWorld():
        os.chdir(gc.grendelOtherData)
        for each in peopleList:
            with open("peopleIknow", 'w') as f:
                 f.write(each)

        for each in objectList:
            with open("objectsIknow", 'w') as f:
                 f.write(each)

        for each in animalList:
            with open("animalsIknow", 'w') as f:
                 f.write(each)

        for each in plantList:
            with open("plantsIknow", 'w') as f:
                f.write(each)

        for each in otherLifeList:
            with open("otherlifeIknow", 'w') as f:
             f.write(each)


    def getinfo(self,name):
        #ask humanabout a thing
        pass

#######################################
def analyseStatement():
    pass

def makeMsg(title, text, priority, reciever, otherRecievers, files):
    mytime = time.time()
    mymessage = gc.message
    mymessage.write(mytime, title, text, "AI", priority, reciever, otherRecievers, files)

def makeAnswer():
    pass

def processTask():
    pass

def processToDo():
    pass

def makeDecisions():
    pass

def implementActions():
    pass

def shutdownGrendel():
    #save world()
    sys.exit()
    pass

def startMycroft():
    #simple start commmand , or link to what is happeing on the mycroft computer
    pass

def loadOtherData():
    pass

startMycroft()
myWorld.loadWorld()
loadOtherData()
#startConversationWindow()
#startEye1()  ???
#startEye2()

###########################################################

while (1):
    print("in the loop")
    # check for incoming info
    newMsgs = os.listdir(gc.msgPathAI)
    for each in newMsgs:
        #getfirst message, need priority system
        answer  = gc.message.read(each,"AI") #should look at message and add to todo list
        if answer[1] == "sendVerbalAnswer":
            analyseStatement()
            makeAnswer()
        if  answer[1] == "needsProcessing":
            processTask()
        if  answer[1] ==  "needsUpdateWorld":
            myWorld.updateWorld()
        if  answer[1] == "needsShutdown":
            myWorld.saveWorld()
            shutdownGrendel()
            break
    myWorld.updateWorld() #not sure about this call
    processToDo()
    makeDecisions()
    implementActions()
    makeMsg("test","blahblahblah and blah", "!" , "PY","NOONE", "NONE")
    myanswer = input("any key to continue")
    #repeat
