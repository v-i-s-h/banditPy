################################################################################
# TestScript  : Model - MAB
# Description : Tests model for Multi-Arm Bandit
# Author      : Vishnu Raj
# Email       : get_vichu@yahoo.com

# Changelogs

################################################################################

# Import root path
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../modules")))

# Import modules
from arms import bernoulliArm, normalArm
from models import MAB

# create some arms
bArm1 = bernoulliArm.bernoulliArm( 0.7, reward1 = 3.0, reward2 = 2.5 )
bArm2 = bernoulliArm.bernoulliArm( 0.85 )
nArm1 = normalArm.normalArm( 3.0, 2.0 )
nArm2 = normalArm.normalArm( 2.0, 5.0 )

banditArms = [ bArm1, bArm2, nArm1, nArm2 ]

# Create a bandit model using arm
bandit = MAB.MAB( banditArms )

# Pull, pull and pull!!
print bandit.pull( 1 )
print bandit.pull( 0 )
print bandit.pull( [ 1, 3] )
print bandit.pull( [] )
print bandit.tick()
