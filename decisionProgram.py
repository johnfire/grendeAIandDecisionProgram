#!/usr/bin/python3

import grendel.config as gc

#main decision program for grendel the robot
class person():
    name = ""
    sex = ""
    job = ""
    hobbies = ()
    currentLocation = ""
    HomeLocation = ""
    WorkLocation = ""
    importantIdeas = ()
    importantThoughts = ()
    trustRating = ""
    likes = ()
    dislikes = ()
    loves = ()
    favoritePlaces = ()
    history = ()
    school = ()
    degrees = ()
    skills = ()
    experience = ()
    family = ()
    friends = ()
    picture = ""
    height = ""
    weight = ""
    color = ""
    hairColor = ""
    eyeColor = ""
    conversatons = ()
    commonExperiences = ()


#####################################
class object():
    name = ""
    location = ""
    function = ""
    color = ""
    size = ""
    dims = ()
    dangers = ()
    uses = ()

######################################
class myWorld ():
     
    def addNew():
        pass

    def changeLocation():
        pass

#######################################
def readAnswer():
    pass

def makeMsg():
    pass

def sendMsg():
    pass

def processTask():
    pass

def updateWorld():
    pass

def processToDo():
    pass

def makeDecisions():
    pass

def implementActions():
    pass

def shutdownGrendel():
    pass

def startMycroft():
    pass

def loadWorld():
    pass

def loadOtherData():
    pass


startMycroft()
loadWorld()
loadOtherData()
#startConversationWindow()
#startEye1()  #???
#startEye2()

while (1):
    print("in the loop")
    # check for incoming info
    if len(os.listdir(gc.msgPathAI) ) != 0
        #getfirst message, need priority system
        readMsg() #should look at message and add to todo list
        if needsVerbalAnswer == 1
            makeAnswer()
            sendAnswer()
        if needsProcessing == 1
            processTask()
        if needsUpdateWorld == 1
            updateWorld()
        if needsShutdown == 1
            shutdownGrendel()
    updateWorld() #not sure about this call
    processToDo()
    makeDecisions()
    implementActions()
    #repeat
