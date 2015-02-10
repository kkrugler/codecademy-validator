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

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

result = check_text('42', my_int_as_string, 'my_int_as_string');
if (result != True):
    return result

result = check_text('42.0', my_float_as_string, 'my_float_as_string');
if (result != True):
    return result

result = check_text('True', is_yes_as_string, 'is_yes_as_string');
if (result != True):
    return result

if (len(printed_lines) < 3):
    return """Your modifications have prevented the code from
generating the three lines to the console. You can try to fix
the error you introduced, or just click the Reset Code button and
start over."""

result = check_text('my_int looks like 42',
                    printed_lines[0],
                    'first line of console output');
if (result != True):
    return result

result = check_text('my_float looks like 42.0',
                    printed_lines[1],
                    'second line of console output');
if (result != True):
    return result

result = check_text('is_yes looks like True',
                    printed_lines[2],
                    'third line of console output');
if (result != True):
    return result

code_lines = code.splitlines()
line_number = 0
num_print_statements = 0
for line in code_lines:
    line_number += 1

    if (line.startswith('my_int_as_string')):
        if (line.find('str(') < 0):
            return """Use the String constructor to assign the
string representation of my_int to my_int_as_string
on line %d.""" % line_number
        if (line.count('my_int') < 2):
            return """Pass my_int to the String constructor in
your assignment statement on line %d.""" % line_number

    if (line.startswith('my_float_as_string')):
        if (line.find('str(') < 0):
            return """Use the String constructor to assign the
string representation of my_float to my_float_as_string
on line %d.""" % line_number
        if (line.count('my_float') < 2):
            return """Pass my_float to the String constructor in
your assignment statement on line %d.""" % line_number

    if (line.startswith('is_yes_as_string')):
        if (line.find('str(') < 0):
            return """Use the String constructor to assign the
string representation of is_yes to is_yes_as_string
on line %d.""" % line_number
        if (line.count('is_yes') < 2):
            return """Pass is_yes to the String constructor in
your assignment statement on line %d.""" % line_number

    if (line.startswith('print')):
        num_print_statements += 1
        if  (   (num_print_statements > 3)
            and (line.find('str(') < 0)):
            return """Use the String constructor to build the
string representation on line %d.""" % line_number

if (len(printed_lines) < 6):
    return """Add three more print statements as directed."""

result = check_text('my_int looks like 42',
                    printed_lines[3],
                    'first line of console output');
if (result != True):
    return result

result = check_text('my_float looks like 42.0',
                    printed_lines[4],
                    'second line of console output');
if (result != True):
    return result

result = check_text('is_yes looks like True',
                    printed_lines[5],
                    'third line of console output');
if (result != True):
    return result

return True
