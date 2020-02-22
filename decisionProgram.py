#!/usr/bin/python3
# main grendel one AI loop, drives all higher level thinking
# by Christopher Rehm christopherrehm@web.de
# released under the gnu public license number 3
# started 15 feb 2020

import os
import grendelconfig as gc

#######################################
#main decision program for grendel the robot
class thing():
    name = ""
    currentLocation = ""
    mass = ""
    dims = []
    living = ""
    intellegent = ""
    tangible = ""

#######################################
class person(thing):
    sex = ""
    job = ""
    hobbies = []
    HomeLocation = ""
    WorkLocation = ""
    importantIdeas = []
    importantThoughts = []
    trustRating = ""
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
    picture = ""
    height = ""
    weight = ""
    color = ""
    hairColor = ""
    eyeColor = ""
    conversatons = []
    commonExperiences = []

#####################################
class object(thing):
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
class message():
    text = ""
    sender = ""
    primeRecipient = ""
    otherRecipients = []
    piority = ""
    files = []

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
needsVerbalAnswer = False
needsProcessing = False
needsUpdateWorld = False
needsShutdown = False



def readAnswer():
    pass

def makeMsg():
    pass

def sendMsg():
    pass

def readMsg():
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
    #see loadWorld()
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
    if len(os.listdir(gc.msgPathAI) ) != 0:
        #getfirst message, need priority system
        readMsg() #should look at message and add to todo list
        if needsVerbalAnswer == 1:
            makeAnswer()
            sendAnswer()
        if needsProcessing == 1:
            processTask()
        if needsUpdateWorld == 1:
            myWorld.updateWorld()
        if needsShutdown == 1:
            shutdownGrendel()
            break
    myWorld.updateWorld() #not sure about this call
    processToDo()
    makeDecisions()
    implementActions()
    #repeat
