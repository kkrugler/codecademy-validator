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

def check_str_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single String literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\'|")[^:+%]+[ \t]*(#.*)?$',
                            no_match_msg)

def check_int_prediction(expected, name, line):
    no_match_msg = '''You must assign %s to a single Integer literal value.
No "re-computing" your prediction!''' % name
    return check_prediction(expected,
                            name,
                            line,
                            r'^[^ \t=]+[ \t]*=[ \t]*(\+|-)?\d+[ \t]*(#.*)?$',
                            no_match_msg)

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) < 6):
    return '''It looks like you modified the code in such a way
that it no longer sends all of the output to the console that
it is supposed to. Click the Reset Code button, and start over.'''

if (len(printed_lines) > 6):
    return '''It looks like you modified the code so that it
sends an unexpected line to the console.
Click the Reset Code button and start over.'''

code_lines = code.splitlines()
line_number = 0
for line in code_lines:
    line_number += 1

    result = check_int_prediction(num_rooms,
                                  'num_rooms_prediction',
                                  line)
    if (result != True):
        return result

    result = check_str_prediction(room_a,
                                  'room_a_prediction',
                                  line)
    if (result != True):
        return result


    if (len(room_prediction) > 0):
        result = check_str_prediction(room,
                                      'room_prediction',
                                      line)
        if (result != True):
            return result

    if  (   (line.find('winner') >= 0)
        and (   (line.find('Sally') > 0)
            or  (line.find('[2]') > 0))):
        return '''You cheated on line %d.  You should fix the
second loop in such a way that it will remember the winning
player name no matter which player has the high score.
Click the Reset Code button and start over.''' % line_number

    if  (   line.startswith('players = [')
        and (line != "players = ['Jane', 'Bob', 'Sally', 'Dave']")):
        return '''It looks like you modified the original
assignment to the players List (or perhaps tried to reassign the
entire List?)  Make only the changes specifically described in
the comments and follow the instructions carefully when doing so.
Click the Reset Code button and start over.'''

if (len(room_prediction) == 0):
    return '''Next, predict the value of the room variable after
the first loop completes, by setting the room_prediction
variable to a String Literal as directed.'''

if (len(winner) == 0):
    return '''Next, add one line to the second loop so that it
announces the correct winner and score.'''

result = check_text('Sally won with a score of 7.',
                    printed_lines[0],
                    'announcement printed after the second loop',
                    'period');
if (result != True):
    return result

if (players == ['Jane', 'Bob', 'Sally', 'Dave']):
    return '''Finally, add lines to the third loop so that it
also sorts the players List to match the sorted scores List.'''

if (players != ['Sally', 'Jane', 'Dave', 'Bob']):
    return '''You didn't sort the players List properly.'''

if (scores != [7, 6, 5, 2]):
    return '''The changes you made broke the sorting of the
scores list.  Click the Reset Code button and start over.'''

return True