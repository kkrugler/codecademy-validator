import re
import sys

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
        if (type(expected) == str):
            return check_text(expected, actual, name, False)
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

def get_target_index(line):
    assignment_re = re.compile(r'^[^ \t[]+[ \t]*\[[ \t]*([0-9]+)[ \t]*][ \t]*=.*?$')
    assignment_match = assignment_re.match(line)
    if (assignment_match == None):
        return -1
    return int(assignment_match.groups()[0])

if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (len(scores_string_prediction_1) == 0):
    return '''Predict the string representation of the scores
List after it gets sorted, by setting the scores_string_prediction_1
variable to a String Literal as directed.'''

code_lines = code.splitlines()
line_number = 0
last_default_line_number = sys.maxint
players_copy_indexes = []
scores_copy_indexes = []
for line in code_lines:
    line_number += 1

    if  (   line.startswith('players = [')
        and (line != "players = ['Jane', 'Bob', 'Sally', 'Dave']")):
        return '''It looks like you modified the original
assignment to the players List (or perhaps tried to reassign the
entire List?)  Make only the changes specifically described in
the comments and follow the instructions carefully when doing so.
Click the Reset Code button and start over.'''
    if  (   line.startswith('scores = [')
        and (line != "scores = [6, 2, 7, 5]")):
        return '''It looks like you modified the original
assignment to the scores List (or perhaps tried to reassign the
entire List?)  Make only the changes specifically described in
the comments and follow the instructions carefully when doing so.
Click the Reset Code button and start over.'''
    if  (   line.startswith('players_copy = [')
        and (line != "players_copy = ['Jane', 'Bob', 'Sally', 'Dave']")):
        return '''It looks like you modified the original
assignment to the players_copy List (or perhaps tried to reassign
the entire List?)  Make only the changes specifically described in
the comments and follow the instructions carefully when doing so.
Click the Reset Code button and start over.'''
    if (line.startswith('scores_copy = [')):
        if (line != "scores_copy = [6, 2, 7, 5]"):
            return '''It looks like you modified the original
assignment to the scores_copy List (or perhaps tried to reassign
the entire List?)  Make only the changes specifically described in
the comments and follow the instructions carefully when doing so.
Click the Reset Code button and start over.'''
        last_default_line_number = line_number

    if (len(scores_string_prediction_1) > 0):
        result = check_str_prediction("[7, 6, 5, 2]",
                                      'scores_string_prediction_1',
                                      line)
        if (result != True):
            return result

    if  (   line.startswith('players[')
        or  line.startswith('players_copy[')):
        comment_pos = line.find('#')
        if (comment_pos >= 0):
            line = line[:comment_pos]
        if  (   (line.find("'") > 0)
            or  (line.find('"') > 0)):
            return '''Your assignment statement on line %d seems
to include a String Literal.  Each of your assignment statements
should instead MOVE a single element that came from the same list.
See the assignment statements that sorted players the first time
for examples.''' % line_number

    if (line_number > last_default_line_number):
        if (line.startswith('players[')):
            return '''Your assignment statement on line %d is to
an element of players, but it should be to an element of
players_copy instead.''' % line_number
        if (line.startswith('scores[')):
            return '''Your assignment statement on line %d is to
an element of scores, but it should be to an element of
scores_copy instead.''' % line_number
        if (line.find('players[') > 0):
            return '''Your assignment statement on line %d uses
an element of players, but it should use an element of
players_copy instead.''' % line_number
        if (line.find('scores[') > 0):
            return '''Your assignment statement on line %d uses
an element of scores, but it should use an element of
scores_copy instead.''' % line_number
        if (line.startswith('players_copy[')):
            players_copy_indexes.append(get_target_index(line))
        elif (line.startswith('scores_copy[')):
            scores_copy_indexes.append(get_target_index(line))

    if (len(scores_string_prediction_2) > 0):
        result = check_str_prediction("[2, 5, 6, 7]",
                                      'scores_string_prediction_2',
                                      line)
        if (result != True):
            return result

if (len(players_copy_indexes) == 0):
    if (players == ['Sally', 'Jane', 'Dave', 'Bob']):
        return '''Next, re-sort both the players and their scores
so that LOWER scores (and associated players) appear first in each
List, as directed.'''
    elif (players != ['Bob', 'Dave', 'Jane', 'Sally']):
        return '''Your players aren't arranged correctly so that
those with LOWER scores appear first in this List.'''
    elif (scores != [2, 5, 6, 7]):
        return '''Your scores aren't arranged correctly so that
LOWER scores appear first in this List.'''
    else:
        if (len(scores_string_prediction_2) == 0):
            return '''Next, predict the string representation of
the scores List after it gets re-sorted (to put LOWER scores first),
by setting the scores_string_prediction_2 variable to a String
Literal as directed.'''
    return '''Finally, sort both the players_copy and scores_copy
Lists so that HIGHER scores (and associated players) appear first
in each List, but make sure you do so in a DIFFERENT way than was
done for players and scores the first time, as directed.'''

if (players_copy != ['Sally', 'Jane', 'Dave', 'Bob']):
    return '''Your players_copy elements aren't arranged correctly
so that those with HIGHER scores appear first in this List.'''
elif (scores_copy != [7, 6, 5, 2]):
    return '''Your scores_copy elements aren't arranged correctly
so that HIGHER scores appear first in this List.'''
elif (players_copy_indexes == [0, 2, 3, 1]):
    return '''You used the same sequence of assignment
statements as the one used by the code that sorted players
in this way the first time.  Use a different sequence as directed.'''
elif (scores_copy_indexes == [0, 2, 3, 1]):
    return '''You used the same sequence of assignment
statements as the one used by the code that sorted scores
in this way the first time.  Use a different sequence as directed.'''

return True
