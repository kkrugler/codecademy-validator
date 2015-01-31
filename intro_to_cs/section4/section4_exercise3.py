# Here are the examples we used when we started learning about
# conditional structures, but the code has been modified to
# expose the result of the conditionals via bool variables.

age = 20
true_condition_count = 0
printed_line_count = 0

# Here we are assigning the variable is_python_broken to the
# Boolean result of evaluating the expression (3 > 4).
#
# Note that we are choosing to prefix our Boolean variable names
# with "is_".  There is no requirement to do so in Python, it's
# just another example of a useful convention, making your code
# far easier for humans to understand (i.e., good style).
# If this variable were referenced much later in the program,
# it would still be obvious that it contains some Boolean value.
# (Note, however, that such a convention arguably runs contrary
# to the entire "duck typing" philosophy!)
#
# Can you guess what value is_python_broken has immediately
# after the assignment statement below?

is_python_broken = (3 > 4)

# Assign the is_python_broken_prediction variable below to the
# value you think is_python_broken has at this point in the
# program's execution, then click the Save & Submit button to
# check your prediction.

is_python_broken_prediction = False

# Here we are using the value of the Boolean variable
# is_python_broken as the condition controlling the if clause:

if (is_python_broken):
    # The following three indented statements will execute only
    # when three is greater than four (i.e., never):
    true_condition_count = true_condition_count + 1
    print 'Are you sure Python understands arithmetic?'
    printed_line_count = printed_line_count + 1

# The following two statements will always execute.
print 'Python understands arithmetic.'
printed_line_count = printed_line_count + 1

is_python_working = (4 > 3)
if (is_python_working):
    true_condition_count = true_condition_count + 1
    print 'Here is a little proof.'
    printed_line_count = printed_line_count + 1

is_adult = (age > 20)
is_teenager = (age < 20)
is_in_limbo = (age == 20)  # Equality test uses double equals
if (is_adult):
    true_condition_count = true_condition_count + 1
    print 'I thought you were only 20!'
    printed_line_count = printed_line_count + 1
if (is_teenager):
    true_condition_count = true_condition_count + 1
    print 'I thought you had already turned 20!'
    printed_line_count = printed_line_count + 1
if (is_in_limbo):
    true_condition_count = true_condition_count + 1
    print 'That condition looks a little strange to me.'
    printed_line_count = printed_line_count + 1
    age = age + 1
print 'Anybody hungry?'
printed_line_count = printed_line_count + 1

# Note that if the code above ends up changing the age variable,
# that might invalidate the three bool variables we calculated
# before it did so.  Let's make sure all three are updated to
# reflect any such change.
is_adult = (age > 20)
is_teenager = (age < 20)
is_in_limbo = (age == 20)

if (is_adult):
    true_condition_count = true_condition_count + 1
    print 'Happy birthday!'
    print 'Now get a job, already.'
    printed_line_count = printed_line_count + 2
print 'I have a job.'
printed_line_count = printed_line_count + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the counter it refers to at this
# point in the program.

true_condition_count_prediction = 3
printed_line_count_prediction = 7

# Assign the is_many_were_true variable below to True if the
# value of the true_condition_count variable at this point in
# the program is greater than four.  Otherwise, assign it to
# False.  Design your assignment statement so that it would work
# properly even if we changed the code above, which changed the
# value of true_condition_count.  Your statement should NOT use
# an if/else conditional structure.
# (DO NOT increment EITHER counter, whether your condition is
# true or not.)

is_many_were_true = (true_condition_count > 4)

# Write your own conditional statement below that prints out
# "More than four conditions were true" whenever the value of the
# true_condition_count variable at this point in the program
# is greater than four, but use the bool variable you assigned
# above in your conditional.
# (Again, DO NOT increment EITHER counter, whether your
# condition is true or not.)

if (is_many_were_true > 4):
    print('More than four conditions were true')

# (Note how the variable name "is_many_were_true" falls somewhat
# short of correct English grammar.  Although it might instead
# be named "many_were_true", and doing so would arguably make
# the conditional structure easier for humans to read, most
# professional software developers would argue that sticking
# with the "is_" prefix is still a better convention, since it
# clarifies the type of the variable in a glance.)

# Assign the is_few_lines_printed variable below to True or False
# depending on whether the printed_line_count variable at this
# point in the program is less than ten.  Again, your code should
# work no matter what value printed_line_count has at this point,
# and should NOT use an if/else structure.
# (Again, DO NOT increment EITHER counter, whether your
# condition is true or not.)

is_few_lines_printed = (printed_line_count < 10)

# Write another conditional statement below that prints out
# "Fewer than ten lines were printed (not including this one)"
# whenever the value of the printed_line_count variable at
# this point in the program is less than ten, but use the
# bool variable you assigned above in your conditional.
# (Again, DO NOT increment EITHER counter, whether your
# condition is true or not.)

if (is_few_lines_printed):
    print 'Fewer than ten lines were printed (not including this one)'
