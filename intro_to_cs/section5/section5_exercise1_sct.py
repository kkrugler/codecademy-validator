import re

printed_lines = CC.prints()

def check_text(expected, actual, desc, last_char_desc=None):
    if (type(actual) != str):
        return '''Your %s is not even a String.''' % desc
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
right will identify the first line that Python didn't like."""

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Click the Reset Code button and start over.'''

if (len(printed_lines) < 9):
    return '''You seem to have modified the program somehow so that
it no longer prints everything it was originally designed to.
Click the Reset Code button and start over.'''

result = check_text("It's time to eat.",
                    printed_lines[0],
                    "first print statement's output")
if (result != True):
    return result
result = check_text("It's time to eat.",
                    printed_lines[1],
                    "second print statement's output")
if (result != True):
    return result

result = check_text("Don't get all fussy!",
                    printed_lines[2],
                    "third print statement's output")
if (result != True):
    return result
result = check_text("Don't get all fussy!",
                    printed_lines[3],
                    "fourth print statement's output")
if (result != True):
    return result

result = check_text("Michelle can't make it here on time.",
                    printed_lines[4],
                    "fifth print statement's output")
if (result != True):
    return result
result = check_text("Michelle can't make it here on time.",
                    printed_lines[5],
                    "sixth print statement's output")
if (result != True):
    return result

is_found_user_condition_area = False
num_user_conditions = 0
code_lines = code.splitlines()
line_number = 0
print_number = 0
num_breaks = 0
is_triple_single = False
for line in code_lines:
    line_number += 1
    if (line.startswith('print')):
        if  (   (print_number < 6)
            and (   ((print_number % 2) == 0)
                ==  (line.find("\\") > 0))):
            return '''The second instance in each pair should
escape the apostrophe; the first should just use double quotes.
Fix the print statement on line %i.''' % line_number
        print_number += 1

        if (line.find("'''") > 0):
            is_triple_single = True

    line = line.split('#', 2)[0]
    if  (   (print_number == 7)
        and (not line.rstrip().endswith('"'))
        and (len(line.strip()) > 0)):
        if (line.rstrip().endswith('\\')):
            num_breaks += 1
        else:
            return '''Line %i should end with the continuation
character.''' % line_number

    if  (   (print_number >= 7)
        and (print_number <= 8)
        and (len(line.strip()) > 0)
        and line.startswith(' ')):
        return '''Line %i begins with an extra space character.''' % line_number

if (num_breaks != 3):
    return '''Your seventh print statement should be broken into
four pieces using the continuation character.'''

result = check_text("Now is the time for all good men to come to the aid of their country, don't you think?",
                    printed_lines[6],
                    "seventh print statement's output")
if (result != True):
    return result

if (len(printed_lines) < 10):
    return '''Repeat the seventh print statement, but use a String
literal with triple-' syntax to break it up into the same four parts.'''

if (printed_lines[7].count('\n') != 3):
    return '''Your eighth print statement should be broken into
four pieces using triple-' syntax.'''

pieces = printed_lines[7].split('\n')
joined = "%s %s %s %s" % (pieces[0].rstrip(),
                          pieces[1].rstrip(),
                          pieces[2].rstrip(),
                          pieces[3].rstrip())
result = check_text("Now is the time for all good men to come to the aid of their country, don't you think?",
                    joined,
                    "eighth print statement's output (after removing breaks)")
if (result != True):
    return result

if (is_triple_single):
    return '''Modify your eighth print statement to use triple-"
syntax instead.'''

result = check_text("The backslash (\\) is Python's escape character.",
                    printed_lines[8],
                    "ninth print statement's output")
if (result != True):
    return result

result = check_text('Three backslashes can be printed like so: \\\\\\',
                    printed_lines[9],
                    "tenth print statement's output")
if (result != True):
    return result

return True
