first_name = 'Kenneth'
middle_initial = 'W'
last_name = 'Krugler'

# The following assignment statement doesn't quite accomplish
# what was obviously intended.

formal_name = first_name + ' ' + middle_initial + '. ' + last_name

# Can you guess what the following print statement will send to
# the console?  Modify the assignment statement above to fix the
# problem.

print 'His formal name is ' + formal_name

# Compare the color used by the code window to draw the variable
# names above vs. the color it uses to draw the text in the print
# statement below (including both instances of formal_name).
# This print statement just sends the text to the console exactly
# as it appears below.  Modify this statement so that it uses
# concatenation to generate the output that was obviously
# intended, but don't forget the period at the end.

print 'The variable formal_name contains ' + formal_name + '.'
