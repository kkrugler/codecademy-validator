import re

printed_lines = CC.prints()

def check_text(expected, actual, desc, last_char_desc=None):
    if (type(actual) != str):
        return '''Your %s is not even a String.''' % desc
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
    return """The program still contains at least one error.
The cryptic error message to the right will identify the first line
that Python didn't like. Work your way through the directions
embedded in the comments until you've resolved the final one."""

if (len(printed_lines) < 7):
    return '''It looks like you modified the code in some other
way than requested (e.g., commenting out too many lines).
Click the Reset Code button, and start over.'''

result = check_text('I think scores less than 10 are wimpy.',
                    printed_lines[5],
                    'second to last print statement')
if (result != True):
    return result

result = check_text('Female spiders are generally larger.',
                    printed_lines[6],
                    'last print statement')
if (result != True):
    return result

code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1
    if (line.find('wimpy') > 0):
        if (line.find('%') < 0):
            return '''You need to build your print statement on line %d
using the formatting operator.''' % line_number
        if (line.find('%s') > 0):
            return '''You could improve the style of your print
statement on line %d so that it will only insert numbers.''' % line_number
    if (line.find('spiders') > 0):
        if (line.find('%') < 0):
            return '''You need to build your print statement on line %d
using the formatting operator.''' % line_number

return True
