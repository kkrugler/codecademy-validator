# The following code creates a Tuple containing three elements
# so that the formatting operator can insert them into the
# matching placeholders in the template String, then assigns
# the text variable to the resulting String.  Note that the
# three elements in the Tuple all had different data types.
is_correct = True
name = 'Sean'
score = 86
message_1 = 'It is %s that %s scored %d.' % (is_correct, name, score)

# Predict the value of the message_1 variable above by assigning
# message_1_prediction below to a String literal.
message_1_prediction = ''

# The following code creates two Tuple variables.  Note how all
# the elements in each Tuple share the same data type.
players = ('Jane', 'Bob', 'Sally', 'Dave')
scores = (6, 2, 7, 5)

# This function returns a String describing one player's score,
# and which one gets described is controlled by the i parameter.
# (It's very common programming style to use a variable named i
# for the index into a sequence of elements like a Tuple.)
# Note that this function assumes that every element of the
# scores Tuple will be an Integer.
def player_score_message(players, scores, i):
    return '%s scored %d.' % (players[i], scores[i])

# For example, the following code describes Bob's score:
message_2 = player_score_message(players, scores, 1)

# Predict the value of the message_2 variable above by assigning
# message_2_prediction below to a String literal.
message_2_prediction = ''

# The following code builds a new Tuple from the best three
# elements of the scores Tuple and then tries to describe the
# winner's score.  Unfortunately, since it didn't rearrange the
# player names too, the winner's name will be wrong.
best_3_scores = (scores[2], scores[0], scores[3])
message_3 = player_score_message(players, best_3_scores, 0)

# Predict the value of the message_3 variable above by assigning
# message_3_prediction below to a String literal.  Remember that
# this announces the winning score, but the name will be wrong.
message_3_prediction = ''

# Assign a new Tuple of player names to best_3_players below
# using the elements from players that match the elements of
# best_scores (i.e., put the names in the same order).
# Reference the elements of the players Tuple rather than using
# new String literals for your elements.
best_3_players = ()

# Use the player_score_message function to describe the SECOND
# best player and score and send this message to the console.
# Use a SINGLE Python statement to do so.  Your statement should
# reference one element from best_3_players and one element from
# best_3_scores.


# Here are some examples of slicing a Tuple containing the first
# five letters of the alphabet (including a few slicing methods
# that we haven't seen previously).  Note the Tuple that results
# from each slice by checking how its String representation
# appears in the console.
letters = ('A', 'B', 'C', 'D', 'E')
print 'letters = %s' % str(letters)
print 'letters[0:4] = %s' % str(letters[0:4])
print 'letters[:4] = %s' % str(letters[:4])
print 'letters[0:] = %s' % str(letters[0:])
print 'letters[:] = %s' % str(letters[:])
print 'letters[1:3] = %s' % str(letters[1:3])
print 'letters[1:5] = %s' % str(letters[1:5])
print 'letters[1:100] = %s' % str(letters[1:100])

# Finally, assign best_2_players below to a Tuple containing the
# best TWO player names, but change the statement below to take
# a SLICE of the best_3_players Tuple to do so.
best_2_players = best_3_players
