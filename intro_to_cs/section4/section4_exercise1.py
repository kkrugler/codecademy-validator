# So far we've only been using the formatting operator (%) to
# insert Strings into other Strings.  Even when we use it in the
# following way, it is still doing so.  This is because the
# Integer value in the Integer variable thirteen (13) has a
# String representation ("13").  Here we're telling the
# formatting operator to replace the String placeholder in the
# template with a String, but then we're handing it an Integer.
# It must therefore ask the Integer for its String
# representation, and use that to replace the String placeholder.

thirteen = 13
message = 'The variable thirteen has the value %s.' % thirteen
print message

# We've already seen that there are things you can do with
# Strings that cannot be done with Integers, such as return
# their lengths (where the length of a String is the number of
# characters it contains, including invisible characters like
# spaces).  The second statement below generates a TypeError,
# because the variable thirteen is not itself a String, and
# therefore has no length.
# Note that in this case Python does NOT automatically return
# the length of thirteen's String representation.

print 'The message variable has a length of %s.' % len(message)
#print 'The thirteen variable has a length of %s.' % len(thirteen)

# Click the Save & Submit button to see how Python complains
# about the statement above.  Read over the message in the
# console carefully, then "comment out" (only) the line above
# that caused the problem by inserting the comment character (#)
# immediately before the print keyword on that line.

# The first statement below creates a String variable named
# thirteen_string that is identical to the String representation
# of the variable thirteen.  Can you guess what the print
# statement that follows will send to the console?
# Since the variable thirteen_string is a String, Python will
# complain if you try to add it to an Integer.
# Can you guess which of the statements below will generate a
# TypeError?

thirteen_string = "13"
print 'thirteen_string has length %s.' % len(thirteen_string)
twenty_six = thirteen + thirteen
#twenty_six = thirteen_string + thirteen

# Again, click the Save & Submit button to see how Python
# complains about the code block above.  Read over the message in
# the console carefully.

# Next, try reversing the order of the two variables that the
# problem statement is trying to add, and then click the
# Save & Submit button again.

# If you read the console message carefully, you'll notice that
# it's a little different from the previous error message.
# Python has now assumed that the plus sign (+) is being used as
# the concatenation operator (rather than for addition).
# It can't know for sure which operation you intended, so it
# made a guess here (based on the type of the first variable
# you were trying to add), and got it wrong.
# Again, comment out the offending line by inserting a comment
# character at the beginning of that line.

# The formatting operator (%) presents an opportunity for more
# explicit Python style.  In addition to the String placeholder
# (%s), it also supports an Integer placeholder (%i).

# The formatting in the first statement below is almost identical
# to what was used to build the message String variable at the
# very top of this program. However, this time the formatting
# operator was told to replace the Integer placeholder (%i).
# The difference is very subtle, but important.
# Which of these two statements is going to run into trouble?

print 'The variable thirteen has the value %i.' % thirteen
print 'thirteen_string has the value %s.' % thirteen_string

# Click the Save & Submit button to see how Python complains
# about the code block above.  Read over the message in the
# console carefully.
# Also note that the console output produced by the first print
# statement in the block above is identical to the one produced
# by the first print statement in this program.
# Fix the problem print statement above by using the appropriate
# placeholder.

# Finally complete the print statements below so that each
# includes the value of the variable mentioned, but use the
# most appropriate formatting placeholder.

score = 10
gender = 'Female'

print 'I think scores less than %i are wimpy.' % 10
print '%s spiders are generally larger.' % gender
