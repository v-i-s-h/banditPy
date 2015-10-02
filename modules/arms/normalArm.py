################################################################################
# Module      : normalArm
# Description : Implements a Normal distribution arm
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

import random

class normalArm:
    """----------------------------------------------------------------------"""
    """ Arm Initializer """
    def __init__( self, mu = 0.00, sigma = 1.00 ):
        self.mu     = mu
        self.sigma  = sigma
    """----------------------------------------------------------------------"""
    """ Function to advance by one time step, retruns None
    """
    def tick( self ):
        return None
    """----------------------------------------------------------------------"""
    """ Function to pull arm - returns either reward1 or reward2
    """
    def pull( self ):
        reward = None
        reward = random.gauss( self.mu, self.sigma )
        return reward

# test code
if __name__ == '__main__':
    arm1    = normalArm()
    sum     = 0.00
    for i in range( 1000 ):
        sum += arm1.pull()
    print "Normal Arm 1 -- Average = ", sum/1000

    arm2    = normalArm( 5.00 )
    sum     = 0.00
    for i in range( 1000 ):
        sum += arm2.pull()
    print "Normal Arm 2 -- Average = ", sum/1000

    arm3    = normalArm( 5.00, 30.00 )
    sum     = 0.00
    for i in range( 1000 ):
        sum += arm3.pull()
    print "Normal Arm 3 -- Average = ", sum/1000
