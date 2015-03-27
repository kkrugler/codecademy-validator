# The following function returns True if score (which is assumed
# to be a number) is higher than any of the elements of scores
# (which is assumed to be a List of numbers).
# It also keeps track of all the unique score values it has ever
# seen by appending ones never seen before to scores.  Note that
# the append(new_item) List method (which we haven't seen before)
# is sort of like insert(len(scores), new_item), meaning it just
# adds the new item to the end of the scores List.
# DO NOT modify the code in this function.
def is_best(score, scores):
    result = True
    is_new = True
    for other_score in scores:
        if (other_score >= score):
            result = False
            if (other_score == score):
                is_new = False
    if (is_new):
        scores.append(score)
    return result

# The following function sends an announcement to the console
# whenever score is the best score seen thus far.
def announce_leader(score, scores):
    if (is_best(score, scores)):
        print 'The new leader has a score of %d.' % score

# The following code considers a series of input scores, sending
# an announcement to the console whenever a new leader is
# encountered.
# DO NOT modify the code in this section.
input_scores = [3, 2, 5, 5, 3, 7, 6, 10]
print 'Considering %s...' % input_scores
unique_scores_1 = []
for score in input_scores:
    announce_leader(score, unique_scores_1)
string_1 = str(unique_scores_1)

# Predict the contents of string_1 by assigning
# string_1_prediction below to a literal String.
# Recall that the str() built-in function will return the
# string representation of a List, which looks the same as the
# syntax you use to build a List literal with the same value.
string_1_prediction = ''

# The following function tries to do the same thing as the
# announce_winner() function above.  However, it's designed to
# be a little more efficient at finding the winner, because
# it assumes at least one player will reach 5.
# Unfortunately, it fails to consider two side effects of the
# is_best() function.
# DO NOT modify the code in this function.
def announce_leader_faster(score, scores):
    if (score >= 5) and (is_best(score, scores)):
        print 'The new leader has a score of %d.' % score

# The following code considers the same series of scores,
# again sending an announcement to the console whenever a new
# leader is encountered.  Note the difference in the output
# sent to the console this time, due to the first side effect
# that announce_leader_faster() failed to consider.
# DO NOT modify the code in this section.
print 'Considering %s more efficiently...' % input_scores
unique_scores_2 = []
for score in input_scores:
    announce_leader_faster(score, unique_scores_2)
string_2 = str(unique_scores_2)

# Predict the contents of the unique_scores_2 variable at this
# point in the execution by setting the value of the prediction
# variable below to a literal list of integers.
# Again, predict the contents of string_2 by assigning
# string_2_prediction below to a String literal.
string_2_prediction = ''

# The following List of input scores tries to represent the fact
# that if a player doesn't reach at least 5, the score should be
# disqualified.
# DO NOT modify this List.
valid_input_scores = [None, None, 5, 5, None, 7, 6, 10]

# The following code would try to consider this list using the
# (original) announce_leader() function, but that's not going to
# work properly.  Change False to True in the line immediately
# below to see what happens.
if False:
    print 'Considering %s...' % valid_input_scores
    unique_scores_3 = []
    for score in valid_input_scores:
        announce_leader(score, unique_scores_3)

# Finally, modify the announce_leader() function near the top of
# this file so that it "short circuits" the call to is_best()
# whenever score is None, thereby "guarding" that call against
# such an unexpected input score.  Your modification should not
# add any lines of code to announce_leader(), but should instead
# make one line just a little more complex.
