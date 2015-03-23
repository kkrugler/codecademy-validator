# Each of the following four statements uses the and operator to
# assign the value of a Boolean variable, by combining the
# results from two arithmetic sub-expressions.
and_result_1 = ((3 > 4) and (1 <= 2))
and_result_2 = ((5 > 4) and (1 <= 2))
and_result_3 = ((5 > 4) and (1 == 0))
and_result_4 = ((3 > 4) and (1 != 1))

# Predict the values of the four results above by assigning each
# of the four prediction variables below to a simple Boolean
# literal value.
and_result_1_prediction = False
and_result_2_prediction = True
and_result_3_prediction = False
and_result_4_prediction = False

# Each of the following four statements uses the or operator to
# assign the value of a Boolean variable, by combining the
# results from two arithmetic sub-expressions.
or_result_1 = ((3 > 4) or (1 <= 2))
or_result_2 = ((5 > 4) or (1 <= 2))
or_result_3 = ((5 > 4) or (1 == 0))
or_result_4 = ((3 > 4) or (1 != 1))

# Again, predict the values of the four results above by
# assigning each of the four prediction variables below to a
# simple Boolean literal value.
or_result_1_prediction = True
or_result_2_prediction = True
or_result_3_prediction = True
or_result_4_prediction = False

# Modify the definitions of each of the following four functions
# so that they still return the same value for every input
# number, but none of them use the not operator.  You shouldn't
# have to use either of the other two Boolean operators either.
def is_not_less_than_four(number):
    return (number >= 4)

def is_not_equal_to_seven(number):
    return (number != 7)

def is_not_different_from_42(number):
    return (number == 42)

def is_not_greater_than_or_equal_to_five(number):
    return (number < 5)

# Modify the definition of the following function so that it
# still returns the same value for every pair of input numbers,
# but does so using a SINGLE conditional structure with no elif
# or else clauses.
def is_clear_winner(score, other_score):
    return ((score > other_score) and (score >= 5))
