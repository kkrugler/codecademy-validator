# This program is a puzzle that will help you test your
# understanding of if/elif/else structures.  Three player
# scores are tested and incremented according to the if/elif/else
# statements below.  The players all start out with zero scores,
# and the winner will be the one who ends up scoring 5 or more.

bob_score = 0
jane_score = 0
sally_score = 0

# The following statements increment one or more of the player
# scores, possibly more than once.

if (bob_score < 5):
    jane_score = jane_score + 1
elif (sally_score < 1):
    sally_score = sally_score + 1
elif (jane_score < 100):
    bob_score = bob_score + 1
else:
    sally_score = sally_score + 1
    sally_score = sally_score + 1
sally_score = sally_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_1 = 0
jane_score_prediction_1 = 1
sally_score_prediction_1 = 1

################################################################
# DO NOT begin this section until you've checked your answers
# above via the Save & Submit Code button, so that the message
# from checking your code refers to the predictions below
# (rather than those above).

# The following statements increment one or more of the player
# scores, possibly more than once.  Note that the scores have
# NOT been reset to zero; they are continuing forward with the
# values that resulted from the code above.

if (jane_score > 1):
    bob_score = bob_score + 1
    sally_score = sally_score + 1
elif (bob_score > 0):
    bob_score = bob_score + 1
elif (sally_score > 0):
    jane_score = jane_score + 1
    jane_score = jane_score + 1
jane_score = jane_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_2 = 0
jane_score_prediction_2 = 4
sally_score_prediction_2 = 1

################################################################
# DO NOT begin this section until you've checked your answers
# above via the Save & Submit Code button, so that the message
# from checking your code refers to the predictions below
# (rather than those above).

# The following statements increment one or more of the player
# scores, possibly more than once.  Note that the scores have
# NOT been reset to zero; they are continuing forward with the
# values that resulted from the code above.

if (jane_score < 2):
    jane_score = jane_score + 1
    sally_score = sally_score + 1
elif (sally_score < 2):
    bob_score = bob_score + 1
    jane_score = jane_score + 1
    sally_score = sally_score + 1
else:
    bob_score = bob_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_3 = 1
jane_score_prediction_3 = 5
sally_score_prediction_3 = 2

################################################################
# DO NOT begin this section until you've checked your answers
# above via the Save & Submit Code button, so that the message
# from checking your code refers to the predictions below
# (rather than those above).

# The following statements increment one or more of the player
# scores, possibly more than once.  Note that the scores have
# NOT been reset to zero; they are continuing forward with the
# values that resulted from the code above.

bob_score = bob_score + 1
if (bob_score > 2):
    jane_score = jane_score + 1
elif (jane_score < 5):
    sally_score = sally_score + 1
bob_score = bob_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_4 = 3
jane_score_prediction_4 = 5
sally_score_prediction_4 = 2

################################################################
# DO NOT begin this section until you've checked your answers
# above via the Save & Submit Code button, so that the message
# from checking your code refers to the message your code is
# printing below (rather than your predictions above).

# You have an opportunity here to modify the three player scores
# so that you can test out all possible scenarios for the
# conditional code you're going to write in this final section.


# Write a simple if/elif/else structure below that announces the
# winner of the contest above by printing a message to the
# console of the form "Sally Won!" (but using correct name).
# Just print a simple String literal rather than using the
# formatting operator.   Make sure that your code would work
# no matter who actually wins.  It's OK to have a bias for one
# player if two players score 5 or more.

if (bob_score > 4):
    print "Bob Won!"
elif (jane_score > 4):
    print "Jane Won!"
else:
    print "Sally Won!"

# Make sure you try out all possible winners above by modifying
# the player scores at the top of this section.  Once you're
# confident that your code works properly, remove those three
# lines of code above (lines 127-129), and then click the
# Save & Submit Code button one last time to finish the
# exercise.
