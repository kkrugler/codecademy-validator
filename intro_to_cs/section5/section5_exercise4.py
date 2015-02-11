# The following variable is an instance of a String, which not
# only allows use to compute its length using the built-in
# len() function, but which also supports a number of built-in
# String "methods".
# DO NOT modify this assignment statement.

my_string = 'Do your homework!'

# As we saw in the text, the lower() String method returns a new
# String that contains the same text, but with each uppercase
# character converted to lowercase.
# DO NOT modify this print statement.

print my_string.lower()

# There is a similar method that converts all lowercase letters
# to uppercase, named upper().  Use upper() to send the
# same message to the console, but in ALL UPPERCASE.

print my_string.upper()

# There is also a startswith(prefix) method that returns True if
# the String itself begins with the prefix String that is passed
# in as a method parameter.  Otherwise, it returns False.
# For example, the following code sends "It does begin that way!"
# to the console.
# DO NOT modify this conditional structure.

if (my_string.startswith('Do your')):
    print 'It does begin that way!'
else:
    print 'You must have broken the code!'

# There is a similar method named endswith(suffix) that returns
# True if the String ends with the suffix parameter.  Modify the
# condition in the code below to check whether my_string ends
# with "homework" (and note that it doesn't):

if (my_string.endswith('homework')):
    print "Your code doesn't seem to be working properly."
else:
    print 'Your code might be working properly.'

# There is also a find(substring) method that returns the
# (0-based) index of the position in the String where the
# substring first appears, or -1 if it's not found in the String.
# For example, the first line below prints "3" to the console,
# and the second one prints "-1" to the console (because
# the first letter in my_string is an uppercase "D").
# DO NOT modify any of these five lines of code.

print my_string.find('your')
print my_string.find('do')
position_1 = my_string.find('work')
position_2 = my_string.find(' ')
position_3 = my_string.find('home ')

# Try to predict the value of the three position variables by
# changing the assignment to the associated prediction variables
# below.

position_1_prediction = 12
position_2_prediction = 2
position_3_prediction = -1

# There is also a replace(target, replacement) method that
# returns a new String that has every (non-overlapping) instance
# of the target parameter found in the String replaced by
# whatever you pass in the replacement parameter.
# For example, the first line below prints "It's cold in here.",
# the second one prints "It's hot in here.",
# the third one prints "It's  hot  in  here.", and
# the fourth one prints "Only two in XX".
# DO NOT modify any of these seven lines of code.

print "It's hot in here.".replace('hot', 'cold')
print "It's hot in here.".replace('cold', 'funky')
print "It's hot in here.".replace(' ', '  ')
print "Only two in aaaa".replace('aa', 'X')
string_1 = my_string.replace('your', 'my')
string_2 = my_string.replace('my', 'his')
string_3 = my_string.replace(' ', '-')

# Again, try to predict the value of the position variables by changing
# the assignment to the associated prediction variables below.

string_1_prediction = 'Do my homework!'
string_2_prediction = 'Do your homework!'
string_3_prediction = 'Do-your-homework!'

# Modify the following function definition so that whenever the
# input_text parameter contains the substring "Chris", the
# function returns a new String just like input_text, but with
# every instance of "OK" replaced with "awesome".  If input_text
# does not contain "Chris", then return input_text without any
# modifications.  As you can see, the function is currently
# written so that it always returns input_text as is.

def improve_chris_status(input_text):
    if (input_text.find('Chris') < 0):
        return input_text
    return input_text.replace('OK', 'awesome')

# Here's a function call you can also play around with to test
# your function definition.  However, note that whenever you
# click the Save & Submit button, the validation code will check
# its return value for many different cases.

print improve_chris_status('Chris is OK')
