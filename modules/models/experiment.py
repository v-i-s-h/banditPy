################################################################################
# Module      : Experiment
# Description : Implements model for running experiment
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Description : Implements model for running an experiment. Takes a bandit, an
#               algorithm, and number of steps to run.
#               Returns index of arms selected at each step and reward obtained
#               at each step.

# Changelogs

################################################################################

class experiment( object ):
    """----------------------------------------------------------------------"""
    """ Initialization : Initializes experiment with bandit model and experiment
            Returns : None
    """
    def __init__( self, banditModel, algorithm ):
        self.banditModel    = banditModel
        self.algorithm      = algorithm
        self.tickCounter    = 0

        # list for returning experiment results
        self.selectedIndices = []   # Nothing
        self.obtainedRewards = []   # Nothing
    """----------------------------------------------------------------------"""
    """ run() : Runs experiment for specified number of steps
                noOfSteps - Number of steps to run
            Returns : list of arms selected at each step, reward obtained
    """
    def run( self, noOfSteps ):
        for step in range(0,noOfSteps):
            armsToPull = self.algorithm.getArmsToPull()
            thisReward = self.banditModel.pull( armsToPull )
            self.algorithm.updateRewards( armsToPull, thisReward )

            # save results
            self.selectedIndices += [ armsToPull ]
            self.obtainedRewards += [ thisReward ]

        return self.selectedIndices, self.obtainedRewards
    """----------------------------------------------------------------------"""
    """ getStats() : Passes internal state of algorithm
            Returns : tuple of internal state of algorithm, as returned by
                        algorithm
    """
    def getStats( self ):
        return self.algorithm.getStats()
    """----------------------------------------------------------------------"""
    """ reset() : Resets algorithm
            Returns : None
    """
    def reset( self ):
        self.algorithm.reset()
    """----------------------------------------------------------------------"""
