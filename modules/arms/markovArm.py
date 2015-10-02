################################################################################
# Module      : markovArm
# Description : Implements a markov arm - both rested and restless case
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

import random

""" Constants """
ARMTYPE_RESTED   = 0
ARMTYPE_RESTLESS = 1


class markovArm:
    """----------------------------------------------------------------------"""
    """ Arm Initializer """
    def __init__( self, armModel, armType = ARMTYPE_RESTED, startState = "s0" ):
        self.armType    = armType
        self.armModel   = armModel
        self.startState = startState
        self.currState  = startState
        self.states     = list( armModel.keys() )
        self.states.sort()
    """----------------------------------------------------------------------"""
    """ Reset arm to start state """
    def reset( self ):
        self.currState  = self.startState
    """----------------------------------------------------------------------"""
    """ A clock tick for restless arm
        return reward if restless arm, None otherwise
    """
    def tick( self ):
        reward = None

        # If restless arm, then do state transition and extract reward
        if( self.armType == ARMTYPE_RESTLESS ):
            reward = self.pull()

        return reward

    """----------------------------------------------------------------------"""
    """ Pull a rested arm, returns reward """
    def pull( self ):
        # 1. Get current state
        # 2. Look up in the model for transition probabilities from this state
        # 3. Create the cumulative distribution
        # 4. Generate a U(0,1) random number and do the next state selection
        # 5. Do the transition and return the reward.

        reward = None

        # 3.
        cummProb = [ 0 ]        # to hold cummulative probabilities, dummy 0 will be removed later
        for nxtState in self.armModel[self.currState]["p"]:
            cummProb = cummProb + [ cummProb[-1]+self.armModel[self.currState]["p"][nxtState] ]
        cummProb.pop(0)         # remove dummy 0

        # 4. Generate random number U(0,1]
        x = random.random()
        # 4. Select next state based on 'x'
        pos = 0
        while( x > cummProb[pos] ):
            pos = pos + 1

        # 5. Do transition to next state
        self.currState = self.armModel[self.currState]["p"].keys()[pos]
        # 5. Extract reward
        reward = self.armModel[self.currState]["r"]

        return reward

    """----------------------------------------------------------------------"""

# self test code
if __name__ == '__main__':
    testModel = {
                    "s0" : {
                        "r" : 1.0,
                        "p" : {
                            "s0" : 0.3,
                            "s1" : 0.7
                        }
                    },
                    "s1" : {
                        "r" : 2.0,
                        "p" : {
                            "s0" : 0.6,
                            "s1" : 0.4
                        }
                    }
                }

    testArm_restless = markovArm( armModel = testModel, startState = "s0", armType = ARMTYPE_RESTLESS )
    testArm_rested   = markovArm( armModel = testModel, startState = "s0" )

    # test for restless arm
    lastState = testModel["s0"]["r"]
    currState = 0.00
    rewardTable = {}
    for state in testModel.keys():
        rewardTable[testModel[state]["r"]] = {}

    for i in range(1000):
        currState = testArm_restless.tick();
        if( currState in rewardTable[lastState] ):
            rewardTable[lastState][currState] += 1
        else:
            rewardTable[lastState][currState] = 1
        lastState = currState

    # display results
    states = rewardTable.keys()
    states.sort()

    print "Restless Arm"
    print "    ",
    for prevState in states:
        print prevState, "    ",
    print ""
    for prevState in states:
        print prevState, " ",
        for currState in states:
            print rewardTable[prevState].get( currState, 0 ), "     ",
        print ""


    print "Rested Arm"
    print testArm_rested.pull()
    print testArm_rested.pull()
    print testArm_rested.pull()
    print testArm_rested.tick()
    print testArm_rested.tick()
