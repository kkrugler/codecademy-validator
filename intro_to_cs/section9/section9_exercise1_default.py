# The score variable below is initially assigned to the value 10.
score = 10

# The inflate_score() function takes a score parameter, but its
# "scope" is limited to the function definition.  Even though
# this parameter is using the same identifier name as the score
# variable defined outside this function, they remain two
# completely separate variables.
# The score parameter is initially assigned to whatever value the
# caller passes into the function (i.e., regardless of the value
# of the similarly named variable outside).
# Reassigning the score parameter to some other value can only
# affect variables outside the function definition via the
# return value (and what the caller chooses to do with it).
def inflate_score(score):
    score = score + 4
    return score + 1

# Predict the value of the score variable at this point in the
# program by assigning score_prediction_1 below.
score_prediction_1 = 0

# Here we call the inflate_score() function, providing a value
# (known as a function "argument" here on the caller's side)
# which is 10 greater than the current value of score.  We take
# the value returned from the function and assign a new variable
# inflated_score to it.
inflated_score = inflate_score(score + 10)

# Predict the value of both the score and inflated_score
# variables at this point in the program by assigning
# score_prediction_2 and inflated_score_prediction_2 below.
score_prediction_2 = 0
inflated_score_prediction_2 = 0

# This function takes two parameters which happen to share their
# names with two variables defined outside the function.  It
# returns the difference between the parameter values passed in
# by its caller.  Along the way, it reassigns one of these
# parameters, but doing so does not directly affect any variable
# outside this function definition.
def calculate_inflation(score, inflated_score):
    inflated_score = inflated_score - score
    return inflated_score

# Again, predict the value of the score and inflated_score
# variables at this point in the program by assigning
# score_prediction_3 and inflated_score_prediction_3 below.
score_prediction_3 = 0
inflated_score_prediction_3 = 0

# Here we call the calculate_inflation() function, providing
# the current values of the score and inflated_score variables
# as the function arguments.  We also assign inflation to the
# value returned from the function.
inflation = calculate_inflation(score, inflated_score)

# Predict the values of the score, inflated_score and inflation
# variables at this point in the program by assigning the three
# variables below:
score_prediction_4 = 0
inflated_score_prediction_4 = 0
inflation_prediction_4 = 0

# Here we call calculate_inflation() again.
score = score + calculate_inflation(score, inflated_score)

# Finally, predict the values of the score, inflated_score and
# inflation variables at this point in the program by assigning
# the three variables below:
score_prediction_5 = 0
inflated_score_prediction_5 = 0
inflation_prediction_5 = 0
