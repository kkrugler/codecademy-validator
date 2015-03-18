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

def check_prediction(expected, name, line, prediction_pattern, no_match_msg, section):
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
            return '''One of the predictions in your %s set
was incorrect.''' % section
    return True

def check_int_prediction(expected, name, line, section):
    no_match_msg = '''You must assign %s to a single Integer literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?\d+[ \t]*(#.*)?$',
                            no_match_msg,
                            section)

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) < 7):
    return '''It looks like you modified the code in such a way
that it no longer sends all of the output to the console that
it is supposed to. Click the Reset Code button, and start over.'''

if (len(printed_lines) > 7):
    return '''You should be ashamed of yourself!  It looks like
you modified the code so that it sends an unexpected line to the
console.  You're not going to learn much about the break and
continue statements if you continue CHEATING.  Instead, please
try to execute the code in your head.'''

code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1

    result = check_int_prediction(20,
                                  'score_prediction_1',
                                  line,
                                  'first')
    if (result != True):
        return result
    result = check_int_prediction(10,
                                  'num_twists_prediction_1',
                                  line,
                                  'first')
    if (result != True):
        return result

    if (score_prediction_2 != 0):
        result = check_int_prediction(18,
                                      'score_prediction_2',
                                      line,
                                      'second')
        if (result != True):
            return result
        result = check_int_prediction(8,
                                      'num_twists_prediction_2',
                                      line,
                                      'second')
        if (result != True):
            return result

    if (score_prediction_3 != 0):
        result = check_int_prediction(26,
                                      'score_prediction_3',
                                      line,
                                      'third')
        if (result != True):
            return result
        result = check_int_prediction(10,
                                      'num_twists_prediction_3',
                                      line,
                                      'third')
    if (result != True):
        return result

if (score_prediction_2 == 0):
    return '''Next, predict the values of the two variables
after the second loop terminates, as directed.'''

if (score_prediction_3 == 0):
    return '''Finally, predict the values of the two variables
after the third loop terminates, as directed.'''


return True