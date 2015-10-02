################################################################################
# Module      : bernoulliArm
# Description : Implements a Bernoulli arm for bandit
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

import random

class bernoulliArm:
    """----------------------------------------------------------------------"""
    """ Arm Initializer :
        'p' - probability,
        'reward1' - high reward, default is 1.00
        'reward2' - low reward, default is 0.00
    """
    def __init__( self, p, reward1 = 1.0, reward2 = 0.0 ):
        self.p      = p
        self.reward1 = reward1
        self.reward2 = reward2
    """----------------------------------------------------------------------"""
    """ Function to advance by one time step, retruns None
    """
    def tick( self ):
        return None
    """----------------------------------------------------------------------"""
    """ Function to pull arm - returns either reward1 or reward2
    """
    def pull( self ):
        if( random.random() <= self.p ):
            
            return self.reward1
        else:
            return self.reward2
    """----------------------------------------------------------------------"""

# test code
if __name__ == '__main__':
    arm1 = bernoulliArm( 0.5 )
    counter = 0
    for i in range(1000):
        if( arm1.pull() == 1.0 ):
            counter += 1
        else:
            pass

    print "Arm1\n\tCounter = ", counter

    arm2 = bernoulliArm( 0.3, 4, 1 )
    counter = 0;
    for i in range(1000):
        if( arm2.pull() == 4.0 ):
            counter += 1
        else:
            pass
    print "Arm2\n\tCounter = ", counter
