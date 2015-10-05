################################################################################
# TestScript  : Model - Experiment
# Description : Tests model for running experiments
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
from algorithms import epsilonGreedy
from models import MAB
from models import experiment

# Create some arms
arm1 = bernoulliArm.bernoulliArm( 0.70, reward1 = 5.0, reward2 = 0.0 )
arm2 = bernoulliArm.bernoulliArm( 0.35, reward1 = 3.0 )
arm3 = bernoulliArm.bernoulliArm( 0.40, reward1 = 3.0 )
arm4 = bernoulliArm.bernoulliArm( 0.90, reward1 = 1.5 )
armModels = [ arm1, arm2, arm3, arm4 ]

bandit = MAB.MAB( armModels )

algo = epsilonGreedy.epsilonGreedy( 0.25, len(armModels) )

exp = experiment.experiment( bandit, algo )

# run expriment
exp.run( 1000 )
# indices, rewards = exp.run()
# print "Indices : ", indices
# print "Rewards : ", rewards

# Get Status of experiment
stats = exp.getStats()
print "Stats : ", stats
