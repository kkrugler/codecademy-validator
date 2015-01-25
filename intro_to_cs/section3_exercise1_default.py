# This program is designed to count the number of conditions
# that it finds to be true, as well as the number of lines of
# text it displays in the console.  It does so by adding one to
# the current value of the variable true_condition_count
# (also known as "incrementing" the variable) after each true
# condition.  It also increments printed_line_count after
# sending each line of text to the console.
#
# Read over the code carefully, then make predictions by setting
# the values of the two variables at the end of the program.

true_condition_count = 0
printed_line_count = 0

if (3 > 4):
    true_condition_count = true_condition_count + 1
    print 'Are you sure Python understands arithmetic?'
    printed_line_count = printed_line_count + 1
print 'Python understands arithmetic.'
printed_line_count = printed_line_count + 1
if (4 > 3):
    true_condition_count = true_condition_count + 1
    print 'Here is a little proof.'
    printed_line_count = printed_line_count + 1

age = 20
if (age > 20):
    true_condition_count = true_condition_count + 1
    print 'I thought you were only 20!'
    printed_line_count = printed_line_count + 1
if (age < 20):
    true_condition_count = true_condition_count + 1
    print 'I thought you had already reached 20!'
    printed_line_count = printed_line_count + 1
if (age == 20):
    true_condition_count = true_condition_count + 1
    print 'That condition looks a little strange to me.'
    printed_line_count = printed_line_count + 1
    age = age + 1
print 'Anybody hungry?'
printed_line_count = printed_line_count + 1

if (age > 20):
    true_condition_count = true_condition_count + 1
    print 'Happy birthday!'
    print 'Now get a job, already.'
    printed_line_count = printed_line_count + 2
print 'I have a job.'
printed_line_count = printed_line_count + 1

# Replace the zero in each assignment statement below with your
# prediction for the value of the counter it refers to at this
# point in the program.

true_condition_count_prediction = 0
printed_line_count_prediction = 0
