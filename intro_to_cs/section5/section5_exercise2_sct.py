import re

printed_lines = CC.prints()

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

def check_bool_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Boolean literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(True|False)[ \t]*(#.*)?$',
                            no_match_msg)

def check_str_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single String literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\'|")[^[\]:+%]+[ \t]*(#.*)?$',
                            no_match_msg)

if ((error) and (type(error) == IndexError)):
    return """It looks like you guessed incorrectly.  The console
is displaying an IndexError from Python about the bad line.
Think about why this line caused the problem, whereas the others
did not, then re-insert the comment character at the beginning
of this line and remove the comment character from the others."""

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
    result = check_str_prediction(substring_1,
                                  'substring_1_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_0_1,
                                  'substring_0_1_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_0_2,
                                  'substring_0_2_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_4,
                                  'substring_4_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_4_6,
                                  'substring_4_6_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_6,
                                  'substring_6_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_27_28,
                                  'substring_27_28_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(substring_21_27,
                                  'substring_21_27_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(long_substring,
                                  'long_substring_prediction',
                                  line)
    if (result != True):
        return result
    result = check_int_prediction(len_15_15,
                                  'len_15_15_prediction',
                                  line)
    if (result != True):
        return result
    result = check_bool_prediction(is_equal_to_none,
                                   'is_equal_to_none_prediction',
                                   line)
    if (result != True):
        return result

if (len(printed_lines) < 4):
    return '''Remove the comment character from the beginning of all
the print statements except for the one that you think would generate
an IndexError, then click the Save & Submit button to check your guess.'''

return True
