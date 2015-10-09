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
from algorithms import UCB
from models import MAB
from models import experiment

# Plot tools
import matplotlib.pyplot as plt

# Create some arms
# arm1 = bernoulliArm.bernoulliArm( 0.70, reward1 = 5.0, reward2 = -4.0 )
# arm2 = bernoulliArm.bernoulliArm( 0.35, reward1 = 3.0 )
# arm3 = bernoulliArm.bernoulliArm( 0.40, reward1 = 3.0 )
# arm4 = bernoulliArm.bernoulliArm( 0.90, reward1 = 1.5 )
# armModels = [ arm1, arm2, arm3, arm4 ]

armModels = [
                normalArm.normalArm( 3.0 ),
                normalArm.normalArm( 4.0, 1.0 ),
                normalArm.normalArm( 5.0, 1.0 )
            ]

bandit = MAB.MAB( armModels )

algo0 = epsilonGreedy.epsilonGreedy( 0.25, len(armModels) )
algo1 = UCB.UCB1( len(armModels) )

exp0 = experiment.experiment( bandit, algo0 )
exp1 = experiment.experiment( bandit, algo1 )

# run expriment
selArmIndex0, obtainedRewards0 = exp0.run( 1000 )
selArmIndex1, obtainedRewards1 = exp1.run( 1000 )

# Get Status of experiment
stats0 = exp0.getStats()
print "Stats0 : "
for stat in stats0:
    print stat, " : ", stats0[stat]
stats1 = exp1.getStats()
print "Stats1 : "
for stat in stats1:
    print stat, " : ", stats1[stat]

# calculate cummulative rewards
cumRewards0 = [ sum(obtainedRewards0[:i+1]) for i in range(len(obtainedRewards0)) ]
cumRewards1 = [ sum(obtainedRewards1[:i+1]) for i in range(len(obtainedRewards1)) ]
# calculate average rewards till that step
avgRewards0 = [ cumRewards0[i]/float(i+1) for i in range(len(cumRewards0)) ]
avgRewards1 = [ cumRewards1[i]/float(i+1) for i in range(len(cumRewards1)) ]

# Plot results
# plt.figure( 1 )
# plt.plot( cumRewards )
# plt.ylabel( 'Cummulative Rewards' )
# plt.xlabel( 'Steps')
# plt.title( 'Cummulative Reward' )
# plt.show()

plt.figure( 1 )
plt.plot( range(1,len(cumRewards0)+1), avgRewards0, 'b-', label = "epsilon-Greedy" )
plt.plot( range(1,len(cumRewards1)+1), avgRewards1, 'r-', label = "UCB1" )
plt.ylabel( 'Average Reward' )
plt.xlabel( 'Steps' )
plt.title( 'Average Reward' )
plt.legend()
plt.show()

# plt.figure( 3 )
# plt.plot( list(range(1,len(selArmIndex)+1)), selArmIndex, 'ro' )
# plt.xlabel( 'Steps' )
# plt.ylabel( 'Selected Arm' )
# plt.title( 'Selected Arm' )
# plt.show()
