# Just like in mathematics, the order of operation often makes a
# difference in the value of an expression.  The first expression
# lets operator precedence control the order of operation,
# whereas the parentheses control it in the other two.
result_1 = 8 - 4 / 2
result_2 = (8 - 4) / 2
result_3 = 8 - (4 / 2)

# Predict the values of the three results above by setting the
# value of each of the three prediction variables below to a
# simple Integer Literal value.
result_1_prediction = 6
result_2_prediction = 2
result_3_prediction = 6

# We've been using some of the arithmetic comparison operators,
# but here's the complete set.  The following 8 expressions all
# evaluate to True (as you can see in the console):
print (4 == 4)  # equal to
print (4 != 5)  # not equal to
print (4 > 3)   # greater than
print (4 >= 3)  # greater than or equal to
print (4 >= 4)  # greater than or equal to
print (4 < 5)   # less than
print (4 <= 5)  # less than or equal to
print (4 <= 4)  # less than or equal to

# Whereas the following 6 expressions all evaluate to False:
print (4 == 5)  # equal to
print (4 != 4)  # not equal to
print (3 > 3)   # greater than
print (3 >= 4)  # greater than or equal to
print (4 < 4)   # less than
print (5 <= 4)  # less than or equal to

# Here are some more arithmetic operators.  There are a few
# that we've neglected to list (e.g., the bitwise operators),
# but they'd be esoteric at this point in our study.
print +3        # positive prefix (doesn't affect value at all)
print -3        # negation prefix
print 13 / 5    # truncated quotient of integer division
print 13 % 5    # remainder of integer division (modulus)
print 2 ** 3    # exponentiation (e.g., 2 raised to 3rd power)

# Expressions can obviously be made arbitrarily complex by
# combining operations.
result_4 = (((3 ** ((25 / 5) - 2)) + 3) % 7) * 4

# Predict the result of the expression above by setting the
# value of the prediction variable below to a simple Integer
# Literal value.
result_4_prediction = 8
