# The following function always returns the largest of the two
# numeric values passed to it by its caller.
#
# Note: The last statement doesn't have to be in the else clause
# of the conditional, because the first return statement will
# exit the function completely.

def biggest_value(value_1, value_2):
    if (value_1 > value_2):
        return value_1
    return value_2

# You have an opportunity here to modify the two values passed
# to biggest_value() to test out its operation.  Make sure you
# try out all three cases before going on.
#
# Did you notice that the caller has its own names for the
# parameters it is passing to biggest_value()?

first_value = 0
second_value = 1
if (first_value < 100):
    print biggest_value(first_value, second_value)

# Once you've tried all three cases (and checked the console
# output for each), set first_value to 100 above to signal that
# you're ready to go on.

################################################################
# DO NOT begin this section until you've tried all three cases
# above via the Save & Submit Code button, and have then set
# first_value as directed above.

# The following function definition is supposed to return the
# smallest of the two numeric values passed by its caller.
# However, it always returns the second value.  Modify this
# function definition so that it always returns the smallest
# value.

def smallest_value(value_1, value_2):
    return value_2

# The following code calls the smallest_value() function several
# times with different inputs, and prints the result each time.
# DO NOT modify any of this code, but check the console output.

if (first_value > 99):
    print "Testing smallest_value()..."
    print smallest_value(0, 1)
    print smallest_value(1, 0)
    print smallest_value(1, 1)
    print smallest_value(-4, 0)

################################################################
# DO NOT begin this section until you've carefully checked the
# console output produced by the four calls to smallest_value()
# above.

# You have an opportunity here to modify the three player scores
# so that you can test out all possible scenarios for the
# conditional code in the function definition below.

bob_score = 0
jane_score = 0
sally_score = 0

# Modify the following relatively simple conditional structure by
# replacing each of its first three return statements with a
# single nested conditional structure.  Do not modify the outer
# structure at all.  Make sure that your modified code will
# always return the correct winner or winners, no matter what
# the three player scores happen to be at this point in the
# program.  The String you return should always list all of the
# winners and include either the word "Won" or the word "Tied".
#
# You may go back to the previous exercise, copy your conditional
# section and then paste it in here.  However, after doing so
# you will then need to indent every line in the conditional an
# extra 4 spaces so that Python will consider these statements
# part of the get_announcement() function.  You will also have to
# replace every print statement with a return statement.

def get_announcement(bob_score, jane_score, sally_score):
    if (bob_score > jane_score):
        return "Bob Won!"
    elif (jane_score > sally_score):
        return "Jane Won!"
    elif (sally_score > bob_score):
        return "Sally Won!"
    else:
        return "Bob, Jane and Sally Tied!"

# Here is the function call to get_announcement() that
# (as long as bob_score is less than 100) will execute
# get_announcement() exactly once with the scores you set above.

if (first_value > 99):
    if (bob_score < 100):
        print "Testing get_announcement..."
        line = get_announcement(bob_score, jane_score, sally_score)
        print line

# However, if bob_score is 100 or greater, the SCT for this
# exercise (which is hidden from you) will instead call
# get_announcement() many times with different scores to verify
# that it really does behave properly for all possible cases.
# It doesn't bother printing those announcements in the console,
# however.
