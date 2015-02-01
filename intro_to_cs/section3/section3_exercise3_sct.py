import re

printed_lines = CC.prints()

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
line_number = 0
for line in code_lines:
    line_number += 1
    if (line.startswith('bob_score_prediction_')):
        bob_score_prediction_line_numbers.append(line_number)
    elif (bob_score_init_re.match(line)):
        last_bob_score_init_line_number = line_number

    if (len(bob_score_prediction_line_numbers) > 3):
        if  (   (   (line.startswith('if'))
                and (not line.startswith('if (bob_score > jane_score):')))
            or  (   (line.startswith('elif'))
                and (not line.startswith('elif (jane_score > sally_score):'))
                and (not line.startswith('elif (sally_score > bob_score):')))
            or  (   (line.startswith('else'))
                and (not line.startswith('else:')))):
            return '''It looks like you modified line %d.
Write down your three sets of predictions, click the Reset Code
button, and start over.  Please be careful next time to leave the
outer conditional structure unchanged and just add nested conditional
structures within its if and elif clauses.''' % line_number

line_number = bob_score_prediction_line_numbers[0]
if  (   (bob_score_prediction_1 != 1)
    or  (jane_score_prediction_1 != 1)
    or  (sally_score_prediction_1 != 0)):
    return '''One of the predicted scores in your first set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)

line_number = bob_score_prediction_line_numbers[1]
if  (   (bob_score_prediction_2 != 2)
    or  (jane_score_prediction_2 != 2)
    or  (sally_score_prediction_2 != 0)):
    return '''One of the predicted scores in your second set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)

line_number = bob_score_prediction_line_numbers[2]
if  (   (bob_score_prediction_3 != 4)
    or  (jane_score_prediction_3 != 2)
    or  (sally_score_prediction_3 != 1)):
    return '''One of the predicted scores in your third set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)

line_number = bob_score_prediction_line_numbers[3]
if  (   (bob_score_prediction_4 != 5)
    or  (jane_score_prediction_4 != 3)
    or  (sally_score_prediction_4 != 5)):
    return '''One of the predicted scores in your fourth set
(lines %d to %d) was wrong.''' % (line_number, line_number + 2)


if (len(printed_lines) < 1):
    return '''No lines were printed to the console.
Your program still needs to announce the winner.'''

line_number = last_bob_score_init_line_number
if (last_bob_score_init_line_number > bob_score_prediction_line_numbers[3]):
    return '''Modify the winner announcement code as directed,
then begin testing it. Make sure your program is printing the
correct winner no matter what you set the scores to on
lines %d to %d.  Once you're finished testing, remove those lines
and then click the Save & Submit Code button again to have it
announce the real winner.''' % (line_number, line_number + 2)

printed_lower = printed_lines[0].lower().strip()
if (printed_lower.find('jane') >= 0):
    return '''Jane did not win.'''

if (printed_lower.find('bob') < 0):
    return '''What about Bob?'''

if (printed_lower.find('sally') < 0):
    return '''What about Sally?'''

if  (   (printed_lower.find('won') >= 0)
    or  (printed_lower.find('tie') < 0)):
    return '''It was actually a tie.'''

return True
