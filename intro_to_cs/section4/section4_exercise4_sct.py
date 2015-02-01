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

def check_int_literal(expected, name, line):
    no_match_msg = '''You must assign %s to a single Integer literal value.
No "computing" allowed!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?\d+[ \t]*(#.*)?$',
                            no_match_msg)

def check_float_literal(expected, name, line):
    no_match_msg = '''You must assign %s to a single Floating-point literal value.
No "computing" allowed!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?[0-9.eE]+[ \t]*(#.*)?$',
                            no_match_msg)

def check_bool_literal(expected, name, line):
    no_match_msg = '''You must assign %s to a single Boolean literal value.
No "computing" allowed!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(True|False)[ \t]*(#.*)?$',
                            no_match_msg)

if (error):
    return """The program still contains at least one error.
The cryptic error message to the right will identify the first line
that Python didn't like. Work your way through the directions
embedded in the comments until you've resolved the final one."""

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Click the Reset Code button and start over.'''

if (len(printed_lines) < 5):
    return '''You seem to have modified the program somehow so that
it no longer prints everything it was originally designed to.
Click the Reset Code button and start over.'''

is_found_user_condition_area = False
num_user_conditions = 0
code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1
    result = check_int_literal(42, 'my_int', line)
    if (result != True):
        return result
    result = check_float_literal(42.0, 'my_float', line)
    if (result != True):
        return result
    result = check_text('42', my_string, 'my_string')
    if (result != True):
        return result
    result = check_bool_literal(True, 'is_yes', line)
    if (result != True):
        return result
    actual = globals().get('my_empty')
    if (not ('my_empty' in globals())):
        return '''You seem to have modified the program somehow so that
it no longer assigns my_empty to anything.
Click the Reset Code button and start over.'''
    if (None != my_empty):
        return '''Your my_empty value was incorrect.'''
    if (line.find('my_int has') > 0):
        if (line.count('my_int') < 2):
            return '''Your print statement on line %i should
use the format operator and reference the variable my_int.''' % line_number
        if  (   (line.find('%i') < 0)
            and (line.find('%d') < 0)):
            return '''You could format your print statement on
line %i in better style.''' % line_number
    if  (   (line.find('my_float has') > 0)
        and (line.count('my_float') < 2)):
        return '''Your print statement on line %i should
use the format operator and reference the variable my_float.''' % line_number
    if  (   (line.find('my_string has') > 0)
        and (line.count('my_string') < 2)):
        return '''Your print statement on line %i should
use the format operator and reference the variable my_string.''' % line_number
    if  (   (line.find('is_yes has') > 0)
        and (line.count('is_yes') < 2)):
        return '''Your print statement on line %i should
use the format operator and reference the variable is_yes.''' % line_number
    if  (   (line.find('my_empty has') > 0)
        and (line.count('my_empty') < 2)):
        return '''Your print statement on line %i should
use the format operator and reference the variable my_empty.''' % line_number

result = check_text('my_int has the value 42!',
                    printed_lines[0],
                    'first line of output')
if (result != True):
    return result
result = check_text('my_float has the value 42.00!',
                    printed_lines[1],
                    'second line of output')
if (result != True):
    return result
result = check_text('my_string has the value 42!',
                    printed_lines[2],
                    'third line of output')
if (result != True):
    return result
result = check_text('is_yes has the value True!',
                    printed_lines[3],
                    'fourth line of output')
if (result != True):
    return result
result = check_text('my_empty has the value None!',
                    printed_lines[4],
                    'fifth line of output')
if (result != True):
    return result

return True
