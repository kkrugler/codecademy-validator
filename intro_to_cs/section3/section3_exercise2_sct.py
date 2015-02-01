import re

printed_lines = CC.prints()

def check_text(expected, actual, desc, last_char_desc=None):
    if (type(actual) != str):
        return '''Your %s is not even a String.''' % desc
    if  (   (last_char_desc)
        and (actual == expected[:-1])):
        return '''It looks like you forgot the %s at the end of your %s.''' % (last_char_desc, desc)
    case_warning = ''
    if (actual.lower() == expected.lower()):
        case_warning = ''' The difference is only a question of uppercase vs. lowercase,
so check your text over carefully.'''
    if (actual != expected):
        return '''Your %s was "%s" instead of "%s".%s''' % (desc, actual, expected, case_warning)
    return True

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

code_lines = code.splitlines()
bob_score_prediction_line_numbers = list()
bob_score_init_re = re.compile(r'^bob_score[ \t]*=[ \t]*\d+[ \t]*$')
last_bob_score_init_line_number = 0
num_student_ifs = 0
student_if_line_number = 0
num_student_elifs = 0
student_elif_line_number = 0
num_student_elses = 0
student_else_line_number = 0
line_number = 0
for line in code_lines:
    line_number += 1
    if (line.startswith('bob_score_prediction_')):
        bob_score_prediction_line_numbers.append(line_number)
    elif (bob_score_init_re.match(line)):
        last_bob_score_init_line_number = line_number

    if (len(bob_score_prediction_line_numbers) > 3):
        if (line.startswith('if')):
            num_student_ifs += 1
            student_if_line_number = line_number
        elif (line.startswith('elif')):
            num_student_elifs += 1
            student_elif_line_number = line_number
        elif (line.startswith('else')):
            num_student_elses += 1
            student_else_line_number = line_number

line_number = bob_score_prediction_line_numbers[0]
if  (   (bob_score_prediction_1 != 0)
    or  (jane_score_prediction_1 != 1)
    or  (sally_score_prediction_1 != 1)):
    return '''One of the predicted scores in your first set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)

line_number = bob_score_prediction_line_numbers[1]
if  (   (bob_score_prediction_2 != 0)
    or  (jane_score_prediction_2 != 4)
    or  (sally_score_prediction_2 != 1)):
    return '''One of the predicted scores in your second set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)

line_number = bob_score_prediction_line_numbers[2]
if  (   (bob_score_prediction_3 != 1)
    or  (jane_score_prediction_3 != 5)
    or  (sally_score_prediction_3 != 2)):
    return '''One of the predicted scores in your third set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)

line_number = bob_score_prediction_line_numbers[3]
if  (   (bob_score_prediction_4 != 3)
    or  (jane_score_prediction_4 != 5)
    or  (sally_score_prediction_4 != 2)):
    return '''One of the predicted scores in your fourth set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)


if (len(printed_lines) < 1):
    return '''No lines were printed to the console.
Your program still needs to announce the winner.'''


if (num_student_ifs == 0):
    return '''It doesn't seem like you use an if/elif/else structure
to announce your winner.  Your code should be designed to announce
the correct winner no matter which player wins.'''

if (num_student_ifs > 1):
    return '''It looks like you have more than one "if" structure
in your annoucement code. Try to announce the correct winner using
a single if/elif/else structure. Note that it should announce only
one winner, even if two players have at least 5 points.'''

if (num_student_elifs == 0):
    return '''It doesn't seem like you have an elif condition in
your if/elif/else structure. Your code should be designed to announce
the correct winner no matter which player wins.'''

if (num_student_elses == 0):
    if (num_student_elifs > 1):
        return '''It doesn't seem like you have an else clause in
your if/elif/else structure. If you've already tested each case
separately by fudging the scores (and it seems to work),
then your code could probably be simplified by converting your
final elif condition on line %d into an else
clause.''' % student_elif_line_number
    else:
        return '''It doesn't seem like you have an else clause in
your if/elif/else structure. Your code should be designed to announce
the correct winner no matter which player wins.'''

line_number = last_bob_score_init_line_number
if (last_bob_score_init_line_number > bob_score_prediction_line_numbers[3]):
    return '''Check to make sure your program is printing the
correct winner no matter what you set the scores to on
lines %d to %d.  Once you're finished testing, remove those lines
and then click the Save & Submit Code button again to have it
announce the real winner.''' % (line_number, line_number + 2)


result = check_text('Jane Won!',
                    printed_lines[0],
                    'printed line',
                    'exclamation point')
if (result != True):
    return result

return True
