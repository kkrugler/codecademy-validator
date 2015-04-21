# The following function returns a String that warns students
# about an activity that is either always prohibited, or perhaps
# prohibited just during a specific time period (i.e., if the
# caller specifies a value for the optional when parameter).
#
# DO NOT modify the code in the function definition, except for
# the specific changes to its SIGNATURE that are requested later
# in this exercise.
def warn(activity='texting', location='on campus', when=None):
    if (when == None):
        when_part = ''
    else:
        when_part = ' %s' % when
    inserted = (activity, location, when_part)
    return 'Note that %s is prohibited %s%s!' % inserted

# The first warning is about texting.  Note that the optional
# when parameter is not specified.
warn_1 = warn()

# Predict the value of the warn_1 variable at this point in
# the program by setting warn_1_prediction to a String literal.
warn_1_prediction = 'Note that texting is prohibited on campus!'

# The second warning is more general.  Note that the optional
# when parameter is still not specified.
warn_2 = warn('all cell phone usage')

# Predict the value of the warn_2 variable at this point in the
# program by setting warn_2_prediction to a String literal.
warn_2_prediction = 'Note that all cell phone usage is prohibited on campus!'

# The third warning is about a different activity and location,
# but the optional when parameter is still not specified.
warn_3 = warn('skateboarding', 'in the computer lab')

# Predict the value of the warn_3 variable at this point in the
# program by setting warn_3_prediction to a String literal.
warn_3_prediction = 'Note that skateboarding is prohibited in the computer lab!'

# The fourth warning is about a different activity and location,
# but the default value of the when parameter is "overridden".
warn_4 = warn('PDA', 'on campus', 'while teachers are looking')

# Predict the value of the warn_4 variable at this point in the
# program by setting warn_4_prediction to a String literal.
warn_4_prediction = 'Note that PDA is prohibited on campus while teachers are looking!'

# Refer to the Instructions section to the left for additional
# directions.
