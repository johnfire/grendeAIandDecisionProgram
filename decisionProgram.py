#!/usr/bin/python3
"""Main grendel one AI loop, drives all higher level thinking.

by Christopher Rehm christopherrehm@web.de
released under the gnu public license number 3
started 15 feb 2020.
"""

import os
import sys
import time
import logging
# import json
import pickle
import grendelShares.grendelconfig as gc

DEBUG1 = True
DEBUG2 = True
DEBUG3 = True


#######################################
# main decision program for grendel the robot
class thing():
    """A thing in grendels world."""

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
    """Create a person object."""

    # pylint: disable=too-many-instance-attributes

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
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)

    def changeLocation(self):
        """Change persons location."""
        pass


#####################################
class anObject(thing):
    """Make an objext in grendels world."""

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
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class animal(thing):
    """Make an animal."""

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for animal ", "decisionProgram.py")
        self.family = ""
        self.color = ""

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class plant(thing):
    """Make a plant object."""

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for plant ", "decisionProgram.py")
        self.family = ""
        self.color = ""

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class otherLife(thing):
    """Make some other object."""

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for otherLife ", "decisionProgram.py")
        self.family = ""
        self.color = ""

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class idea(thing):
    """Make an idea object."""

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init for idea ", "decisionProgram.py")
        self.discription = ""

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class myMorals(idea):
    """Establish robot moral principals."""

    def __init__(self):
        super().__init__
        # self.name = name
        gc.debugBreakPoint("In init for myMorals ", "decisionProgram.py")
        self.listOfMorals = [







            ]

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class myGoals(idea):
    """Establish robot Goals."""

    def __init__(self):
        super().__init__
        # self.name = name
        gc.debugBreakPoint("In init for myGoals ", "decisionProgram.py")
        self.listOfShortTermGoals = []
        self.listOfMedTermGoals = []
        self.listOfLongTermGoals = []

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
class aPlace(thing):
    """Create a place object."""

    def __init__(self, name):
        super().__init__
        self.name = name
        gc.debugBreakPoint("In init aPlace ", "decisionProgram.py")
        # size, numpy array
        self.vectorFromHome = []
        self.otherVectorList = []

    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)


######################################
######################################
class myWorld(thing):
    """Create the general world object."""

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
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)

    ###################################
    def firstInit(self):
        """Init the program.

        Returns
        -------
        None.

        """
        print("Starting init")
        gc.debugBreakPoint("In init for first initialisation myWorld ",
                           "decisionProgram.py")
        dummy0 = person("empty person")
        gc.debugBreakPoint(2, dummy0, "First Init")
        self.peopleList.append(dummy0)
        gc.debugBreakPoint(2, self.peopleList[0], "First Init")
        gc.debugBreakPoint(2, "+++++++++++++++", "First Init")
        dummy1 = anObject("blank object")
        gc.debugBreakPoint(2, dummy1, "First Init")
        self.objectList.append(dummy1)
        gc.debugBreakPoint(3, self.objectList[0], "First Init")
        gc.debugBreakPoint(3, "end of object", "First Init")
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
        """Add something new to World Model.

        Parameters
        ----------
        theType : TYPE
            DESCRIPTION.
        name : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
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
        """Change grendels location in world model."""
        gc.debugBreakPoint(1, "In init for myWorld.changeLocation ",
                           "decisionProgram.py")
        self.currentLocation = name

    #####################################
    def updateWorld(self):
        """Update grendels model of the world."""
        gc.debugBreakPoint(1, "In init for myWorld.updateWorld",
                           "decisionProgram.py")

########################################
    def getinfo(self, name):
        """Ask questions to human.

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        gc.debugBreakPoint(1, "In init for getInfo", "decisionProgram.py")
        # ask humanabout a thing
        # should ask basic questions first then start filling in detals
        # based on current info
        # get name and what is it first then fill in other info as availaible

# =============================================================================
# ########################################
# def debugPoint(level, message2Print):
#     """Check debug statement."""
#     if DEBUG1 is True:
#         print(message2Print)
#     if DEBUG2 is True:
#         print(message2Print)
#     if DEBUG3 is True:
#         print(message2Print)
#
#
# #######################################
# =============================================================================


def analyseStatement():
    """Analyze a statement in English."""
    gc.debugBreakPoint(1, "In init for analyseStatement", "decisionProgram.py")
    # call NLP analyser


def makeAnswer():
    """Create Answer."""
    gc.debugBreakPoint(1, "In init for amakeAnswer", "decisionProgram.py")
    # check for easy standard replys while thinking:
    standardReplies = {
        # note this is a list of standard replys. its a dict of lists.
        # list format is replay, positive value, friend value,
        # unknown value, unfriend value
        # scale is on 0 to 9 for all values  9 is positive 0 is weak.
        "greeting": [["hello ,my name is grendel, nice to see you", 3, 1, 7, 0],
                     ["greetings human, how are you today?", 1, 2, 1, 5],
                     ["so hows it going today, i hope you are having a good one", 5, 7, 4, 1],
                     ["greets, whats up", 7, 9, 2, 0],
                     ["hi, I'm Grendel One, who are you", 4, 1, 9, 0],
                     ["dude whats happening", 5, 8, 4, 2]
                     ],

        "departure": [["thank you I have enjoyed this conversation", 5, 3, 7, 5],
                      ["later gator", 7, 9, 3, 5],
                      ["be seeing you!", 3, 4, 5, 7],
                      ["drugs are not the answer do something hip", 4, 1, 2, 7],
                      ["hasta la vista baby", 5, 5, 5, 7],
                      ["thank you that was an enjoyable conversaton", 7, 5, 5, 5],
                      ["ill be around round all around ", 7, 7, 4, 3],
                      ["it was a pleasure to meet you", 7, 1, 2, 2],
                      ],
        "unknownQuestion": ["I am sorry i do not know the answer to that,"
                            " I will attempt to do some research"
                            ],
        "knownQuestion": ["I think i may have an answer for that."
                          " here is the information"
                          ],
        "greetingAFriend": ["Hey mon its good to see you again, whats news?"
                            ],
        "helpQueston": ["can I help you with that some how"
                        ],
        "thankYou": ["thank you for that, it helps me understand"
                     " and deal with the world"
                     ]
        }

    # standardQuestions {
    #    }


def processTask():
    """Process a Task.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("In init for processTask", "decisionProgram.py")


def processToDo():
    """Do some Todo task.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("In init for processToDo", "decisionProgram.py")


def makeDecisions():
    """Make a Decision.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("In init for makeDecisions", "decisionProgram.py")
    # consider analzsed info evalute for goals
    # consider priciple evalute for morals
    # make decision


def implementActions():
    """Implement an action.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("In init for implementActions", "decisionProgram.py")


def shutdownMe():
    """Shutdown System.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("In init for shutdownGrendel", "decisionProgram.py")
    os.chdir(gc.grendelLogData)
    os.rename("masterlog.log", ("masterlog.log" + str(time.time())))
    sys.exit(0)


def startMycroft():
    """Start Mycroft software.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("In init for startMycroft", "decisionProgram.py")
    # simple start commmand, or link to what is happening on the mycroft comp


def loadOtherData():
    """Load some other data.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint(1, "In init for loadOtherDatat", "decisionProgram.py")

################################################################
# initialze grendel world

#####################################################################


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='grendel_logs_file',
                    filemode='a')
# Until here logs only to file: 'logs_file'

# define a new Handler to log to console as well
console = logging.StreamHandler()
# optional, set the logging level
console.setLevel(logging.INFO)
# set a format which is the same for console use
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to both ti file and console
logging.info('Jackdaws love my big sphinx of quartz.')
logging.info('Hello world')
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
    gc.debugBreakPoint(1, "Initialize world", "system start")
    grendelsWorld = myWorld()
    grendelsWorld.firstInit()
else:  # do not reset, load  current data
    gc.debugBreakPoint(1, "Loading saved world now", "system Start")
    os.chdir(gc.grendelWorldData)
    with open('world_data.pkl', 'rb') as input:
        grendelsWorld = pickle.load(input)
# loadOtherData()
# startConversationWindow()
# startEye1()
# startEye2()

###########################################################
FIRSTTIME = True
RUN = True
while(RUN is True):
    msgLocation = "Main decision loop"
    gc.debugBreakPoint("In while loop main dec program ", msgLocation)
    # check for incoming inf
    if FIRSTTIME is True:
        os.chdir(gc.msgPathPY)
        gc.makeMsg("AI", "AI startup", "starting AI program", "3",
                   "PY", "NOONE", "NONE")
        FIRSTTIME = False
        gc.debugBreakPoint(1, "AI1", msgLocation)
    newMsgs = os.listdir(gc.msgPathAI)
    gc.debugBreakPoint(1, "Adding the messages to list", msgLocation)
    gc.debugBreakPoint(1, newMsgs, msgLocation)
    for each in newMsgs:
        # getfirst message, need priority system
        damessage = gc.message()
        damessage.read(each, "AI")
        gc.debugBreakPoint(1, "1111111111111111111", msgLocation)
        gc.debugBreakPoint(1, damessage.sender, msgLocation)
        if damessage.title == "sendVerbalAnswer":
            analyseStatement()
            makeAnswer()
        if damessage.title == "needsProcessing":
            processTask()
        if damessage.title == "needsUpdateWorld":
            myWorld.updateWorld()
        if damessage.title == "shutdown":
            gc.debugBreakPoint(1, "Recieved shutdown message", msgLocation)
            gc.debugBreakPoint(1, "SHUTTDOWN", msgLocation)
            os.chdir(gc.grendelWorldData)
            with open('world_data.pkl', 'wb') as output:
                pickle.dump(grendelsWorld, output, pickle.HIGHEST_PROTOCOL)
            shutdownMe()
        gc.makeMsg("AI", "test", "blahblahblah and blah", "7",
                   "PY", "NOONE", "NONE")
        gc.debugBreakPoint(2, "Leaving loop after updating messages processed",
                           msgLocation)
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
