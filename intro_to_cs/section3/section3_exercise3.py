# This program is another puzzle that will help you test your
# understanding of nested conditional structures. As before,
# three player scores are tested and incremented according to
# the conditional structures below.  The players all start out
# with zero scores, but this time the winner will be the one who
# ends up with the HIGHEST score, and we'll also handle ties
# with a custom message announcing all co-winners.

bob_score = 0
jane_score = 0
sally_score = 0

# The following statements increment one or more of the player
# scores, possibly more than once.

if (bob_score > 1):
    jane_score = jane_score + 1
elif (sally_score < 5):
    if (jane_score > 2):
        sally_score = sally_score + 1
        sally_score = sally_score + 1
    else:
        bob_score = bob_score + 1
elif (bob_score > 0):
    jane_score = jane_score + 1
else:
    sally_score = sally_score + 1
jane_score = jane_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_1 = 1
jane_score_prediction_1 = 1
sally_score_prediction_1 = 0

################################################################
# DO NOT begin this section until you've checked your answers
# above via the Save & Submit Code button, so that the message
# from checking your code refers to the predictions below
# (rather than those above).

# The following statements increment one or more of the player
# scores, possibly more than once.  Note that the scores have
# NOT been reset to zero; they are continuing forward with the
# values that resulted from the code above.

#                    *** ATTENTION!! ***

# The following conditional structure is functionally identical
# to an if/elif/elif structure we saw in the previous exercise.
# Note the extra indentation that results when each else label
# is separated from the if condition that immediately follows it.
# It's harder to see the following as a simple sequence of tests
# performed one after the other until the first one passes.
# Using elif when possible can improve the elegance of your code.

if (jane_score > 1):
    bob_score = bob_score + 1
    sally_score = sally_score + 1
else:
    if (bob_score > 0):
        bob_score = bob_score + 1
    else:
        if (sally_score > 0):
            jane_score = jane_score + 1
            jane_score = jane_score + 1
jane_score = jane_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_2 = 2
jane_score_prediction_2 = 2
sally_score_prediction_2 = 0

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
    if (bob_score > 1):
        jane_score = jane_score + 1
        sally_score = sally_score + 1
    elif (sally_score < 1):
        bob_score = bob_score + 1
    else:
        jane_score = jane_score + 1
        jane_score = jane_score + 1
elif (bob_score > 0):
    bob_score = bob_score + 1
    if (bob_score > 3):
        jane_score = jane_score + 1
        sally_score = sally_score + 1
    elif (sally_score < 1):
        bob_score = bob_score + 1
        if (bob_score > 3):
            sally_score = sally_score + 1
    else:
        jane_score = jane_score + 1
        jane_score = jane_score + 1
else:
    sally_score = sally_score + 1
    sally_score = sally_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_3 = 4
jane_score_prediction_3 = 2
sally_score_prediction_3 = 1

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
if (sally_score < 2):
    sally_score = sally_score + 1
    sally_score = sally_score + 1
    if (sally_score > 3):
        jane_score = jane_score + 1
    else:
        if (jane_score > 2):
            bob_score = bob_score + 1
        else:
            jane_score = jane_score + 1
        sally_score = sally_score + 1
elif (jane_score < 5):
    sally_score = sally_score + 1
sally_score = sally_score + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the player score it refers to at
# this point in the program:

bob_score_prediction_4 = 5
jane_score_prediction_4 = 3
sally_score_prediction_4 = 5

################################################################
# DO NOT begin this section until you've checked your answers
# above via the Save & Submit Code button, so that the message
# from checking your code refers to the message your code is
# printing below (rather than your predictions above).

# You have an opportunity here to modify the three player scores
# so that you can test out all possible scenarios for the
# conditional code you're going to write in this final section.



# Modify the following relatively simple conditional structure by
# replacing each of its first three print statements with a
# single nested conditional structure.  Do not modify the outer
# structure at all.  Make sure that your modified code will
# always announce the correct winner or winners, no matter what
# the three player scores happen to be at this point in the
# program.  Your announcement should always list all of the
# winners and include either the word "Won" or the word "Tied".

if (bob_score > jane_score):
    if (bob_score > sally_score):
        print "Bob Won!"
    elif (sally_score > bob_score):
        print "Sally Won!"
    else:
        print "Bob and Sally Tied!"
elif (jane_score > sally_score):
    if (jane_score > bob_score):
        print "Jane Won!"
    else:
        print "Bob and Jane Tied!"
elif (sally_score > bob_score):
    if (sally_score > jane_score):
        print "Sally Won!"
    else:
        print "Jane and Sally Tied!"
else:
    print "Bob, Jane and Sally Tied!"

# Make sure you try out all possible winners and all possible
# combinations of winners (7 different announcements) by
# modifying the player scores at the top of this section.
# Once you're confident that your code works properly, remove
# those three lines of code above (lines 169-171), and then
# click the Save & Submit Code button one last time to finish
# this exercise.
