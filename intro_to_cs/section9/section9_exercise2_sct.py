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

def check_int_prediction(expected, name, line, section=None):
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

if ((score != 10) and (score != 14)):
    if  (   (score_prediction_5 == 10)
        or  (score_prediction_5 == 14)):
        return """Your changes to the code have modified the
behavior of one or more of the functions (and NOT in the way
specifically directed in the final step of this exercise)."""
    else:
        return """Your changes to the code have modified the
behavior of one or more of the functions.  Please click the
Reset Code button and start over."""

if (len(printed_lines) > 0):
    return '''You should be ashamed of yourself!  It looks like
you modified the code so that it sends an unexpected line to the
console.  You're not going to learn much about managing global
variables if you continue CHEATING.  Instead, please try to
execute the code in your head.'''

code_lines = code.splitlines()
line_number = 0
num_global_score_declarations = 0
num_global_extra_points_declarations = 0
for line in code_lines:
    line_number += 1

    result = check_int_prediction(8,
                                  'result_1_prediction',
                                  line,
                                  'first')
    if (result != True):
        return result
    result = check_int_prediction(8,
                                  'score_prediction_1',
                                  line,
                                  'first')
    if (result != True):
        return result

    if  (   (result_2_prediction != 0)
        or  (score_prediction_2 != 0)):
        if (score == 14):
            expected_score_prediction_2 = 12
        else:
            expected_score_prediction_2 = 8
        result = check_int_prediction(result_2,
                                      'result_2_prediction',
                                      line,
                                      'second')
        if (result != True):
            return result
        result = check_int_prediction(expected_score_prediction_2,
                                      'score_prediction_2',
                                      line,
                                      'second')
        if (result != True):
            return result

    if  (   (result_3_prediction != 0)
        or  (score_prediction_3 != 0)):
        if (score == 14):
            expected_result_3_prediction = 14
            expected_score_prediction_3 = 12
        else:
            expected_result_3_prediction = 10
            expected_score_prediction_3 = 8
        result = check_int_prediction(expected_result_3_prediction,
                                      'result_3_prediction',
                                      line,
                                      'third')
        if (result != True):
            return result
        result = check_int_prediction(expected_score_prediction_3,
                                      'score_prediction_3',
                                      line,
                                      'third')
        if (result != True):
            return result

    if  (   (result_4_prediction != 0)
        or  (score_prediction_4 != 0)):
        if (score == 14):
            expected_result_4_prediction = 12
            expected_score_prediction_4 = 12
        else:
            expected_result_4_prediction = 12
            expected_score_prediction_4 = 8
        result = check_int_prediction(expected_result_4_prediction,
                                      'result_4_prediction',
                                      line,
                                      'fourth')
        if (result != True):
            return result
        result = check_int_prediction(expected_score_prediction_4,
                                      'score_prediction_4',
                                      line,
                                      'fourth')
        if (result != True):
            return result

    if (score_prediction_5 != 0):
        if (score == 14):
            expected_score_prediction_5 = 14
        else:
            expected_score_prediction_5 = 10
        result = check_int_prediction(expected_score_prediction_5,
                                      'score_prediction_5',
                                      line,
                                      'fifth')
        if (result != True):
            return result

    if (line.strip().startswith('global')):
        if (line.find('score') > 0):
            num_global_score_declarations += 1
        if (line.find('extra_points') > 0):
            num_global_extra_points_declarations += 1

if (score_prediction_2 == 0):
    return '''Next, predict the values of the two variables in
the second section, as directed.'''

if (score_prediction_3 == 0):
    return '''Next, predict the values of the two variables in
the third section, as directed.'''

if (score_prediction_4 == 0):
    return '''Next, predict the values of the two variables in
the fourth section, as directed.'''

if (score_prediction_5 == 0):
    return '''Next, predict the value of the variable
in the fifth section, as directed.'''

if  (   (num_global_extra_points_declarations == 4)
    and (num_global_score_declarations == 2)):
    return '''Next, remove any unnecessary variable names from
the global statements in the function definitions, as directed.'''

if  (   (num_global_extra_points_declarations > 0)
    or  (   (num_global_score_declarations > 1)
        and (score == 10))):
    return '''There is at least one unnecessary variable name in
a global statement within a function definition.'''

if (score == 10):
    return '''Finally add one variable name to one global
statement within one function definition, but without introducing
a syntax error, as directed.'''

return True
