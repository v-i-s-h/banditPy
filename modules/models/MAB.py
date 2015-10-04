################################################################################
# Module      : MAB
# Description : Implements model for Multi-Arm Bandit
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

class MAB( object ):
    """----------------------------------------------------------------------"""
    """ Initializer : Initializes MAB model with arms
    """
    def __init__( self, arms = [] ):
        self.arms = arms
        self.tickCounter = 0
    """----------------------------------------------------------------------"""
    """ Pull : Pull arms
            armsToPull : Array of Index of arms to Pull
        Retruns : Array of rewards from each arm
    """
    def pull( self, armsToPull ):
        thisArmReward = 0;
        thisRoundReward = []
        if( type(armsToPull) == int ):
            armsToPull = [ armsToPull ]

        #Pull arm with given Index
        for i in range(0,len(armsToPull)):
            thisArmReward = self.arms[armstoPull[i]].pull()
            thisRoundReward += [ thisArmReward ]

        # Tick through other arms
        for i in range(0,len(arms):
            if i not in armstoPull:
                self.arms[i].tick()
    """----------------------------------------------------------------------"""
    """ Tick : Tick through each arm once
    """
    def tick( self ):
        for i in range(0,len(arms)):
            self.arms[i].tick()
    """----------------------------------------------------------------------"""
