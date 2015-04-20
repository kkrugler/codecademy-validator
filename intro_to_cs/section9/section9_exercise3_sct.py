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

def check_str_prediction(expected, name, line, section=None):
    no_match_msg = '''You must assign %s to a single String literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\'|")[^[\]:+%]+[ \t]*(#.*)?$',
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
console.  You're not going to learn much about optional function
parameters if you continue CHEATING.  Instead, please try to
execute the code in your head.'''

expected_warn_1 = 'Note that texting is prohibited on campus!'
expected_warn_2 = 'Note that all cell phone usage is prohibited on campus!'
expected_warn_3 = 'Note that skateboarding is prohibited in the computer lab!'
expected_warn_4 = 'Note that PDA is prohibited on campus while teachers are looking!'

code_lines = code.splitlines()
line_number = 0
num_texting_invocations = 0
num_on_campus_invocations = 0
for line in code_lines:
    line_number += 1

    result = check_str_prediction(expected_warn_1,
                                  'warn_1_prediction',
                                  line)
    if (result != True):
        return result

    if (warn_2_prediction != ''):
        result = check_str_prediction(expected_warn_2,
                                      'warn_2_prediction',
                                      line)
        if (result != True):
            return result

    if (warn_3_prediction != ''):
        result = check_str_prediction(expected_warn_3,
                                      'warn_3_prediction',
                                      line)
        if (result != True):
            return result

    if (warn_4_prediction != ''):
        result = check_str_prediction(expected_warn_4,
                                      'warn_4_prediction',
                                      line)
        if (result != True):
            return result

    if  (   line.startswith('warn_')
        and (line.find('_prediction') < 0)):
        if (line.find('texting') > 0):
            num_texting_invocations += 1
        if (line.find('on campus') > 0):
            num_on_campus_invocations += 1

if (warn_2_prediction == ''):
    return '''Next, predict the result of the second invocation
of warn(), as directed.'''

if (warn_3_prediction == ''):
    return '''Next, predict the result of the third invocation
of warn(), as directed.'''

if (warn_4_prediction == ''):
    return '''Next, predict the result of the fourth invocation
of warn(), as directed.'''

result = check_text(expected_warn_1,
                    warn('texting', 'on campus'),
                    "warn('texting', 'on campus')",
                    True)
if (result != True):
    return result

result = check_text(expected_warn_2,
                    warn('all cell phone usage', 'on campus'),
                    "warn('all cell phone usage', 'on campus')",
                    True)
if (result != True):
    return result

result = check_text(expected_warn_3,
                    warn('skateboarding', 'in the computer lab'),
                    "warn('skateboarding', 'in the computer lab')",
                    True)
if (result != True):
    return result

result = check_text(expected_warn_4,
                    warn('PDA', 'on campus', 'while teachers are looking'),
                    "warn('PDA', 'on campus', 'while teachers are looking')",
                    True)
if (result != True):
    return result

try:
    try:
        result = check_text(expected_warn_1,
                            warn('texting'),
                            "warn('texting') result",
                            True)
        if (result != True):
            return result
    except TypeError:
        return '''Next, modify the warn() function definition so
that the first invocation wouldn't have to specify the location
argument, as directed.'''

    if (num_on_campus_invocations == 3):
        return '''Next, simplify any invocations of warn() that
can take advantage of your modification to its signature.'''

    result = check_text(expected_warn_1, warn_1, "warn_1", True)
    if (result != True):
        return result
    result = check_text(expected_warn_2, warn_2, "warn_2", True)
    if (result != True):
        return result
    result = check_text(expected_warn_3, warn_3, "warn_3", True)
    if (result != True):
        return result
    result = check_text(expected_warn_4, warn_4, "warn_4", True)
    if (result != True):
        return result

    if (num_on_campus_invocations > 1):
        return '''There is at least one warn() invocation that
could still be simplified to take advantage of your modification
to its signature.'''

    try:
        result = check_text(expected_warn_1,
                            warn(),
                            "warn() result",
                            True)
        if (result != True):
            return result
    except TypeError:
        return '''Next, modify the warn() function definition so
that the first invocation wouldn't have to specify ANY arguments,
as directed.'''

    if (num_texting_invocations > 0):
        return '''Next, simplify any invocations of warn() that
can take advantage of your modification to its signature.'''

except:
    return '''You seem to have broken the warn() function
definition with your changes so that invoking it returns an error.
The cryptic error message to the right will identify the first
line that Python didn't like. You can try to fix the error you
introduced, or just click the Reset Code button and start over.'''

return True