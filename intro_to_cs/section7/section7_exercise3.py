# We mentioned the modulo operator (%) briefly when we were
# studying integer division.  It's different from the formatting
# operator, even though both use the same character.
# The modulo operator returns the remainder of integer division.
# Note the result of the modulo operator sent to the console by
# the following statements.
# DO NOT modify the code in this section.
print '(9 % 3) = ' + str(9 % 3)
print '(9 % 5) = ' + str(9 % 5)
print '(5 % 2) = ' + str(5 % 2)
print '(4 % 2) = ' + str(4 % 2)
print '(14 % 2) = ' + str(14 % 2)
print '(256 % 2) = ' + str(256 % 2)
print '(257 % 2) = ' + str(257 % 2)

# As you can see, (number % 2) returns 0 whenever number is even,
# and it returns 1 whenever number is odd.
# Thus, ((number % 2) == 0) will be True whenever number is even,
# a handy test that we'll use in the code that follows.

# The following code contains just one fairly simple loop and
# two Integer variables.  However, it's still far from trivial
# to predict what values the variables will have after the loop
# terminates.
# DO NOT modify the code in this section.
score = 0
num_twists = 0
while (num_twists < 10):
    score = score + 1
    if ((score % 2) == 0): # (returns True if score is even)
        num_twists = num_twists + 1

# Predict the values that each of the two variables used above
# have at this point in the program by assigning the
# score_prediction_1 and num_twists_prediction_1 variables below.
score_prediction_1 = 20
num_twists_prediction_1 = 10

# Here's the same code, except with the introduction of a single
# conditional break statement.  You can still figure it out, but
# the break statement certainly makes doing so more difficult.
# DO NOT modify the code in this section.
score = 0
num_twists = 0
while (num_twists < 10):
    score = score + 1
    if (score > 17):
        break
    if ((score % 2) == 0): # (returns True if score is even)
        num_twists = num_twists + 1

# Again, predict the values that each of the two variables have
# now by assigning the score_prediction_2 and
# num_twists_prediction_2 variables below.
score_prediction_2 = 18
num_twists_prediction_2 = 8

# Here's the same code, except with the introduction of a single
# conditional continue statement.  Again, you can still figure
# it out, but the continue statement also makes doing so more
# difficult.
# DO NOT modify the code in this section.
score = 0
num_twists = 0
while (num_twists < 10):
    score = score + 1
    if (score < 7):
        continue
    if ((score % 2) == 0): # (returns True if score is even)
        num_twists = num_twists + 1

# Again, predict the values that each of the two variables have
# now by assigning the score_prediction_3 and
# num_twists_prediction_3 variables below.
score_prediction_3 = 26
num_twists_prediction_3 = 10
