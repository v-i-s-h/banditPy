################################################################################
# Module      : UCB
# Description : Upper Confidence Bound algorithm
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

import math

MODULE_NAME = "UCB"

################################################################################
# Description : Implementation of UCB1 based on Fig.1 from
#                   Auer, P., Cesa-bianchi, N., & Fischer, P. (2002).
#                   Finite time analysis of the multiarmed bandit problem.
#                   Machine Learning, 47, 235-256.
################################################################################
class UCB1( object ):
        """----------------------------------------------------------------------"""
        """ Initialization : set the parameters for algorithm
                noOfArms    - Number of arms of the bandit
        """
        def __init__( self, noOfArms ):
            self.noOfArms   = noOfArms

            # init the internal values
            self.reset()
        """----------------------------------------------------------------------"""
        """ reset() : function to reset the internal values of algorithm
        """
        def reset( self ):
            # Reset internal values to default
            self.pullCount    = [ 0 for i in range(self.noOfArms) ]
            self.armAvgReward = [ 0.00 for i in range(self.noOfArms) ]
            self.armValue     = [ float('Inf') for i in range(self.noOfArms) ]
        """----------------------------------------------------------------------"""
        """ getArmsToPull() : returns indices of best armsToPull
                noOfArms    - (optional) number of arms required
        """
        def getArmsToPull( self, noOfArms = 1 ):
            sortedIndices = sorted( range(len(self.armValue)), key=lambda i:self.armValue[i] )[::-1]
            if noOfArms == 1:
                return sortedIndices[0]
            else:
                return sortedIndices[0:noOfArms-1]
        """----------------------------------------------------------------------"""
        """ updateRewards() : updates the observed rewards to algorithm, calculates
                              new value for each arm
                armIndices  - indices of the arms to update
                rewards     - rewards of corresponding arms
        """
        def updateRewards( self, armIndices, rewards ):
            # Check whether we have right type for armIndices
            if( not isinstance(armIndices,list) ):
                armIndices  = [ armIndices ]
            if( not isinstance(rewards,list) ):
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
            for arm in armIndices:
                self.pullCount[arm]     += 1
                self.armAvgReward[arm]   = self.armAvgReward[arm] \
                                            + 1.00/self.pullCount[arm] \
                                                * (rewards[armIndices.index(arm)]-self.armAvgReward[arm])

            # calculate value for each arm
            n = sum( self.pullCount )
            for arm in armIndices:
                try:
                    self.armValue[arm] = self.armAvgReward[arm] + math.sqrt( 2*math.log(n)/self.pullCount[arm] )
                except ZeroDivisionError:
                    self.armValue[arm] = float( 'Inf' )
        """----------------------------------------------------------------------"""
        """ getStats() : get inner statistics of algorithm
                Return : depends on algorithm,
                         armPullCount, armIndices
        """
        def getStats( self ):
            return { 'pullCount' : self.pullCount,
                     'armValue'  : self.armValue,
                     'AvgReward' : self.armAvgReward }
        """----------------------------------------------------------------------"""


################################################################################
# Description : Implementation of UCB2 based on Fig.2 from
#                   Auer, P., Cesa-bianchi, N., & Fischer, P. (2002).
#                   Finite time analysis of the multiarmed bandit problem.
#                   Machine Learning, 47, 235-256.
################################################################################
class UCB2( object ):
        """----------------------------------------------------------------------"""
        # Mandatory Functions
        """----------------------------------------------------------------------"""
        """ Initialization : set the parameters for algorithm
                <param : description>
        """
        def __init__( self, noOfArms, alpha ):
            self.noOfArms   = noOfArms
            self.alpha      = alpha

            # Optional Reset init the internal values
            self.reset()
        """----------------------------------------------------------------------"""
        """ reset() : function to reset the internal values of algorithm
        """
        def reset( self ):
            # Reset internal values to default
            self.pullCount    = [ 0 for i in range(self.noOfArms) ]
            self.armAvgReward = [ 0.00 for i in range(self.noOfArms) ]
            self.armValue     = [ float('Inf') for i in range(self.noOfArms) ]
            self.rIndex       = [ 0 for i in range(self.noOfArms) ]
            self.stepsToCompleteThisEpoch   = 0
            self.thisEpochArmIndex          = 0
        """----------------------------------------------------------------------"""
        """ getArmsToPull() : returns indices of best armsToPull
                noOfArms    - (optional) number of arms required
        """
        def getArmsToPull( self ):
            # First, play all arms atleast once
            if 0 in self.pullCount:
                self.thisEpochArmIndex = self.pullCount.index( 0 )
                self.stepsToCompleteThisEpoch   = 0
                return self.thisEpochArmIndex   # Return the arm which is not played

            # All arms are played atleast once
            # If we are in a play epoch, play that last arm again
            if self.stepsToCompleteThisEpoch > 0:
                self.stepsToCompleteThisEpoch -= 1
                return self.thisEpochArmIndex

            # NEW EPOCH,
            # update last epoch arm index
            self.rIndex[self.thisEpochArmIndex] += 1
            # Calculate armValues
            n = sum( self.pullCount )
            for arm in range(self.noOfArms):
                try:
                    self.armValue[arm] = self.armAvgReward[arm] + \
                                            math.sqrt( ((1+self.alpha)*math.log(math.e*n/self.tau(self.rIndex[arm])))/ \
                                                       (2*self.tau(self.rIndex[arm])) )
                except ZeroDivisionError:
                    self.armValue[arm] = float( 'Inf' )
            # Find arm with highest index
            sortedIndices = sorted( range(len(self.armValue)), key=lambda i:self.armValue[i] )[::-1]
            self.thisEpochArmIndex = sortedIndices[0]
            self.stepsToCompleteThisEpoch = self.tau( self.rIndex[self.thisEpochArmIndex]+1 ) - \
                                                self.tau( self.rIndex[self.thisEpochArmIndex] )

            # return this arm
            self.stepsToCompleteThisEpoch -= 1
            return self.thisEpochArmIndex

        """----------------------------------------------------------------------"""
        """ updateRewards() : updates the observed rewards to algorithm, calculates
                              new value for each arm
                armIndices  - indices of the arms to update
                rewards     - rewards of corresponding arms
        """
        def updateRewards( self, armIndices, rewards ):
            # Check whether we have right type for armIndices
            if( not isinstance(armIndices,list) ):
                armIndices  = [ armIndices ]
            if( not isinstance(rewards,list) ):
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
            for arm in armIndices:
                self.pullCount[arm]     += 1
                self.armAvgReward[arm]   = self.armAvgReward[arm] \
                                            + 1.00/self.pullCount[arm] \
                                                * (rewards[armIndices.index(arm)]-self.armAvgReward[arm])
        """----------------------------------------------------------------------"""
        """ getStats() : get inner statistics of algorithm
                Return : depends on algorithm,
                         armPullCount, armIndices
        """
        def getStats( self ):
            return { 'pullCount' : self.pullCount,
                     'armValue'  : self.armValue,
                     'AvgReward' : self.armAvgReward,
                     'rIndex'    : self.rIndex }
        """----------------------------------------------------------------------"""
        # Any Additional functions
        """----------------------------------------------------------------------"""
        def tau( self, r ):
            return math.ceil( (1+self.alpha)**r )
        """----------------------------------------------------------------------"""


def test_UCB1():
    print "Testing UCB1..."
    r = [ 3, 5, 8, 7.9, 1 ]
    myUCB1 = UCB1( len(r) )
    for i in range(0,100):
        j = myUCB1.getArmsToPull()
        myUCB1.updateRewards( j, r[j] )
    stats = myUCB1.getStats()
    for k in stats:
        print k, " : ", stats[k]
    print "End of UCB1"

def test_UCB2():
    print "Testing UCB2..."
    r = [ 3, 5, 8, 7.9, 1 ]
    myUCB2 = UCB2( len(r), 0.2 )
    for i in range(0,100):
        j = myUCB2.getArmsToPull()
        myUCB2.updateRewards( j, r[j] )
    stats = myUCB2.getStats()
    for k in stats:
        print k, " : ", stats[k]
    print "End of UCB2"

if __name__ == '__main__':
    test_UCB1()
    test_UCB2()
