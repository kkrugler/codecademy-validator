printed_lines = CC.prints()

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

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Click the Reset Code button and start over.'''

if (len(printed_lines) < printed_line_count):
    return '''You seem to have modified the program somehow so that
it no longer prints everything it was originally designed to.
Click the Reset Code button and start over.'''

if (true_condition_count != true_condition_count_prediction):
    return '''Your predicted value for true_condition_count was wrong.'''

if (printed_line_count != printed_line_count_prediction):
    return '''Your predicted value for printed_line_count was wrong.'''

is_found_user_condition_area = False
num_user_conditions = 0
code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1
    if (line.startswith('# Write your own conditional statement')):
        is_found_user_condition_area = True
    if (is_found_user_condition_area):
        line = line.strip()
        if (line.startswith('if')):
            num_user_conditions += 1
            if (line.find('true_condition_count') >= 0):
                if  (   (line.find('4') < 0)
                    and (   (line.find('5') < 0)
                        or  (line.find('=') < 0))):
                    return '''The condition you added on line %d doesn't
seem like it would always work as intended. It might just be more
complex than necessary, but it probably has a bug.''' % line_number
                if  (   (line_number == len(code_lines))
                    or  (not code_lines[line_number].startswith('    print'))):
                    return '''The condition you added on line %d doesn't
seem to be followed by a properly indented print statement. It might just be more
complex than necessary, but it probably has a bug.''' % line_number
            elif (line.find('printed_line_count') >= 0):
                if  (   (line.find('10') < 0)
                    and (   (line.find('9') < 0)
                        or  (line.find('=') < 0))):
                    return '''The condition you added on line %d doesn't
seem like it would always work as intended. It might just be more
complex than necessary, but it probably has a bug.''' % line_number
            else:
                return '''The condition you added on line %d doesn't
refer to true_condition_count or printed_line_count.''' % line_number

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
    if (line.strip().startswith('More than')):
        return '''The code you added did end up printing "%s",
but its condition should not have been true.''' % line
    if (line.strip().startswith('Less than')):
        if (user_printed_line):
            return '''The code you added ended up printing
at least two lines that began with "Less than".'''
        else:
            user_printed_line = line

result = check_text('Less than ten lines were printed (not including this one)',
                    user_printed_line,
                    'printed line')
if (result != True):
    return result

return True
