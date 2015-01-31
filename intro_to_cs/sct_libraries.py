import re

def check_text(expected, actual, desc, last_char_desc=None):
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

def check_int_prediction(expected, actual, name, line):
    assignment_re = re.compile(r'^([^ \t=]+)[ \t]*=([^=].*)?$')
    assignment_match = assignment_re.match(line)
    if  (   (assignment_match)
        and (assignment_match.groups()[0] == name)):
        prediction_re = re.compile(r'^[^ \t=]+[ \t]*=[ \t]*\d+[ \t]*(#.*)?$')
        if (not prediction_re.match(line)):
            return '''You must assign %s to a single Integer literal value.
No "re-computing" your prediction!''' % name
    if (expected != actual):
        return '''Your %s value was incorrect.''' % name
    return True

assert (check_int_prediction(3, 3, 'prediction', 'prediction = 3') == True)
assert (check_int_prediction(3, 4, 'prediction', 'prediction = 4') != True)
assert (check_int_prediction(3, 3, 'prediction', 'prediction = cheat') != True)
assert (check_int_prediction(3, 3, 'prediction', 'prediction = (1+2)') != True)

