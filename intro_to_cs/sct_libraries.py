import re


def handle_student_error(error):
    if (error):
        return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""
    return True


def handle_not_finished(error):
    if (error):
        return """The program still contains at least one error.
The cryptic error message to the right will identify the first line
that Python didn't like. Work your way through the directions
embedded in the comments until you've resolved the final one."""
    return True


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


def check_int_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Integer literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?\d+[ \t]*(#.*)?$',
                            no_match_msg)

prediction = 4
assert (check_int_prediction(3, 'prediction', 'prediction = 4') != True)
prediction = 3
assert (check_int_prediction(3, 'prediction', 'prediction = 3') == True)
assert (check_int_prediction(3, 'prediction', 'prediction = cheat') != True)
assert (check_int_prediction(3, 'prediction', 'prediction = (1+2)') != True)


def check_float_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Floating-point literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?[0-9.eE]+[ \t]*(#.*)?$',
                            no_match_msg)

prediction = 4.0
assert (check_float_prediction(3.0, 'prediction', 'prediction = 4.0') != True)
prediction = 3.0
assert (check_float_prediction(3.0, 'prediction', 'prediction = 3.0e0') == True)
assert (check_float_prediction(3.0, 'prediction', 'prediction = cheat') != True)
assert (check_float_prediction(3.0, 'prediction', 'prediction = (1+2)') != True)


def check_bool_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Boolean literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(True|False)[ \t]*(#.*)?$',
                            no_match_msg)

prediction = False
assert (check_bool_prediction(True, 'prediction', 'prediction = False') != True)
prediction = True
assert (check_bool_prediction(True, 'prediction', 'prediction = True') == True)
assert (check_bool_prediction(True, 'prediction', 'prediction = cheat') != True)
assert (check_bool_prediction(True, 'prediction', 'prediction = (1 > 2)') != True)
