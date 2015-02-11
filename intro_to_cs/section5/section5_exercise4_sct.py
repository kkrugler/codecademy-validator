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
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?\d+[ \t]*(#.*)?$',
                            no_match_msg)

def check_str_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single String literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\'|")[^[\]:+%]+[ \t]*(#.*)?$',
                            no_match_msg)

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) < 10):
    return '''It looks like you modified the code so that it no longer
prints all the lines to the console that it originally did.
Click the Reset Code button and start over.'''

if (printed_lines[1].startswith('It does')):
    return '''Please add a print statement as directed that uses
the upper() String method.'''

result = check_text('DO YOUR HOMEWORK!',
                    printed_lines[1],
                    'uppercase version of my_string',
                    'exclamation point')
if (result != True):
    return result

if (printed_lines[3] != 'Your code might be working properly.'):
    return '''Please modify the second conditional as directed
to test whether my_string ends with "homework".'''

code_lines = code.splitlines()
line_number = 0
num_print_statements = 0
for line in code_lines:
    line_number += 1

    if (line.lstrip().startswith('print')):
        num_print_statements += 1
        if  (   (num_print_statements == 2)
            and (   (line.find('HOMEWORK') > 0)
                or  (line.find('my_string.upper()') < 0))):
            return '''You cheated on line %i. Call the upper() method
of my_string and then print the result
(all in a single statement).''' % line_number

    if  (   (num_print_statements == 4)
        and (line.startswith('if'))
        and (   (line.find('my_string.endswith') < 0)
            or  (line.find('homework') < 0))):
        return '''Your modification on line %i
doesn't look right. It should test whether my_string ends with
"homework".''' % line_number

    result = check_int_prediction(position_1,
                                  'position_1_prediction',
                                  line)
    if (result != True):
        return result
    result = check_int_prediction(position_2,
                                  'position_2_prediction',
                                  line)
    if (result != True):
        return result
    result = check_int_prediction(position_3,
                                  'position_3_prediction',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction(string_1,
                                  'string_1_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(string_2,
                                  'string_2_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(string_3,
                                  'string_3_prediction',
                                  line)
    if (result != True):
        return result

result = check_text('Chris is awesome',
                    improve_chris_status('Chris is OK'),
                    "improve_chris_status('Chris is OK') return value")
if (result != True):
    return result

result = check_text('Kate is OK',
                    improve_chris_status('Kate is OK'),
                    "improve_chris_status('Kate is OK') return value")
if (result != True):
    return result

result = check_text('Chris and Kate are awesome',
                    improve_chris_status('Chris and Kate are OK'),
                    "improve_chris_status('Chris and Kate are OK') return value")
if (result != True):
    return result

result = check_text('Kate and Chris are awesome',
                    improve_chris_status('Kate and Chris are OK'),
                    "improve_chris_status('Kate and Chris are OK') return value")
if (result != True):
    return result

return True
