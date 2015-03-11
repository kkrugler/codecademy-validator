# The following code creates two List variables.  Note how all
# the elements in each List share the same data type.
players = ['Jane', 'bob', 'Sally', 'Dave']
scores = [6, 2, 7, 5]

# The players List above contains a typo (one player's name is
# not capitalized.  Because we can modify List elements
# directly, we can fix this WITHOUT modifying the assignment
# statement above.  Instead, fix this by adding an assignment
# statement below that uses indexing on the LEFT side of the
# equals sign to replace the player name with a correctly
# capitalized version



# The string representation of a sequence looks the same as the
# syntax you use to build a sequence literal with the same value.
# For example, the formatting operator in the following statement
# embeds the String representation of scores in message_1:
message_1 = 'scores contains %s' % scores

# Predict the value of the message_1 variable above by assigning
# message_1_prediction below to a String literal.
message_1_prediction = ''

# This function (from the previous exercise) returns a String
# describing one player's score, and which one gets described
# is controlled by the i parameter.  Note that Python's "duck
# typing" means that this function, which was designed to take
# two Tuple parameters, could also be used with two List
# parameters (or any two sequence parameters).
# Note, however, that it still assumes that every element of the
# scores sequence will be an Integer.
def player_score_message(players, scores, i):
    return '%s scored %d.' % (players[i], scores[i])

# For example, the following code describes Bob's score:
message_2 = player_score_message(players, scores, 1)

# Predict the value of the message_2 variable above by assigning
# message_2_prediction below to a String literal.
message_2_prediction = ''

# The following code removes the lowest score using the
# remove(item) method, which removes the first element it finds
# in the List whose value matches the item parameter.  Note that
# the item parameter is NOT a position in the List, but rather
# data to search for among the List's elements.
scores.remove(2)

# Again, the formatting operator in the following statement
# embeds the String representation of scores in message_3:
message_3 = 'scores now contains %s' % scores

# Predict the value of the message_3 variable above by assigning
# message_3_prediction below to a String literal.
message_3_prediction = ''

# The following code removes the second element from scores and
# assigns item to this element.  It does so by using the pop(i)
# method, which removes and returns the element immediately
# following the position specified via the i parameter.
# Note that the i parameter in this case really is a POSITION
# (NOT an item to search for in the List).
item = scores.pop(1)

# Again, the formatting operator in the following statement
# embeds the String representation of scores in message_4:
message_4 = 'scores now contains %s' % scores

# Predict the value of the message_4 variable above by assigning
# message_4_prediction below to a String literal.
message_4_prediction = ''

# The following code inserts the highest score at the very start
# of scores.  It does so by passing the position in the first
# parameter and the item in the second parameter.  The item is
# inserted immediately after this position (i.e., at the start
# for position zero).
scores.insert(0, item)

# Again, the formatting operator in the following statement
# embeds the String representation of scores in message_5:
message_5 = 'scores now contains %s' % scores

# Predict the value of the message_5 variable above by assigning
# message_5_prediction below to a String literal.
message_5_prediction = ''

# The following code tries to describe the winner's score.
# Unfortunately, since it didn't rearrange the player names in
# the same way we rearranged scores, the winner's name will be
# wrong.
message_6 = player_score_message(players, scores, 0)

# Predict the value of the message_6 variable above by assigning
# message_6_prediction below to a String literal.  Remember that
# this announces the winning score, but the name will be wrong.
message_6_prediction = ''

# Use the remove(item), pop(i) and insert(i, new_item) methods
# to rearrange the elements of the players List so that it just
# contains the three players matching the elements of scores
# (i.e., in the same order).



# Use the player_score_message function to describe the SECOND
# best player and score and send this message to the console.
# Use a SINGLE Python statement to do so.  Your statement should
# reference one element from players and one element from scores.

