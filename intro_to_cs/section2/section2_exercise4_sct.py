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

if (first_name != 'Kenneth'):
    return '''You changed the value of first_name.
Click the Reset button and instead improve the way that full_name
and your print statements built from this and the other parts.'''

if (last_name != 'Krugler'):
    return '''You changed the value of last_name.
Click the Reset button and instead improve the way that full_name
and your print statements built from this and the other parts.'''

if (occupation != 'programmer'):
    return '''You changed the value of occupation.
Click the Reset button and instead improve the way that full_name
and your print statements built from this and the other parts.'''

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Click the Reset Code button and start over.'''

if (len(printed_lines) < 2):
    return '''Your program didn't display a second line of text
to the user.  If you can't figure out why, then you might want to
click the Reset Code button to start again from scratch.'''

result = check_text("His name is Kenneth.",
                    printed_lines[1],
                    "second print statement",
                    "period")
if (result != True):
    return result

if (not ('full_name' in globals())):
    return '''You forgot to assign a variable named "full_name".'''

expected_full_name = "Kenneth Krugler"
result = check_text(expected_full_name,
                    full_name,
                    "full_name variable")
if (result != True):
    return result

if (len(printed_lines) < 3):
    return '''Your program didn't display a third line of text
to the user.  If you can't figure out why, then you might want to
click the Reset Code button to start again from scratch.'''

expected_line = "%s is an awesome programmer!" % expected_full_name
result = check_text(expected_line,
                    printed_lines[2],
                    "third print statement",
                    "exclamation point")
if (result != True):
    return result

lines = code.splitlines()

line_number = 0
for line in lines:
    line_number += 1
    line = line.strip()
    if line.startswith('print'):
        if (line.find('%') < 0):
            return '''You cheated on line %d.  Every print statement should
use the formatting operator (%%) to build the console message.''' % line_number
        if (line.find('+') > 0):
            return '''You cheated on line %d.  Do not use the
concatenation operator (+) to build the console message.
Use only the formatting operator.''' % line_number
        if  (   (line.find('awesome') >= 0)
            and (line.find('occupation') < 0)):
            return '''You cheated on line %d.  Use the occupation variable
to build the console message.''' % line_number
    if line.startswith('full_name'):
        if (line.find('%') < 0):
            return '''You cheated on line %d.  Use the formatting
operator (%%) to build the value of full_name.''' % line_number

return True
