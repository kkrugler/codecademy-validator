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

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (first_name != 'Kenneth'):
    return '''You changed the value of first_name.
Click the Reset button and instead improve the way that formal_name
gets built from this and the other parts.'''

if (middle_initial != 'W'):
    return '''You changed the value of middle_initial.
Click the Reset button and instead improve the way that formal_name
gets built from this and the other parts.'''

if (last_name != 'Krugler'):
    return '''You changed the value of last_name.
Click the Reset button and instead improve the way that formal_name
gets built from this and the other parts.'''

if (formal_name == 'KennethWKrugler'):
    return """The three parts of the formal name are jumbed
together (%s). You should insert spaces between them.""" % formal_name

result = check_text("Kenneth W Krugler",
                    formal_name,
                    "formal_name variable")
result2 = check_text("Kenneth W. Krugler",
                     formal_name,
                     "formal_name variable")
if  (   (result != True)
    and (result2 != True)):
    return result

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Click the Reset Code button and start over.'''

expected_line = "His formal name is %s" % formal_name
if (printed_lines[0] != expected_line):
    return '''Your first print statement output "%s"
instead of "%s".  You weren't supposed to change the
print statement itself, just the value of the
full_name variable.  You might want to click the Reset Code
button to start again from scratch.''' % (printed_lines[0], expected_line)

if (len(printed_lines) < 2):
    return '''Your program didn't display a second line of text
to the user.  If you can't figure out why, then you might want to
click the Reset Code button to start again from scratch.'''

expected_template = "The variable formal_name contains %s."
default_line = expected_template % "formal_name"
if (printed_lines[1] == default_line):
    return '''You didn't fix the second print statement.'''

expected_line = expected_template % formal_name
result = check_text(expected_line,
                    printed_lines[1],
                    "second print statement")
if (result != True):
    return result

lines = code.splitlines()

line_number = 0
for line in lines:
    line_number += 1
    line = line.strip()
    if (line.startswith('formal_name')):
        if (line.find('+') < 0):
            return '''You cheated on line %d.  Use the concatenation
operator (+) to build the value of formal_name.''' % line_number
        if (line.find('Kenneth') > 0):
            return '''You cheated on line %d.  Use the first_name
variable to build the value of formal_name.''' % line_number
        if (line.find('W') > 0):
            return '''You cheated on line %d.  Use the middle_initial
variable to build the value of formal_name.''' % line_number
        if (line.find('Krugler') > 0):
            return '''You cheated on line %d.  Use the last_name
variable to build the value of formal_name.''' % line_number
    if line.startswith('print'):
        if (line.find('+') < 0):
            return '''You cheated on line %d.  Every print statement should
use the concatenation operator (+) to build the console message.''' % line_number
        if  (   (line.find('contains') > 0)
            and (   (line.find('Kenneth') > 0)
                or  (line.find('first_name') > 0))):
            return '''You cheated on line %d.  Use the formal_name variable
to build the console message.''' % line_number

return True
