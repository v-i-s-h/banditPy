################################################################################
# Module      : <Module Name>
# Description : <Algorithm Description>
# Author      : <Your Name>
# Email       : <Your email>

# Changelogs

################################################################################

import math

MODULE_NAME = "MODULE_NAME_HERE"

################################################################################
# Description : <Any references to the algorithm>
################################################################################
class algoName( object ):
        """----------------------------------------------------------------------"""
        # Mandatory Functions
        """----------------------------------------------------------------------"""
        """ Initialization : set the parameters for algorithm
                <param : description>
        """
        def __init__( self, noOfArms, otherParams ):
            # Do Initialization here

            # Optional Reset init the internal values
            # self.reset()
        """----------------------------------------------------------------------"""
        """ reset() : function to reset the internal values of algorithm
        """
        def reset( self ):
            # Reset internal values to default
            pass
        """----------------------------------------------------------------------"""
        """ getArmsToPull() : returns indices of best armsToPull
                noOfArms    - (optional) number of arms required
        """
        def getArmsToPull( self, noOfArms = 1 ):
            pass
        """----------------------------------------------------------------------"""
        """ updateRewards() : updates the observed rewards to algorithm, calculates
                              new value for each arm
                armIndices  - indices of the arms to update
                rewards     - rewards of corresponding arms
        """
        def updateRewards( self, armIndices, rewards ):
            pass
        """----------------------------------------------------------------------"""
        """ getStats() : get inner statistics of algorithm
                Return : depends on algorithm,
                         armPullCount, armIndices
        """
        def getStats( self ):
            pass
        """----------------------------------------------------------------------"""
        # Any Additional functions
        """----------------------------------------------------------------------"""

""" Test Function for algorithm """
def test_algoName():
    pass

if __name__ == '__main__':
    test_algoName()
