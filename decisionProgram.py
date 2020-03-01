#!/usr/bin/python3
# main grendel one AI loop, drives all higher level thinking
# by Christopher Rehm christopherrehm@web.de
# released under the gnu public license number 3
# started 15 feb 2020

import os
import sys
import time
# import json
import pickle
import grendelconfig as gc

DEBUG = True


#######################################
# main decision program for grendel the robot
class thing():

    def __init__(self, name):
        gc.debugBreakPoint("in init for thing ", "decisionProgram.py")
        self.name = name
        self.currentLocation = ""
        self.mass = ""
        self.living = ""
        self.intellegent = ""
        self.tangible = ""
        self.dims = []


#######################################
class person(thing):

    def __init__(self, name):
        super().__init__
        gc.debugBreakPoint("In init for person ", "decisionProgram.py")
        self.name = name
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

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


#####################################
class anObject(thing):

    def __init__(self, name):
        gc.debugBreakPoint("In init for anObject ", "decisionProgram.py")
        super().__init__
        self.name = name
        self.function = ""
        self.color = ""
        self.size = ""
        self.dims = []
        self.dangers = []
        self.uses = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class animal(thing):

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for animal ", "decisionProgram.py")
        self.family = ""
        self.color = ""

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class plant(thing):

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for plant ", "decisionProgram.py")
        self.family = ""
        self.color = ""

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class otherLife(thing):

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for otherLife ", "decisionProgram.py")
        self.family = ""
        self.color = ""

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class idea(thing):

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for idea ", "decisionProgram.py")
        self.discription = ""

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class myMorals(idea):

    def __init__(self):
        super().__init__
        # self.name = name
        gc.debugBreakPoint("In init for myMorals ", "decisionProgram.py")
        self.listOfMorals = [







            ]

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class myGoals(idea):

    def __init__(self):
        super().__init__
        # self.name = name
        gc.debugBreakPoint("In init for myGoals ", "decisionProgram.py")
        self.listOfShortTermGoals = []
        self.listOfMedTermGoals = []
        self.listOfLongTermGoals = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class aPlace(thing):

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init aPlace ", "decisionProgram.py")
        # size, numpy array
        self.vectorFromHome = []
        self.otherVectorList = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
######################################
class myWorld(thing):

    ###################################

    def __init__(self):
        super().__init__
        gc.debugBreakPoint("In init for myWorld ", "decisionProgram.py")
        self.currentModelTime = ""
        self.peopleList = []
        self.objectList = []
        self.placeList = []
        self.animalList = []
        self.plantList = []
        self.otherLifeList = []
        self.currentPlace = "home"

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    ###################################
    def firstInit(self):
        print("Starting init")
        gc.debugBreakPoint("In init for first initialisation myWorld ",
                           "decisionProgram.py")
        dummy0 = person("empty person")
        if DEBUG is True: print(dummy0)
        self.peopleList.append(dummy0)
        if DEBUG is True: print(self.peopleList[0])
        if DEBUG is True: print("+++++++++++++++++")
        dummy1 = anObject("blank object")
        if DEBUG is True: print(dummy1)
        self.objectList.append(dummy1)
        if DEBUG is True: print(self.objectList[0])
        if DEBUG is True: print("end of object")
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
        gc.debugBreakPoint("In init for myWorld.addNew ", "decisionProgram.py")
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
    def changeLocation(self, name):
        gc.debugBreakPoint("In init for myWorld.changeLocation ",
                           "decisionProgram.py")
        self.currentLocation = name

    #####################################
    def updateWorld():
        gc.debugBreakPoint("In init for myWorld.updateWorld",
                           "decisionProgram.py")
        pass

########################################
    def getinfo(self, name):

        gc.debugBreakPoint("In init for getInfo", "decisionProgram.py")
        # ask humanabout a thing
        # should ask basic questions first then start filling in detals
        # based on current info
        # get name and what is it first then fill in other info as availaible
        pass


#######################################
def analyseStatement():
    gc.debugBreakPoint("In init for analyseStatement", "decisionProgram.py")
    # call NLP analyser
    pass


def makeAnswer():
    gc.debugBreakPoint("In init for amakeAnswer", "decisionProgram.py")
    # check for easy standard replys while thinking:
    standardReplies = {
        # note this is a list of standard replys. its a dict of lists.
        # list format is replay, positive value, friend value,
        # unknown value, unfriend value
        # scale is on 0 to 9 for all values  9 is positive 0 is weak.
        greeting: [["hello ,my name is grendel, nice to see you",
                    3, 1, 7, 0],
                   ["greetings human, how are you today?", 1, 2, 1, 5],
                   ["so hows it going today, i hope you are having a good one",
                    5, 7, 4, 1],
                   ["greets, whats up", 7, 9, 2, 0],
                   ["hi, I'm Grendel One, who are you", 4, 1, 9, 0],
                   ["dude whats happening", 5, 8, 4, 2]
                   ],

        departure: [["thank you I have enjoyed this conversation", 5, 3, 7, 5],
                    ["later gator", 7, 9, 3, 5],
                    ["be seeing you!", 3, 4, 5, 7],
                    ["drugs are not the answer do something hip", 4, 1, 2, 7],
                    ["hasta la vista baby", 5, 5, 5, 7],
                    ["thank you that was an enjoyable conversaton",
                     7, 5, 5, 5],
                    ["ill be around round all around ", 7, 7, 4, 3],
                    ["it was a pleasure to meet you", 7, 1, 2, 2],
                    ],
        unknownQuestion: ["I am sorry i do not know the answer to that,"
                          " I will attempt to do some research"
                          ],
        knownQuestion: ["I think i may have an answer for that."
                        " here is the information"
                        ],
        greetingAFriend: ["Hey mon its good to see you again, whats news?"
                          ],
        helpQueston: ["can I help you with that some how"
                      ],
        thankYou: ["thank you for that, it helps me understand"
                   " and deal with the world"
                   ]
        }

    # standardQuestions {
    #    }


def processTask():
    gc.debugBreakPoint("In init for processTask", "decisionProgram.py")


def processToDo():
    gc.debugBreakPoint("In init for processToDo", "decisionProgram.py")


def makeDecisions():
    gc.debugBreakPoint("In init for makeDecisions", "decisionProgram.py")
    # consider analzsed info evalute for goals
    # consider priciple evalute for morals
    # make decision


def implementActions():
    gc.debugBreakPoint("In init for implementActions", "decisionProgram.py")


def shutdownMe():
    gc.debugBreakPoint("In init for shutdownGrendel", "decisionProgram.py")
    os.chdir(gc.grendelLogData)
    os.rename("masterlog.log", ("masterlog.log" + str(time.time())))
    sys.exit(0)


def startMycroft():
    gc.debugBreakPoint("In init for startMycroft", "decisionProgram.py")
    # simple start commmand, or link to what is happening on the mycroft comp


def loadOtherData():
    gc.debugBreakPoint("In init for loadOtherDatat", "decisionProgram.py")
    pass

################################################################
# initialze grendel world

#####################################################################


gc.debugBreakPoint("---------------entered startup routine-----------------",
                   "decisionProgram.py")
startMycroft()
# answer = "NO"
answer = input("You can reset Grendel One to his inital learning state \
                here with yes.\n If you do old data files will be saved \
                to filename.old.\n Do you wish to start from no memory  \
                of the world?")
if answer == "yes":
    os.chdir(gc.grendelWorldData)
    os.rename('world_data.pkl', 'world_data.pkl.old')
    if DEBUG is True: print("Init world")
    grendelsworld = myWorld()
    grendelsworld.firstInit()
else:  # do not reset, load  current data
    if DEBUG is True: print("Loading saved world now")
    os.chdir(gc.grendelWorldData)
    with open('world_data.pkl', 'rb') as input:
        grendelsworld = pickle.load(input)
# loadOtherData()
# startConversationWindow()
# startEye1()
# startEye2()

###########################################################
firsttime = True
run = True
while(run is True):

    gc.debugBreakPoint("In while loop main dec program ", "decisionProgram.py")
    # check for incoming inf
    if firsttime is True:
        os.chdir(gc.msgPathPY)
        gc.makeMsg("AI", "AI startup", "starting AI program", "3",
                   "PY", "NOONE", "NONE")
        firsttime = False
        gc.debugBreakPoint("AI1", "decisonProgram.py")
    newMsgs = os.listdir(gc.msgPathAI)
    if DEBUG is True: print("Adding the messages to list")
    if DEBUG is True: print(newMsgs)
    for each in newMsgs:
        # getfirst message, need priority system
        damessage = gc.message()
        damessage.read(each, "AI")
        if DEBUG is True: print("1111111111111111111")
        if DEBUG is True: print(damessage.sender)
        if damessage.title == "sendVerbalAnswer":
            analyseStatement()
            makeAnswer()
        if damessage.title == "needsProcessing":
            processTask()
        if damessage.title == "needsUpdateWorld":
            myWorld.updateWorld()
        if damessage.title == "shutdown":
            if DEBUG is True: print("Recieved shutdown message")
            gc.debugBreakPoint("SHUTTDOWN", "AI")
            os.chdir(gc.grendelWorldData)
            with open('world_data.pkl', 'wb') as output:
                pickle.dump(grendelsworld, output, pickle.HIGHEST_PROTOCOL)
            shutdownMe()
        gc.makeMsg("AI", "test", "blahblahblah and blah", "7",
                   "PY", "NOONE", "NONE")
        gc.debugBreakPoint("Leaving loop after updating messages processed",
                           " decisionProgram.py", True)
        # move message to processed folder
        os.system('mv '
                  + gc.msgPathPY
                  + "/"
                  + each
                  + ' '
                  + gc.msgPath
                  + '/processedMsgs/'
                  )
    processToDo()
    makeDecisions()
    implementActions()
    # repeat
