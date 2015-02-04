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

def check_prediction(expected, name, line, prediction_pattern, no_match_msg):
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
        if (expected != actual):
            return '''Your %s value was incorrect.''' % name
    return True


def check_int_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Integer literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*\d+[ \t]*(#.*)?$',
                            no_match_msg)

if (error):
    return """The program still contains at least one error.
The cryptic error message to the right will identify the first line
that Python didn't like. Work your way through the directions
embedded in the comments until you've resolved the final one."""

if (len(printed_lines) < 6):
    return '''It looks like you modified the code in some other
way than requested (e.g., commenting out too many lines).
Click the Reset Code button, and start over.'''

code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1
    result = check_int_prediction(quotient,
                                  'quotient_prediction',
                                  line)
    if (result != True):
        return result
    result = check_int_prediction(remainder,
                                  'remainder_prediction',
                                  line)
    if (result != True):
        return result

if (type(third_of_ten) != float):
    return '''You need to make sure the value you compute for
third_of_ten is a float. Dividing an int by another int instead
produces a third int.'''

MAX_FLOAT_DELTA = 0.000001
expected_third_of_ten = (10.0 / 3)
if (abs(expected_third_of_ten - third_of_ten) > MAX_FLOAT_DELTA):
    return '''You set third_of_ten to %s
instead of %f.''' % (third_of_ten, expected_third_of_ten)

result = check_text('One third of ten is roughly %.3f!' % expected_third_of_ten,
                    printed_lines[5],
                    'last print statement')
if (result != True):
    return result

return True
