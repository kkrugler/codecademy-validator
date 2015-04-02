# Simplify the expression in the following function definition
# without affecting what the function returns, no matter what
# number is passed in its score parameter.
# For reference while you're working on your simplification,
# the original expression (before any changes) is/was:
# (not (score < 10))
def is_winner(score):
    return (score >= 10)

# The assignment statement immediately below can be modified to
# pass different values in the score parameter to is_winner(),
# so that you can check the result in the console.
# Once you're sure that your simplification to is_winner() above
# is correct, set score_1 to 100 below to let the SCT test your
# solution.
score_1 = 100

# DO NOT MODIFY the following statement:
print 'is_winner(%d) returns %s.' % (score_1, is_winner(score_1))

# Again, simplify the expression within the following function
# without affecting what the function returns, no matter what
# String is passed in its name parameter.
# For reference while you're working on your simplification,
# the original expression (before any changes) is/was:
# (not (name.lower() == 'chris'))
def is_mediocre(name):
    return (name.lower() != 'chris')

# Again, the assignment statement immediately below can be
# modified to pass different values in the name parameter to
# is_mediocre(), so that you can check the result in the console.
# Once you're sure that your simplification to is_mediocre()
# above is correct, set name_1 to 'Carol' below to let the SCT
# test your solution.
name_1 = 'Carol'

# DO NOT MODIFY the following statement:
print 'is_mediocre(%s) returns %s.' % (name_1, is_mediocre(name_1))

# Simplify the function definition below, but ensure that it
# still returns the same String as it does now for each pair of
# values passed in its name and score parameters.
# By modifying both the expression and the conditional structure,
# you should be able to eliminate all uses of the not operator.
# For reference while you're working on your simplification,
# the original conditional structure (before any changes) is/was:
#    if (not (is_winner(score)) and (not (is_mediocre(name)))):
#        return 'Hang in there, Chris!'
#    else:
#        return '%s scored %d.' % (name, score)
def encourage_chris(name, score):
    if (is_winner(score) or is_mediocre(name)):
        return '%s scored %d.' % (name, score)
    else:
        return 'Hang in there, Chris!'

# The two assignment statements immediately below can be used
# to pass different values in the name and score parameters to
# encourage_chris(), so that you can check the result in the
# console.
# Once you're sure that your simplification to encourage_chris()
# above is correct, set name_2 to 'Carol' and score_2 to 100
# below to let the SCT test your solution.
name_2 = 'Carol'
score_2 = 100

# DO NOT MODIFY the following statement:
print encourage_chris(name_2, score_2)

# The following three Boolean variables can be set to whatever
# you like to test out the code that follows:
is_a = False
is_b = False
is_c = False
is_d = False

# You probably (dimly) remember the associative property of
# addition, which states that the order in which you add terms
# in an expression doesn't change the result.  The same is true
# for the and operator.  For example, the following expression
# is guaranteed to be True, no matter what values the three
# Boolean variables have:
# DO NOT MODIFY the following conditional structure:
if (((is_a and is_b) and is_c) == (is_a and (is_b and is_c))):
    print 'Python is working.'
else:
    print 'Something has gone horribly wrong with Python!'

# The associative property of the and operator means De Morgan's
# first law can actually be used to transform more complex
# expressions, those that are composed of an arbitrary number of
# sub-expressions that are all linked together via and operators.
# For example, the following two functions are guaranteed to
# return the same value, no matter what the values of a, b and c
# might be.  Each function returns True only when all three
# parameters are False.  If any parameter is True, each function
# returns False.
# DO NOT MODIFY the definition of either function.
def function_1(is_a, is_b, is_c):
    return ((not is_a) and (not is_b) and (not is_c))

def function_2(is_a, is_b, is_c):
    return (not (is_a or is_b or is_c))

# DO NOT MODIFY the following conditional structure:
if (function_1(is_a, is_b, is_c) == function_2(is_a, is_b, is_c)):
    print 'Python is still working.'
else:
    print 'Something has gone horribly wrong with Python!'

# As you may have predicted, the or operator also has the
# associative property, which means that De Morgan's second law
# can also be used to transform more complex expressions.
# However, the two operators (and, or) do NOT associate with
# one another.  For example, the following two functions may
# or may not return the same result, depending on the parameters
# passed to each:
# DO NOT MODIFY the definition of either function.
def function_3(is_a, is_b, is_c):
    return ((is_a and is_b) or is_c)

def function_4(is_a, is_b, is_c):
    return (is_a and (is_b or is_c))

# DO NOT MODIFY the following conditional structure:
if (function_3(is_a, is_b, is_c) == function_4(is_a, is_b, is_c)):
    print 'function_3() function_4() returned the same thing.'
else:
    print 'function_3() function_4() returned different things.'

# As you may have predicted, the associative property of the or
# operator means De Morgan's second law can also be used to
# transform more complex expressions, those that are composed of
# an arbitrary number of sub-expressions that are all linked
# together via or operators.

# The following function returns True if any of its parameters
# is False, otherwise it returns False.
# DO NOT MODIFY the definition of function_5().
def function_5(is_a, is_b, is_c, is_d):
    return ((not is_a) or (not is_b) or (not is_c) or (not is_d))

# Modify the following function definition so that it always
# returns the same thing as function_5() above, but it does so
# using an expression containing only a single not operator.
def function_6(is_a, is_b, is_c, is_d):
    return (not (is_a and is_b and is_c and is_d))
