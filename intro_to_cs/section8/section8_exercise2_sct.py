import re

printed_lines = CC.prints()

def check_text(expected, actual, desc, is_describe_expected=True):
    last_char_desc = None
    if (type(actual) != str):
        return '''Your %s is not even a String.''' % desc
    if (expected[-1] == '.'):
        last_char_desc = 'period'
    elif (expected[-1] == '!'):
        last_char_desc = 'exclamation point'
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

    if (actual == expected):
        return True

    # Although the following error message is not always grammatically
    # correct (since the first sentence doesn't end in a period),
    # that period was confusing students, who assumed it was part
    # of the expected string.
    if (is_describe_expected):
        return '''Your %s was "%s" instead of "%s"%s''' % (desc, actual, expected, case_warning)
    return '''Your %s was incorrect.''' % desc

def check_prediction(expected, name, line, prediction_pattern, no_match_msg, section=None):
    actual = globals().get(name)
    if (not (name in globals())):
        return '''You seem to have modified the program somehow so that
it no longer assigns %s to anything.
Click the Reset Code button and start over.''' % name
    assignment_re = re.compile(r'^([^ \t=]+)[ \t]*=([^=].*)?$')
    assignment_match = assignment_re.match(line)
    if  (   (assignment_match)
        and (assignment_match.groups()[0] == name)):
        prediction_re = re.compile(prediction_pattern)
        if (not prediction_re.match(line)):
            return no_match_msg
        if (type(expected) == str):
            return check_text(expected, actual, name, False)
        if (expected != actual):
            if (section):
                return '''One of the predictions in your %s set
was incorrect.''' % section
            else:
                return '''Your %s was not correct.''' % name
    return True

def check_bool_prediction(expected, name, line, section=None):
    no_match_msg = '''You must assign %s to a single Boolean literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(True|False)[ \t]*(#.*)?$',
                            no_match_msg,
                            section)

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) > 0):
    return '''You should be ashamed of yourself!  It looks like
you modified the code so that it sends an unexpected line to the
console.  You're not going to learn much about Boolean operators
if you continue CHEATING.  Instead, please try to execute the
code in your head.'''

code_lines = code.splitlines()
line_number = 0
is_in_not_test_defs = False
num_nots_remaining = 0
is_in_is_clear_winner_def = False
num_is_clear_winner_ifs = 0
for line in code_lines:
    line_number += 1

    result = check_bool_prediction(False,
                                   'and_result_1_prediction',
                                   line,
                                   'first')
    if (result != True):
        return result
    result = check_bool_prediction(True,
                                   'and_result_2_prediction',
                                   line,
                                   'first')
    if (result != True):
        return result
    result = check_bool_prediction(False,
                                   'and_result_3_prediction',
                                   line,
                                   'first')
    if (result != True):
        return result
    result = check_bool_prediction(False,
                                   'and_result_4_prediction',
                                   line,
                                   'first')
    if (result != True):
        return result

    if  (   or_result_1_prediction
        or  or_result_2_prediction
        or  or_result_3_prediction
        or  or_result_4_prediction):
        result = check_bool_prediction(True,
                                       'or_result_1_prediction',
                                       line,
                                       'second')
        if (result != True):
            return result
        result = check_bool_prediction(True,
                                       'or_result_2_prediction',
                                       line,
                                       'second')
        if (result != True):
            return result
        result = check_bool_prediction(True,
                                       'or_result_3_prediction',
                                       line,
                                       'second')
        if (result != True):
            return result
        result = check_bool_prediction(False,
                                       'or_result_4_prediction',
                                       line,
                                       'second')
        if (result != True):
            return result

    if (line.startswith('def is_not')):
        is_in_not_test_defs = True
    elif (line.startswith('def is_clear')):
        is_in_not_test_defs = False
        is_in_is_clear_winner_def = True
    elif (is_in_not_test_defs):
        statement = line[:line.find('#')]
        if (statement.find('not') > 0):
            num_nots_remaining += 1
        if (statement.find('and') > 0):
            return '''Your function definition uses the and
operator on line %d, but you can simplify it so that it uses
none of the Boolean operators.''' % line_number
        if (statement.find('or') > 0):
            return '''Your function definition uses the or
operator on line %d, but you can simplify it so that it uses
none of the Boolean operators.''' % line_number
    elif (is_in_is_clear_winner_def):
        statement = line[:line.find('#')]
        if (statement.find('elif') > 0):
            return '''Your function definition includes an elif
clause on line %d, but you can simplify it so that it contains
no elif or else clauses.''' % line_number
        elif (statement.find('else') > 0):
            return '''Your function definition includes an else
clause on line %d, but you can simplify it so that it contains
no elif or else clauses.''' % line_number
        elif (statement.find('if') > 0):
            num_is_clear_winner_ifs += 1

if  (   (not or_result_1_prediction)
    and (not or_result_2_prediction)
    and (not or_result_3_prediction)
    and (not or_result_4_prediction)):
    return '''Next, predict the values of the or expressions,
as directed.'''

if (num_nots_remaining == 4):
    return '''Next, modify the four is_not...() function
definitions so that each still returns the same value for every
input number, but without using the not operator, as directed.'''

if (num_is_clear_winner_ifs == 3):
    return '''Finally, modify the is_clear_winner() function
definition so that it still returns the same value for every
pair of input numbers, but uses only a single conditional
structure to do so, as directed.'''

def check_bool(expected, actual, desc):
    result = check_text(str(expected), str(actual), desc, True)
    if (result == True):
        return result
    result = result.replace('"True"', 'True')
    return result.replace('"False"', 'False')

for number in (-1, 0, 1, 2, 3, 3.5, 4, 5):
    result = check_bool((number >= 4),
                        is_not_less_than_four(number),
                        'is_not_less_than_four(%s) result' % number)
    if (result != True):
        return result
for number in (-1, 0, 6, 7, 8):
    result = check_bool((number != 7),
                        is_not_equal_to_seven(number),
                        'is_not_equal_to_seven(%s) result' % number)
    if (result != True):
        return result
for number in (-1, 0, 41, 42, 43):
    result = check_bool((number == 42),
                        is_not_different_from_42(number),
                        'is_not_different_from_42(%s) result' % number)
    if (result != True):
        return result
for number in (-1, 0, 1, 2, 3, 4.5, 5, 6):
    result = check_bool((number < 5),
                        is_not_greater_than_or_equal_to_five(number),
                        'is_not_greater_than_or_equal_to_five(%s) result' % number)
    if (result != True):
        return result

if (num_nots_remaining > 0):
    return '''At least one of the four is_not...() functions
still uses the not operator.'''

for score in range(-1, 7):
    for other_score in range(-1, 7):
        result = check_bool((   (score >= 5)
                            and (score > other_score)),
                            is_clear_winner(score, other_score),
                            'is_clear_winner(%s, %s) result' % (score, other_score))
        if (result != True):
            return result

if (num_is_clear_winner_ifs > 1):
    return '''Your is_clear_winner() function definition uses
a total of %d conditional structures.  Simplify it so that it
uses only a single conditional structure, as directed.''' % num_is_clear_winner_ifs

return True
