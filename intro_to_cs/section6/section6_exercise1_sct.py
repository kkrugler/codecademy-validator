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
                            r'^[^ \t=]+[ \t]*=[ \t]*(\'|")[^[\]:+%]+[ \t]*(#.*)?$',
                            no_match_msg)

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(printed_lines) < 8):
    return '''It looks like you modified the code so that it no longer
prints all the lines to the console that it originally did.
Click the Reset Code button and start over.'''

if  (   (len(printed_lines) > 8)
    and (   (len(printed_lines) > 9)
        or  printed_lines[0].startswith('letters'))):
    return '''It looks like you modified the code so that it
sends an unexpected line to the console.
Click the Reset Code button and start over.'''

code_lines = code.splitlines()
line_number = 0
num_print_statements = 0
for line in code_lines:
    line_number += 1

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

    if  (   line.startswith('best_3_players')
        and (line.find('()') < 0)
        and (line.count('players[') != 3)):
            return '''Your assignment statement on line %d should
reference three elements from the players Tuple.''' % line_number

    if (line.lstrip().startswith('print')):
        num_print_statements += 1
        if  (   (len(printed_lines) > 8)
            and (num_print_statements == 1)):
            if  (   (line.find('player_score_message') < 0)
                or  (line.find('best_3_players') < 0)
                or  (line.find('best_3_scores') < 0)):
                return '''You cheated on line %d.
Call the player_score_message() function using best_3_players
and best_3_scores (referencing one element from each)
and print the result (all in a single statement).''' % line_number
            result = check_text('Jane scored 6.',
                                printed_lines[0],
                                "console output from line %d" % line_number)
            if (result != True):
                return result

    if  (   line.startswith('best_2_players')
        and (line != 'best_2_players = best_3_players')):
        if (line.find('best_3_players[') < 0):
            return '''Your assignment statement on line %d should
take a slice of the best_3_players Tuple.''' % line_number
        if (line.find('(') > 0):
            return '''Your assignment statement on line %d should
not require parentheses just take a slice of the best_3_players
Tuple. Note that a slice of a Tuple is already a Tuple.''' % line_number

if (len(best_3_players) == 0):
    return '''Assign best_3_players to a new Tuple containing
the three best player names from the elements of the players Tuple,
as directed.'''
if (best_3_players != (players[2], players[0], players[3])):
    return '''You didn't assign best_3_players to a Tuple
containing the best three player names (ordered by their scores).'''

if (len(printed_lines) < 9):
    return '''Send a description of the second best player and
score to the console, as directed.'''

if (best_2_players == best_3_players):
    return '''Assign best_2_players to a slice of the
best_3_players Tuple, as directed.'''
if (best_2_players != best_3_players[:2]):
    return '''You didn't assign best_2_players to a Tuple
containing the best two player names from best_3_players.'''

return True
