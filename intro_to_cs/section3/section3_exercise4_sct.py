import re

printed_lines = CC.prints()

def check_text(expected, actual, desc, last_char_desc=None):
    if (type(actual) != str):
        return '''Your %s is not even a String.''' % desc
    if  (   (last_char_desc)
        and (actual == expected[:-1])):
        return '''It looks like you forgot the %s at the end of your %s.''' % (last_char_desc, desc)
    if (actual.find('  ') > 0):
        return '''Your %s contains two spaces in a row.
Check its construction over carefully to avoid this problem.''' % desc
    if (actual.startswith(' ')):
        return '''Your %s starts with a space.
Check its construction over carefully to avoid this problem.''' % desc
    if (actual.endswith(' ')):
        return '''Your %s ends with a space.
Check its construction over carefully to avoid this problem.''' % desc
    case_warning = ''
    if (actual.lower() == expected.lower()):
        case_warning = ''' The difference is only a question of uppercase vs. lowercase,
so check your text over carefully.'''

    # Although the following error message is not always grammatically
    # correct (since the first sentence doesn't end in a period),
    # that period was confusing students, who assumed it was part
    # of the expected string.
    if (actual != expected):
        return '''Your %s was "%s" instead of "%s"%s''' % (desc, actual, expected, case_warning)
    return True

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (first_value < 100):
    return '''Try out all cases for biggest_value()'s two input
parameters by setting first_value & second_value, clicking the
Save & Submit Code button, and reviewing the console output.
Once you're finished testing, set first_value to 100 and then
click the Save & Submit Code button again to move on to testing
the smallest_value() function.'''

if (len(printed_lines) < 5):
    return '''It looks like you modified the code outside the
smallest_value() function definition so that it no longer tests
the function as intended. Click the Reset Code button,
and start over.'''

result = check_text('0',
                    printed_lines[1],
                    'result for the first test of smallest_value()')
if (result != True):
    return result

result = check_text('0',
                    printed_lines[2],
                    'result for the second test of smallest_value()')
if (result != True):
    return result

result = check_text('1',
                    printed_lines[3],
                    'result for the third test of smallest_value()')
if (result != True):
    return result

result = check_text('-4',
                    printed_lines[4],
                    'result for the fourth test of smallest_value()')
if (result != True):
    return result


if (bob_score < 100):
    if (len(printed_lines) < 6):
        return '''No lines were printed to the console.
It looks like you must have changed the code that prints the
result of calling get_announcement(). Click the Reset Code button,
and start over being careful to change only the function definition
of get_announcement() and the lines that assign the input scores.'''
    if  (   (bob_score == 0)
        and (jane_score == 0)
        and (sally_score == 0)):
        return '''Your smallest_value() function seems to be working
properly. Now modify the function definition of get_announcement()
as requested and test it to make sure it works properly when you
set various combinations of player scores via the assignment
statements that precede the function definition.'''
    return '''Continue to test your get_announcement() function
to make sure it works properly (check its console output)
when you set various combinations of player scores via the assignment
statements that precede the function definition. Once you're ready
for the SCT to test all cases, just assign bob_score to 100 and
then click the Save & Submit button.'''

def check_result(result, is_bob_winner, is_jane_winner, is_sally_winner):
    if (result == None):
        return False
    result_lower = result.lower().strip()
    is_tie = ((is_bob_winner + is_jane_winner + is_sally_winner) > 1)
    return  (   (is_bob_winner == (result_lower.find('bob') >= 0))
            and (is_jane_winner == (result_lower.find('jane') >= 0))
            and (is_sally_winner == (result_lower.find('sally') >= 0))
            and (is_tie == (result_lower.find('tie') >= 0))
            and (is_tie == (result_lower.find('won') < 0)))

def check_winner(bob_score_test, jane_score_test, sally_score_test):
    result = get_announcement(bob_score_test, jane_score_test, sally_score_test)
    if (bob_score_test > jane_score_test):
        if (bob_score_test > sally_score_test):
            if check_result(result, True, False, False): return True
        elif (sally_score_test > bob_score_test):
            if check_result(result, False, False, True): return True
        else:
            if check_result(result, True, False, True): return True
    elif (jane_score_test > sally_score_test):
        if (jane_score_test > bob_score_test):
            if check_result(result, False, True, False): return True
        elif (bob_score_test > jane_score_test):
            if check_result(result, True, False, False): return True
        else:
            if check_result(result, True, True, False): return True
    elif (sally_score_test > bob_score_test):
        if (sally_score_test > jane_score_test):
            if check_result(result, False, False, True): return True
        elif (jane_score_test > sally_score_test):
            if check_result(result, False, True, False): return True
        else:
            if check_result(result, False, True, True): return True
    else:
            if check_result(result, True, True, True): return True
    return result

for bob_score_test in range (0, 3):
    for jane_score_test in range (0, 3):
        for sally_score_test in range (0, 3):
            result = check_winner(bob_score_test, jane_score_test, sally_score_test)
            if (result == None):
                return '''Your code returns nothing at all when
bob_score is %d, jane_score is %d, and sally_score is %d.
Make sure that you aren't trying to print the announcment in
get_announcement(), but are just returning it. Also, make sure
that the only way out of get_announcement() is via a return
statement that returns an announcement String.''' % (bob_score_test, jane_score_test, sally_score_test)
            elif (result != True):
                return '''Your code returns "%s" when
bob_score is %d, jane_score is %d, and sally_score is %d.''' % (result, bob_score_test, jane_score_test, sally_score_test)

return True
