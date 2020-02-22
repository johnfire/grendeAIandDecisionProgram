#!/usr/bin/python3
# main grendel one AI loop, drives all higher level thinking
# by Christopher Rehm christopherrehm@web.de
# released under the gnu public license number 3
# started 15 feb 2020

import os
import sys
import time
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
    peopleList = []
    objectList = []
    placeList = []

    def addNew(list, name):
        pass

    def changeLocation():
        pass

    def loadWorld():
        global peopleList
        global objectList
         #needs data structure for saved data, prossble folder w people and one with objects
        for each in peopleList:
            #read from json file
            pass
        for each in objectList:
            #read from json file
            pass

    def updateWorld():
        pass

    def saveWorld():
        for each in peopleList:
            #write to json file
            pass
        for each in objectList:
            #write to json file
            pass

#######################################

def readAnswer():
    pass

def makeMsg():
    pass

def sendMsg():
    pass

def readMsg():
    x =7
    #look at message header return code from header to do next task.

    return x
    pass

def makeAnswer():
    pass

def sendAnswer():
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
#loadWorld()
loadOtherData()
#startConversationWindow()
#startEye1()  #???
#startEye2()

while (1):
    print("in the loop")
    # check for incoming info
    newMsgs = os.listdir(gc.msgPathAI)
    for each in newMsgs:
        #getfirst message, need priority system
        answer  = gc.message.read(each,"AI") #should look at message and add to todo list
        if answer[1] == "sendVerbalAnswer":
            makeAnswer()
            sendAnswer()
        if  answer[1] == "needsProcessing":
            processTask()
        if  answer[1] ==  "needsUpdateWorld":
            myWorld.updateWorld()
        if  answer[1] == "needsShutdown":
            shutdownGrendel()
            break
    myWorld.updateWorld() #not sure about this call
    processToDo()
    makeDecisions()
    implementActions()
    mytime = time.time()
    print(mytime)
    mymessage = gc.message
    mymessage.write(mytime,"test","blahblahblah and blah", "PY", "!" , "AI","NOONE", "NONE")
    myanswer = input("any key to continue")
    #repeat
