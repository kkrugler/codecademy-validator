import re
import sys

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

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) > 1):
    return '''It looks like you modified the code so that it
sends an unexpected line to the console.
Click the Reset Code button and start over.'''

try:
    if (players.index('Bob') != 1):
        return '''You modified the wrong element of players.
Remember that positions are zero-based.'''
except:
    if (players[1] == 'bob'):
        return '''Use an assignment statement to capitalize the
second player name.'''

code_lines = code.splitlines()
line_number = 0
num_print_statements = 0
last_default_line_number = sys.maxint
num_player_removals = 0
num_player_pops = 0
num_player_inserts = 0
for line in code_lines:
    line_number += 1

    if  (   line.startswith('players = [')
        and (line.find('bob') < 0)):
        return '''It looks like you modified the original
assignment to the players List (or perhaps tried to reassign the
entire List?)  Make only the changes specifically described in
the comments and follow the instructions carefully when doing so.
Click the Reset Code button and start over.'''

    result = check_str_prediction(message_1,
                                  'message_1_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(message_2,
                                  'message_2_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(message_3,
                                  'message_3_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(message_4,
                                  'message_4_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(message_5,
                                  'message_5_prediction',
                                  line)
    if (result != True):
        return result
    result = check_str_prediction(message_6,
                                  'message_6_prediction',
                                  line)
    if (result != True):
        return result

    if (line.startswith('message_6_prediction')):
        last_default_line_number = line_number

    if (line_number > last_default_line_number):
        statement = line[:line.find('#')]
        num_player_removals += statement.count('players.remove(')
        num_player_pops += statement.count('players.pop(')
        num_player_inserts += statement.count('players.insert(')

    if (line.lstrip().startswith('print')):
        num_print_statements += 1
        if (num_print_statements == 1):
            result = check_text('Jane scored 6.',
                                printed_lines[0],
                                "console output from line %d" % line_number)
            if (result != True):
                return result

if (len(players) == 4):
    return '''Rearrange players so that it matches scores.'''
if (players != ['Sally', 'Jane', 'Dave']):
    return '''Your players aren't arranged correctly to match scores.'''
if  (   (num_player_removals != 1)
    or  (num_player_pops != 1)
    or  (num_player_inserts != 1)):
    return '''Rearrange players using exactly one remove, one
pop and one insert.'''

if (len(printed_lines) < 1):
    return '''Send a description of the second best player and
score to the console, as directed.'''

return True
