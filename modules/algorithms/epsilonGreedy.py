################################################################################
# Module      : epsilonGreedy
# Description : epsilon-Greedy algorithm
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

import random

MODULE_NAME = "epsilonGreedy"

class epsilonGreedy:

    """----------------------------------------------------------------------"""
    """ Initialization : set the parameters for algorithm
            epsilon     - epsilon value for algorithm
            noOfArms    - Number of arms of the bandit
    """
    def __init__( self, epsilon, noOfArms ):
        self.epsilon    = epsilon
        self.noOfArms   = noOfArms

        # init the internal values
        self.reset()
    """----------------------------------------------------------------------"""
    """ reset() : function to reset the internal values of algorithm
    """
    def reset( self ):
        # Reset internal values to default
        self.pullCount  = [ 0 for i in range(self.noOfArms) ]
        self.armValue   = [ 0.00 for i in range(self.noOfArms) ]
    """----------------------------------------------------------------------"""
    """ getArmsToPull() : returns indices of best armsToPull
            noOfArms    - (optional) number of arms required
    """
    def getArmsToPull( self, noOfArms = 1 ):
        sortedIndices = sorted( range(len(self.armValue)), key=lambda i:self.armValue[i] )[::-1]
        if( noOfArms == 1 ):
            # Usual \epsilon-Greedy algorithm
            if( random.random() > self.epsilon ):
                return sortedIndices[0]
            else:
                return random.randrange( self.noOfArms )
        else:
            # for selecting more than one arm,
            # with 1-\epsilon probability, choose the next best arm
            nextBestArm = 0
            armsToPull = [ ]
            for i in range( noOfArms ):
                if( random.random() > self.epsilon ):
                    while( sortedIndices[nextBestArm] in armsToPull ):
                        nextBestArm += 1
                    armsToPull += [ sortedIndices[nextBestArm] ]
                else:
                    selectedArm = random.randrange( self.noOfArms )
                    while( selectedArm in armsToPull ):
                        selectedArm = random.randrange( self.noOfArms )
                    armsToPull += [ selectedArm ]
            return armsToPull
    """----------------------------------------------------------------------"""
    """ updateRewards() : updates the observed rewards to algorithm
            armIndices  - indices of the arms to update
            rewards     - rewards of corresponding arms
    """
    def updateRewards( self, armIndices, rewards ):
        # Check whether we have right type for armIndices
        if( type(armIndices) == int ):
            armIndices  = [ armIndices ]
        if( ~isinstance(rewards,list) ):
            rewards     = [ rewards ]
        elif( type(armIndices) == list ):
            # Check whether rewards is also list of same length
            if( type(rewards) == list):
                # Check whether lengths match
                if( len(armIndices) != len(rewards) ):
                    print MODULE_NAME, " ERROR : ", "'armIndices' and 'rewards' must be of same length"
                    return None
            else:
                print MODULE_NAME, "ERROR : ", "'rewards' also must a list"
        else:
            print MODULE_NAME, " ERROR : ", "'armIndices' should be of type 'int' or 'list'"
            return None

        # incremental update
        i = 0
        for arm in armIndices:
            self.pullCount[arm]  += 1
            self.armValue[arm]   = self.armValue[arm] \
                                    + 1.00/self.pullCount[arm] \
                                        * (rewards[armIndices.index(arm)]-self.armValue[arm])
            i += 1
    """----------------------------------------------------------------------"""
    """ getStats() : get inner statistics of algorithm
            Return : depends on algorithm,
                     armPullCount, armIndices
    """
    def getStats( self ):
        return self.pullCount, self.armValue
    """----------------------------------------------------------------------"""


# tetst code
if __name__ == '__main__':
    algo_epsG = epsilonGreedy( 0.10, 5 )

    rewards = [ 4.3, 6.7, 3.5, 0.3, 1.7 ]

    for i in range( 500 ):
        armIndices = algo_epsG.getArmsToPull()
        # print "Arms to Pull : ", armIndices, "    reward = ", rewards[armIndices]
        algo_epsG.updateRewards( armIndices, rewards[armIndices] )

    algo_epsG.reset()

    for i in range(500):
        armIndices = algo_epsG.getArmsToPull( 3 )
        # print "armsIndices : ", armIndices
        algo_epsG.updateRewards( armIndices, [ rewards[i] for i in armIndices ] )

    algo_epsG.reset()
