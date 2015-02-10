# None of the following variables are Strings, but each has a
# string representation.  DO NOT modify any of these assignments.

my_int = 42
my_float = 42.0
is_yes = True

# Change the following three assignments so that each variable
# now contains the string representation of the variable it is
# associated with above.  Use both the associated variable and
# the String constructor in each assignment statement below,
# then click the Save & Submit button to check your code.

my_int_as_string = str(my_int)
my_float_as_string = str(my_float)
is_yes_as_string = str(is_yes)

# The following three print statements use those representations
# in a way that wouldn't work with the original variables.
# DO NOT modify these print statements at all.

print 'my_int looks like ' + my_int_as_string
print 'my_float looks like ' + my_float_as_string
print 'is_yes looks like ' + is_yes_as_string

# Write three more print statements to send the same three lines
# to the console again.  However, construct the string
# representations directly from the original variables this time,
# instead of using the three _as_string variables you assigned
# above.

print 'my_int looks like ' + str(my_int)
print 'my_float looks like ' + str(my_float)
print 'is_yes looks like ' + str(is_yes)
