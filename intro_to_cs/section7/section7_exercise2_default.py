# The following code iterates over a Tuple of rooms, counts them
# and might do something special for one or more of them.
rooms = ('kitchen', 'pantry', 'garage', 'bedroom')
num_rooms = 0
for room in rooms:
    if (room.find('a') > 0):
        room_a = room
    num_rooms = num_rooms + 1

# Predict the values of the num_rooms and room_a variables at
# this point in the program by setting the prediction variables
# to Literal values below.
num_rooms_prediction = 0
room_a_prediction = ''

# As long as there is at least one iteration, the control
# variable will still have the last element in it after the loop
# terminates.  Predict the value of the control variable at this
# point in the program by setting the prediction variable to
# a Literal String below.
room_prediction = ''

# The following code creates two List variables.
# DO NOT modify the code in this section.
players = ['Jane', 'Bob', 'Sally', 'Dave']
scores = [6, 2, 7, 5]

# The following code finds the winning score in the scores List
# and then tries to announce the winner and score, but it isn't
# quite finished.  Add one line of code to resolve the problem.
winning_score = 0
winner = ''
for i in range(len(scores)):
    if (scores[i] > winning_score):
        winning_score = scores[i]
print '%s won with a score of %d.' % (winner, winning_score)

# The range() built-in function can also be passed two
# parameters.  In this mode, range(x, y) returns all consecutive
# Integers beginning with x (which is included) and ending just
# before y (which is excluded).  Note the similarity to the way
# sequence slices are specified.
# Review the console output produced by the following examples.
print 'range(3) returns %s' % range(3)
print 'range(5) returns %s' % range(5)
print 'range(0, 3) returns %s' % range(0, 3)
print 'range(1, 3) returns %s' % range(1, 3)
print 'range(2, 5) returns %s' % range(2, 5)

# Loops can of course be nested, just like conditional
# structures.  The following code sorts the elements of the
# scores list with higher scores appearing first.
# Study this code carefully to make certain that you understand
# how it works.
# Why did we have to pass 1 in the first parameter to range()?
# What would have happened if we hadn't set num_changes to 1
# at the very beginning?
# What would have happened if we hadn't set num_changes to 0
# at the beginning of the outer loop?
# What exactly do those three statements immediately before
# the incrementing of num_changes do?
# Why did we need the separate bigger_score variable to help?
num_changes = 1
while (num_changes > 0):
    num_changes = 0
    for i in range(1, len(scores)):
        if (scores[i] > scores[i-1]):
            bigger_score = scores[i]
            scores[i] = scores[i-1]
            scores[i-1] = bigger_score
            num_changes = num_changes + 1

# Add lines to the code above so that it also sorts the players
# List to match the sorted scores List.
