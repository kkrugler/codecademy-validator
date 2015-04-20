# The following two variables are defined outside the context
# of any function.
# DO NOT modify the code in this section.
score = 6
extra_points = 2

# Each of the following four function definitions increases
# score by extra_points and then returns the new value, but
# there are subtle differences that affect which variable is
# actually being read and/or written.
#
# DO NOT modify the function definitions until directed to do so,
# and then change ONLY their global statements.

def function_1():
    global score, extra_points
    score = score + extra_points
    return score

def function_2():
    global extra_points
    score = 10
    score = score + extra_points
    return score

def function_3():
    global score, extra_points
    return score + extra_points

def function_4(score):
    global extra_points
    return score + extra_points

# The following line invokes function_1() once and then saves
# its return value.
# DO NOT modify this line.
result_1 = function_1()

# Predict the value returned from function_1() as well as the
# value of the score variable at this point in the execution by
# setting the values of the prediction variables below.
result_1_prediction = 0
score_prediction_1 = 0

# The following line invokes function_2() once and then saves
# its return value.
# DO NOT modify this line.
result_2 = function_2()

# Predict the value returned from function_2() as well as the
# value of the score variable at this point in the execution by
# setting the values of the prediction variables below.
result_2_prediction = 0
score_prediction_2 = 0

# The following line invokes function_3() once and then saves
# its return value.
# DO NOT modify this line.
result_3 = function_3()

# Predict the value returned from function_3() as well as the
# value of the score variable at this point in the execution by
# setting the values of the prediction variables below.
result_3_prediction = 0
score_prediction_3 = 0

# The following line invokes function_4() once with the
# argument 10 and then saves its return value.
# DO NOT modify this line.
result_4 = function_4(10)

# Predict the value returned from function_4() as well as the
# value of the score variable at this point in the execution by
# setting the values of the prediction variables below.
result_4_prediction = 0
score_prediction_4 = 0

# The following line invokes function_4() a second time, passing
# score as the argument and then setting score to the return
# value.
# DO NOT modify this line.
score = function_4(score)

# Predict the value of the score variable at this point in the
# execution by setting the value of the prediction variable
# below.
score_prediction_5 = 0

# Once you have successfully predicted the values of all the
# variables above (and checked your predictions by clicking the
# Save & Submit button), carefully review the global statements
# in the four function definitions above.  Remove any global
# variable names from each global statement that are not
# necessary for the function to continue behaving exactly as
# it does with the original global statement.  If you can remove
# all of the variables from a global statement, then remove the
# entire global statement.
#
# DO NOT modify any other lines in any of the four function
# definitions.
#
# Note that although the unnecessary variable names you removed
# really are global from the perspective of the function
# definitions (and this was legal Python syntax), including them
# was misleading.  Make sure you understand why.

# Once you have removed all (and only) the unnecessary variable
# names from the global statements, click the Save & Submit
# button again to check the changes you made.
#
# Just in case you weren't successful, here are the original
# global statements from the four functions so that you can
# restore them before you try again:
# function_1: global score, extra_points
# function_2: global extra_points
# function_3: global score, extra_points
# function_4: global extra_points

# Finally, there is exactly one variable name that you could add
# to one of those four global statements (that wasn't there
# originally) WITHOUT causing the program to fail with a syntax
# error.  However, doing so WILL modify the behavior of that
# function so that you must also change one or more of your
# predictions.
#
# Add that variable name to the global statement, then click the
# Save & Submit button.  You'll know you added the right one if
# no errors result, but at least one of your predictions is
# suddenly wrong.  If so, fix your prediction(s) to account for
# the new behavior of the function, then click the Save & Submit
# button to check them.
