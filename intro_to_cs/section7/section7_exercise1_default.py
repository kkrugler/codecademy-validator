# This function raises 10 to its exponent parameter and describes
# the result of doing so.  It does this by repeatedly multiplying
# 10 by itself exponent times.
def describe_10_raised_to(exponent):
    if (exponent < 0):
        return "I don't do negative exponents!"
    result = 1
    exponent_left = exponent
    while (exponent_left > 0):
        result = result * 10
        exponent_left = exponent_left - 1
    template = '10 raised to the %d power is %d.'
    return template % (exponent, result)

# Here are some examples of calling the function with various
# natural numbers.  Click the Save & Submit Code button and then
# review the console output produced.
print describe_10_raised_to(1)
print describe_10_raised_to(2)
print describe_10_raised_to(3)
print describe_10_raised_to(4)
print describe_10_raised_to(0) # Yes, that is the correct answer.

# Modify the following function so that it returns 2 raised to
# its exponent parameter, via a method similar to the one used
# by the describe_10_raised_to() function above.  However,
# return the actual power of 2, rather than a String describing
# it as was done by describe_10_raised_to().  Don't worry about
# getting called with invalid parameter values.
def raise_2_to(exponent):
    return 0

# You can use the following code to test your raise_2_to()
# function definition above.  Just modify the assignment to
# exponent below to pass whatever number you like in that
# parameter and then check the console window for the result.
exponent = 3
template = "raise_2_to(%d) returned %d."
print template % (exponent, raise_2_to(exponent))

# When you're pretty sure that your raise_2_to() function
# definition is working properly, set exponent to 31 above to
# let the SCT test it for you.

# This function describes the power of 10 that its natural_number
# parameter meets or exceeds.  In other words, it describes the
# approximate base 10 logarithm of natural_number.
# It does so by repeatedly dividing that number by 10 until it
# reaches zero, and counting the number of such divisions.
def log_base_10_description(natural_number):
    if (natural_number < 1):
        return '%d does not compute!' % natural_number
    power_of_10 = -1
    number = natural_number
    while (number > 0):
        number = number / 10
        power_of_10 = power_of_10 + 1
    template = '%d is at least 10 raised to the %d power.'
    return template % (natural_number, power_of_10)

# Here are some examples of calling the function with various
# natural numbers.  Check the console output to see the results.
#
# Note how this and subsequent console output was skipped until
# you set exponent to 31 to let the SCT test your raise_2_to()
# function above.
if (exponent == 31):
    print log_base_10_description(1)
    print log_base_10_description(10)
    print log_base_10_description(100)
    print log_base_10_description(1000)
    print log_base_10_description(5 * 1000 * 1000)

# Here are two examples for which the logarithm function is
# undefined.
if (exponent == 31):
    print log_base_10_description(0)
    print log_base_10_description(-10)

# Modify the following function so that it returns the exponent
# of the power of 2 that its natural_number parameter meets or
# exceeds.  Return the actual exponent of 2, rather than a String
# describing it as was done by log_base_10_description().
# Don't worry about getting called with invalid parameter values.
def log_base_2(natural_number):
    return 0

# You can use the following code to test your log_base_2()
# function definition above.  Just modify the assignment to
# natural_number below to pass whatever number you like in that
# parameter and then check the console window for the result.
natural_number = 8
template = "log_base_2(%d) returned %d."
if (exponent == 31):
    print template % (natural_number, log_base_2(natural_number))

# When you're pretty sure that your log_base_2() function
# definition is working properly, set natural_number to 65536
# above to let the SCT test it for you.
