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

def check_bool_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Boolean literal value.
No "re-computing" your prediction!''' % name
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

if (len(printed_lines) < printed_line_count):
    return '''You seem to have modified the program somehow so that
it no longer prints everything it was originally designed to.
Click the Reset Code button and start over.'''

is_found_user_condition_area = False
num_user_conditions = 0
code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1
    result = check_bool_prediction(is_python_broken,
                                   'is_python_broken_prediction',
                                   line)
    if (result != True):
        return result
    result = check_int_prediction(  true_condition_count,
                                    'true_condition_count_prediction',
                                    line)
    if (result != True):
        return result
    result = check_int_prediction(  printed_line_count,
                                    'printed_line_count_prediction',
                                    line)
    if (result != True):
        return result
    if (line.startswith('# Assign the is_many_were_true')):
        is_found_user_condition_area = True
    if (is_found_user_condition_area):
        line = line.strip()
        if (result != True):
            return result
        if (line.startswith('if')):
            num_user_conditions += 1
            if (line.find('true_condition_count') >= 0):
                return '''The condition you added on line %i
should use is_many_were_true instead.''' % line_number
                if  (   (line_number == len(code_lines))
                    or  (not code_lines[line_number].startswith('    print'))):
                    return '''The condition you added on line %i doesn't
seem to be followed by a properly indented print statement. It might just be more
complex than necessary, but it probably has a bug.''' % line_number
            elif (line.find('printed_line_count') >= 0):
                return '''The condition you added on line %i
should use is_few_lines_printed instead.''' % line_number
            elif    (   (line.find('is_many_were_true') < 0)
                    and (line.find('is_few_lines_printed') < 0)):
                return '''The condition you added on line %i doesn't
refer to is_many_were_true or is_few_lines_printed.''' % line_number
        elif    (   (   line.startswith('is_many_were_true')
                    or  line.startswith('is_few_lines_printed'))
                and (   (line.find('True') > 0)
                    or  (line.find('False') > 0))):
            return '''Your assignment on line %i would not work
for all possible values of the two counters.''' % line_number

if (not is_found_user_condition_area):
    return '''You seem to have deleted part of the original program.
Click the Reset Code button and start over.'''

if (num_user_conditions < 2):
    return '''Please add both of the conditional statements described
in the comments near the end of the program.'''

if (num_user_conditions > 2):
    return '''You seem to have added more than two conditional
statements to the program. Click the Reset Code button and start over.'''

user_printed_line = None
for line in printed_lines[printed_line_count:]:
    if (line.strip().lower().startswith('more than')):
        return '''The code you added did end up printing "%s",
but its condition should not have been true.''' % line
    elif (line.strip().lower().startswith('fewer than')):
        if (user_printed_line):
            return '''The code you added ended up printing
at least two lines that began with "Fewer than".'''
        else:
            user_printed_line = line
    elif (len(printed_lines) > (printed_line_count)):
        return '''The code you added printed the unexpected line "%s"''' % line

if (user_printed_line):
    result = check_text('Fewer than ten lines were printed (not including this one)',
                        user_printed_line,
                        'printed line')
    if (result != True):
        return result
else:
    return '''The code you added didn't print anything that
starts with "Fewer than".'''

return True
