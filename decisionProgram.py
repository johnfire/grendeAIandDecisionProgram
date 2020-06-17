#!/usr/bin/python3
"""Main grendel one AI loop, drives all higher level thinking.

by Christopher Rehm christopherrehm@web.de
released under the gnu public license number 3
started 15 feb 2020.
"""

import os
import sys
# import time
import logging
# import json
import pickle
import grendelShares.grendelconfig as gc

LOGLEVEL = "logging.DEBUG"


#######################################
# main decision program for grendel the robot
class thing():
    """A thing in grendels world."""

    def __init__(self, name):
        logging.debug('in init for thing')
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
        logging.debug('In init for person')
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

###################################################
    def __str__(self):
        """Make a string from object, for printing.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return str(self.__class__) + ": " + str(self.__dict__)

###################################################
    def changeLocation(self):
        """Change persons location."""
        pass


#####################################
class anObject(thing):
    """Make an objext in grendels world."""

    def __init__(self, name):
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
class myWorld(thing):
    """Create the general world object."""

    ###################################

    def __init__(self):
        super().__init__
        logging.debug('In init for myWorld')
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
        logging.debug('Starting init')
        dummy0 = person("empty person")
        self.peopleList.append(dummy0)
        dummy1 = anObject("blank object")
        self.objectList.append(dummy1)
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
        self.currentLocation = name

    #####################################
    def updateWorld(self):
        """Update grendels model of the world."""

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
        # ask humanabout a thing
        # should ask basic questions first then start filling in detals
        # based on current info
        # get name and what is it first then fill in other info as availaible


###################################################
def analyseStatement():
    """Analyze a statement in English."""
    # call NLP analyser


###################################################
def makeAnswer():
    """Create Answer."""
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


###################################################
def processTask():
    """Process a Task.

    Returns
    -------
    None.

    """


###################################################
def processToDo():
    """Do some Todo task.

    Returns
    -------
    None.

    """


###################################################
def makeDecisions():
    """Make a Decision.

    Returns
    -------
    None.

    """
    # consider analzsed info evalute for goals
    # consider priciple evalute for morals
    # make decision


###################################################
def implementActions():
    """Implement an action.

    Returns
    -------
    None.

    """


###################################################
def shutdownMe():
    """Shutdown System.

    Returns
    -------
    None.

    """
    logging.info('Recieved shutdown message')
    os.chdir(gc.grendelWorldData)
    with open('world_data.pkl', 'wb') as output:
        pickle.dump(grendelsWorld, output, pickle.HIGHEST_PROTOCOL)
    sys.exit(0)


###################################################
def startMycroft():
    """Start Mycroft software.

    Returns
    -------
    None.

    """
    # simple start commmand, or link to what is happening on the mycroft comp


###################################################
def loadOtherData():
    """Load some other data.

    Returns
    -------
    None.

    """


###################################################
def worldUpdate():
    """Call function to update world.

    Returns
    -------
    None.

    """
    myWorld.updateworld()


###################################################
def f_default(*args, **kwargs):
    """Execute default message when switch does not work."""
    print("Received a message I have no idea what to do with.")


###################################################
def dpSwitcher(case):
    """Switching function for decision program.

    Returns
    -------
    None.

    """
    return {
        "sendverbalAnswer": makeAnswer,
        "needsProcessing": processTask,
        "needsUpdateWorld": worldUpdate,
        "shutdown": shutdownMe
        }.get(case, f_default)

################################################################
# initialze grendel world

#####################################################################


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - AIprogram - %(process)d - %(levelname)s - %(message)s',
                    filename='grendel_logs_file',
                    filemode='a')
# Until here logs only to file: 'logs_file'

# define a new Handler to log to console as well
console = logging.StreamHandler()
# optional, set the logging level
console.setLevel(logging.INFO)
# set a format which is the same for console use
formatter = logging.Formatter('%(asctime)s - AIprogram - %(process)d - %(levelname)s - %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to both ti file and console
logging.info('grendel system startup')
logging.info('Hello world')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

startMycroft()
# answer = "NO"
answer = input("You can reset Grendel One to his inital learning state \
                here with yes.\n If you do old data files will be saved \
                to filename.old.\n Do you wish to start from no memory  \
                of the world?")
if answer == "yes":
    os.chdir(gc.grendelWorldData)
    if os.path.exists('./world_data.pkl') is True:
        os.rename('world_data.pkl', 'world_data.pkl.old')
    logging.debug('Initializing Grendel world')
    grendelsWorld = myWorld()
    grendelsWorld.firstInit()
else:  # do not reset, load  current data
    logging.debug('loading previous world now')
    os.chdir(gc.grendelWorldData)
    with open('world_data.pkl', 'rb') as input:
        grendelsWorld = pickle.load(input)
# loadOtherData()
# startConversationWindow()
# startEye1()
# startEye2()

###########################################################
counter = 0
FIRSTTIME = True
RUN = True
logging.debug('entering while loop main decision program ')
while(RUN is True):
    # check for incoming inf
    logging.debug('starting main while loop')
    if FIRSTTIME is True:
        os.chdir(gc.msgPathPY)
        gc.makeMsg("AI", "AI startup", "starting AI program", "3",
                   "PY", "NOONE", "NONE")
        FIRSTTIME = False
    newMsgs = os.listdir(gc.msgPathAI)
    logging.debug("Adding the messages to list")
    for each in newMsgs:
        logging.debug("message name is:")
        logging.debug(each)
        # getfirst message, need priority system
        damessage = gc.message()
        damessage.read(each, "AI")
        dpSwitcher(damessage.title)(gc.message)

        if counter % 100000 == 0:
            gc.makeMsg("AI", "test", "blahblahblah and blah", "7",
                       "PY", "NOONE", "NONE")
        # move message to processed folder
        os.system('mv '
                  + gc.msgPathAI
                  + "/"
                  + each
                  + ' '
                  + gc.msgPath
                  + '/processedMsgs/'
                  )
        logging.info('Leaving loop after updating messages processed')
    processToDo()
    makeDecisions()
    implementActions()
