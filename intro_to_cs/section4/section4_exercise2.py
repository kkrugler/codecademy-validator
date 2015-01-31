# Try to predict the result of the following Integer division.

quotient = 10 / 3
remainder = 10 % 3

# Set the following two variables to your predicted values for
# quotient and remainder above.

quotient_prediction = 3
remainder_prediction = 1

# Now use the division operator to assign the variable
# third_of_ten below to 10 divided by 3, but make sure that
# third_of_ten becomes a float instead of an int so that it
# includes the fractional part.

third_of_ten = 10.0 / 3

# As you might have predicted, there is also a special
# placeholder (%f) you can use with the formatting operator
# to embed a float in a String.  Here there are real advantages
# over the String placeholder (%s), because you can further
# qualify the number of decimal places to include, etc.

print 'One third of ten is roughly %s!' % third_of_ten
print 'One third of ten is roughly %f!' % third_of_ten
print 'One third of ten is roughly %.2f!' % third_of_ten

# Note that the formatting placeholder actually rounds the float
# in order to produce the String to insert into the template.

print 'Two thirds of ten is roughly %.2f!' % (third_of_ten * 2)
print 'Two thirds of ten is roughly %.0f!' % (third_of_ten * 2)

# Check the console output from the five print statements above,
# then modify the following print statement so that it prints
# out the value in third_of_ten, but rounds it to the nearest
# thousandth.

print 'One third of ten is roughly %.3f!' % third_of_ten
