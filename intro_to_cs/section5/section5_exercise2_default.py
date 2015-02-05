# Predict the value of each substring by changing the assignments
# to the prediction Strings following the code block below.
# DO NOT modify ANYTHING except for the assignments to the
# three prediction Strings.

my_string = 'One is the loneliest number.'
substring_1 = my_string[1]
substring_0_1 = my_string[0:1]
substring_0_2 = my_string[0:2]

substring_1_prediction = ''
substring_0_1_prediction = ''
substring_0_2_prediction = ''

# Note that you can use an Integer variable to specify the
# starting and/or ending position of your slice.  Again, predict
# the value of each substring that results.
# Again, DO NOT modify ANYTHING except for the assignments to the
# three prediction Strings.

start_pos = 4
end_pos = 6
substring_4 = my_string[start_pos]
substring_4_6 = my_string[start_pos:end_pos]
substring_6 = my_string[end_pos]

substring_4_prediction = ''
substring_4_6_prediction = ''
substring_6_prediction = ''

# As we've seen before, you can use Python's built-in len()
# function to return the length of a String, which is defined to
# be the number of characters in that String.
# You can use len() to help slice the end of a String, but note
# that (by definition) there is no character after the position
# returned by len(), because it refers to the position just
# AFTER the final character of the String.  Again, predict
# the value of each substring that results.
# Again, DO NOT modify ANYTHING except for the assignments to the
# three prediction Strings.

end_pos = len(my_string)
start_pos = end_pos - 1
substring_27_28 = my_string[start_pos:end_pos]
end_pos = start_pos
start_pos = end_pos - 6
substring_21_27 = my_string[start_pos:end_pos]
long_substring = my_string[0:len(my_string)]

substring_27_28_prediction = ''
substring_21_27_prediction = ''
long_substring_prediction = ''

# Slicing syntax also allows you to omit either the start or the
# end position (as long as you still include the colon).
# Again, predict the value of each substring that results.
# Again, DO NOT modify ANYTHING except for the assignments to the
# three prediction Strings.

substring_to_6 = my_string[:6]
substring_from_11 = my_string[11:]
substring_colon = my_string[:]

substring_to_6_prediction = ''
substring_from_11_prediction = ''
substring_colon_prediction = ''

# In addition to single-character Strings, you can even create
# an empty String.  Predict the length of the empty String by
# changing the assignment to len_15_15_prediction below.
# Also predict whether the empty String is equal to the None
# literal by changing the assignment to
# is_equal_to_none_prediction below (if necessary).
# Again, DO NOT modify ANYTHING except for the assignments to the
# two prediction variables.

substring_15_15 = my_string[15:15]
len_15_15 = len(substring_15_15)
is_equal_to_none = False
if (substring_15_15 == None):
    is_equal_to_none = True

len_15_15_prediction = 15
is_equal_to_none_prediction = True

# Finally, it's easy to make a mistake when indexing arrays.
# Try to predict which of the following statements will
# generate an IndexError if you remove the comment character (#)
# from the beginning of its line:

len_pos = len(my_string)
#print my_string[len_pos]
#print my_string[len_pos:len_pos]
#print my_string[len_pos:(len_pos+1)]
#print my_string[(len_pos+1):(len_pos+1)]
#print my_string[(len_pos+1):len_pos]

# Once you've made your prediction, remove the comment characters
# from the other four lines above, click the Save & Submit
# button, and see if you guessed correctly.
