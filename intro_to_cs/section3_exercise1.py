# This program is designed to count the number of conditions
# that it finds to be true, as well as the number of lines of
# text it displays in the console.  It does so by adding one to
# the current value of the variable true_condition_count
# (also known as "incrementing" the variable) after each true
# condition.  It also increments printed_line_count after
# sending each line of text to the console.
#
# Read over the code carefully, then make predictions by setting
# the values of the two variables near the end of the program.

age = 20
true_condition_count = 0
printed_line_count = 0

if (3 > 4):
    # The following three indented statements will execute only
    # when three is greater than four (i.e., never):
    true_condition_count = true_condition_count + 1
    print 'Are you sure Python understands arithmetic?'
    printed_line_count = printed_line_count + 1

# The following two statements will always execute.  In Python,
# the first statement that is NOT indented marks the end of the
# conditional block of statements (i.e., those that were
# dependent on the first condition test).
print 'Python understands arithmetic.'
printed_line_count = printed_line_count + 1

if (4 > 3):
    true_condition_count = true_condition_count + 1
    print 'Here is a little proof.'
    printed_line_count = printed_line_count + 1

# Note that an empty line is NOT required to signal the end of
# a conditional block.  However, empty lines (like comments) can
# make it easier for other humans to understand your code.
if (age > 20):
    true_condition_count = true_condition_count + 1
    print 'I thought you were only 20!'
    printed_line_count = printed_line_count + 1
if (age < 20):
    true_condition_count = true_condition_count + 1
    print 'I thought you had already turned 20!'
    printed_line_count = printed_line_count + 1

# Testing for equality in most (but not all) programming
# languages is done with a double equals sign, to distinguish it
# from an assignment statement.  Here we DON'T want to ASSIGN
# age to 20; we want to TEST whether age ALREADY equals 20.
if (age == 20):
    true_condition_count = true_condition_count + 1
    print 'That condition looks a little strange to me.'
    printed_line_count = printed_line_count + 1
    age = age + 1
print 'Anybody hungry?'
printed_line_count = printed_line_count + 1

if (age > 20):
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

# Write your own conditional statement below that prints out
# "More than four conditions were true", but only if the value
# of the true_condition_count variable at this point in the
# program is greater than four.
# (DO NOT increment EITHER variable, whether your condition is
# true or not.)

if (true_condition_count > 4):
    print('More than four conditions were true')

# Write another conditional statement below that prints out
# "Less than ten lines were printed (not including this one)",
# but only if the value of the printed_line_count variable at
# this point in the program is less than ten.
# (Again, DO NOT increment EITHER variable, whether your
# condition is true or not.)

if (printed_line_count < 10):
    print 'Less than ten lines were printed (not including this one)'
