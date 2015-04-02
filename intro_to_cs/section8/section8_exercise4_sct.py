import re

printed_lines = CC.prints()

if (error):
    if  (   (len(printed_lines) > 9)
        and printed_lines[9].startswith('Considering [None')):
        return """Next, modify the announce_leader() function
so that it "guards" is_best() against scores that are None,
as directed."""
    else:
        return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) < 6):
    return '''It looks like you modified the code in such a way
that it no longer sends all of the output to the console that
it is supposed to. Click the Reset Code button, and start over.'''

code_lines = code.splitlines()
line_number = 0
is_in_is_winner = False
is_in_is_mediocre = False
is_in_encourage_chris = False
is_in_function_6 = False
is_mediocre_modified = True
is_encourage_chris_modified = True
is_function_6_modified = True
num_encourage_chris_nots = 0
num_encourage_chris_ifs = 0
num_function_6_nots = 0
for line in code_lines:
    line_number += 1

    if (line.startswith('def is_winner(')):
        is_in_is_winner = True
    elif (line.startswith('def is_mediocre(')):
        is_in_is_mediocre = True
    elif (line.startswith('def encourage_chris(')):
        is_in_encourage_chris = True
    elif (line.startswith('def function_6(')):
        is_in_function_6 = True
    elif (not line.startswith(' ')):
        is_in_is_winner = False
        is_in_is_mediocre = False
        is_in_encourage_chris = False
        is_in_function_6 = False

    if (is_in_is_winner):
        if (line.strip() == 'return (not (score < 10))'):
            return '''Simplify the is_winner() function definition,
as directed.'''
        elif (line.find('not') > 0):
            return '''Your is_winner() function definition
should not require the use of the not operator on line %d''' % line_number
        elif (line.find('if') > 0):
            return '''Your is_winner() function definition
should not require the use of the if statement on line %d''' % line_number

    if (is_in_is_mediocre):
        if (line.strip() == "return (not (name.lower() == 'chris'))"):
            is_mediocre_modified = False
        elif (line.find('not') > 0):
            return '''Your is_mediocre() function definition
should not require the use of the not operator on line %d''' % line_number
        elif (line.find('if') > 0):
            return '''Your is_mediocre() function definition
should not require the use of the if statement on line %d''' % line_number

    if (is_in_encourage_chris):
        if (line.strip() == "if (not (is_winner(score)) and (not (is_mediocre(name)))):"):
            is_encourage_chris_modified = False
        num_encourage_chris_nots += line.count('not')
        num_encourage_chris_ifs += line.count('if ')
        if (line.find('elif') > 0):
            return '''Your encourage_chris() function definition
should not require the use of the elif clause on line %d''' % line_number

    if (is_in_function_6):
        if (line.strip().find('if ') > 0):
            return '''Your function_6() function definition
should not require the use of the if statement on line %d''' % line_number
        if (line.strip() == "return False"):
            is_function_6_modified = False
        if (line.find('function_5') > 0):
            return '''You cheated on line %d! No fair calling
function_5() from your function_6() definition.''' % line_number
        num_function_6_nots += line.count('not')

if (score_1 == 100):
    for test_score in [-10, -1, 0, 1, 9, 9.5, 10, 11]:
        result = is_winner(test_score)
        if (result != (test_score >= 10)):
            return 'Your is_winner(%s) returned %s.' % (test_score, result)
else:
    return '''Test your is_winner() modifications by assigning
score_1 to various numbers and then checking the output in the
console window, as directed.  See the instructions for what to
do when you think it's working properly.'''

if (not is_mediocre_modified):
    return '''Next, simplify the is_mediocre() function
definition, as directed.'''
elif (name_1 == 'Carol'):
    for test_name in ['Bob', 'Chris', 'CHRIS', 'Christine', 'christine']:
        result = is_mediocre(test_name)
        if (result != (test_name.lower() != 'chris')):
            return 'Your is_mediocre(%s) returned %s.' % (test_name, result)
else:
    return '''Test your is_mediocre() modifications by assigning
name_1 to various Strings and then checking the output in the
console window, as directed.  See the instructions for what to
do when you think it's working properly.'''

if (not is_encourage_chris_modified):
    return '''Next, simplify the encourage_chris() function
definition, as directed.'''
elif (num_encourage_chris_nots > 0):
    return '''Your encourage_chris() function shouldn't include
any not operators.'''
elif (num_encourage_chris_ifs > 1):
    return '''Your encourage_chris() function should include
only one if statement.'''
elif    (   (name_2 == 'Carol')
        and (score_2 == 100)):
    for test_name in ['Bob', 'Chris', 'CHRIS', 'Christine', 'christine']:
        for test_score in [-10, -1, 0, 1, 9, 9.5, 10, 11]:
            result = encourage_chris(test_name, test_score)
            if (is_winner(test_score) or is_mediocre(test_name)):
                expected_result = '%s scored %d.' % (test_name, test_score)
            else:
                expected_result = 'Hang in there, Chris!'
            if (result != expected_result):
                return 'Your encourage_chris(%s, %d) returned "%s".' % (test_name, test_score, result)
else:
    return '''Test your encourage_chris() modifications by
assigning name_2 to various Strings and score_2 to various numbers,
then checking the output in the console window, as directed.
See the instructions for what to do when you think it's
working properly.'''

if (not is_function_6_modified):
    return '''Finally, modify the function_6() function
definition so that it always returns the same thing as
function_5(), but only uses a single not operator, as directed.'''
if (num_function_6_nots > 1):
    return '''Your function_6() function should include only a
single not operator.'''
for a in [False, True]:
    for b in [False, True]:
        for c in [False, True]:
            for d in [False, True]:
                result = function_6(a, b, c, d)
                if (result != function_5(a, b, c, d)):
                    return 'Your function_6(%s, %s, %s, %s) returned %s' % (a, b, c, d, result)

return True
