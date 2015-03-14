# The following code creates two List variables.  Note how all
# the elements in each List share the same data type.
# DO NOT modify the code in this section.
players = ['Jane', 'Bob', 'Sally', 'Dave']
scores = [6, 2, 7, 5]

# The following code sorts the elements of both the players and
# their scores so that higher scores (and associated players)
# appear first in each List.
# Note that the ORDER in which we perform these assignments
# matters, but that this is not the only order in which we could
# have moved elements to achieve the same sort order.
# Finally, note that we needed an extra place (the player_1
# variable) to hold one element while we were sorting the others.
# Be absolutely certain that you understand why the player_1
# variable was necessary.
# DO NOT modify the code in this section.
player_1 = players[0]   # Saving Jane
players[0] = players[2] # Moving Sally
players[2] = players[3] # Moving Dave
players[3] = players[1] # Moving Bob
players[1] = player_1   # Moving Jane
score_1 = scores[0]     # Saving 6
scores[0] = scores[2]   # Moving 7
scores[2] = scores[3]   # Moving 5
scores[3] = scores[1]   # Moving 2
scores[1] = score_1     # Moving 6

# Predict the string representation of the scores List at this
# point in the program by assigning scores_string_prediction_1
# below to a String Literal.
scores_string_prediction_1 = '[7, 6, 5, 2]'

# Use a series of assignment statements to re-sort both the
# players and their scores so that LOWER scores (and associated
# players) appear first in each List.
player_0 = players[3]
players[3] = players[0]
players[0] = player_0
player_1 = players[2]
players[2] = players[1]
players[1] = player_1
score_0 = scores[3]
scores[3] = scores[0]
scores[0] = score_0
score_1 = scores[2]
scores[2] = scores[1]
scores[1] = score_1

# Predict the string representation of the scores List now
# by assigning scores_string_prediction_2 below to a String
# Literal.
scores_string_prediction_2 = '[2, 5, 6, 7]'

# The following statements create copies of the two Lists in
# their original (unsorted) orders.
# DO NOT modify the code in this section.
players_copy = ['Jane', 'Bob', 'Sally', 'Dave']
scores_copy = [6, 2, 7, 5]

# Use a series of assignment statements to sort both the
# players_copy and scores_copy Lists so that HIGHER scores
# (and associated players) appear first in each List.
# However, do so using a DIFFERENT sequence of assignment
# statements than the one used by the code that sorted players
# and scores this way the first time.
player_2 = players_copy[3]
players_copy[3] = players_copy[1]
players_copy[1] = players_copy[0]
players_copy[0] = players_copy[2]
players_copy[2] = player_2
score_2 = scores_copy[3]
scores_copy[3] = scores_copy[1]
scores_copy[1] = scores_copy[0]
scores_copy[0] = scores_copy[2]
scores_copy[2] = score_2
