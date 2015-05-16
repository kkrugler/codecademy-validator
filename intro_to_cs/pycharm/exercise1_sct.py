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
    return '''Your %s was incorrect.%s''' % (desc, case_warning)

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

def check_int_prediction(expected, name, line, section=None):
    no_match_msg = '''You must assign %s to a single Integer literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?\d+[ \t]*(#.*)?$',
                            no_match_msg,
                            section)

def check_str_prediction(expected, name, line, section=None):
    no_match_msg = '''You must assign %s to a single String literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\'|")[^+%]+[ \t]*(#.*)?$',
                            no_match_msg,
                            section)

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1

    result = check_int_prediction(15,
                                  'answer_1',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(0,
                                  'answer_2',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('red',
                                  'answer_3',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('blue',
                                  'answer_4',
                                  line)
    if (result != True):
        result = check_str_prediction('red',
                                      'answer_4',
                                      line)
        if (result != True):
            return result

    result = check_str_prediction('increase',
                                  'answer_5',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('yes',
                                  'answer_6',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(10,
                                  'answer_7',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('num_cats',
                                  'answer_8_name',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(17,
                                  'answer_8_value',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('num_cats',
                                  'answer_9_name',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(18,
                                  'answer_9_value',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(8,
                                  'answer_10',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('yes',
                                  'answer_11',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('increase, game.py:5',
                                  'answer_12',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(8,
                                  'answer_13',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('num_cats',
                                  'answer_14_name',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(20,
                                  'answer_14_value',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(8,
                                  'answer_15',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(9,
                                  'answer_16',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('no',
                                  'answer_17',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(11,
                                  'answer_18',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction('4. 1',
                                  'answer_19',
                                  line)
    if (result != True):
        return result

    result = check_int_prediction(25,
                                  'answer_20',
                                  line)
    if (result != True):
        return result

return True