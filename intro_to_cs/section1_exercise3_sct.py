if (error):
    return '''Your program has an error in it. The cryptic
message in the window to the right identifies the first statement
of your code that Python didn't like. Each line of code should be
either a valid print statement, a comment, or a blank line.
There needs to be at least one valid statement in your program
or Python will complain when it reaches the end of it
(EOF stands for "end of file".)'''

printed_lines = CC.prints()

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Make sure you have three valid print statements.'''
elif (printed_lines[0] != "Hello, world!"):
    return '''The very first line you displayed doesn't seem to
match the directions (at least not precisely, including all
punctuation, etc.)'''
elif (len(printed_lines) < 2):
    return '''Your program only displayed one line of text
to the user. Make sure you have three valid print statements.'''
elif (printed_lines[1] != "It's nice to have you here with me."):
    return '''The second line you displayed doesn't seem to
match the directions (at least not precisely, including all
punctuation, etc.)'''
elif (len(printed_lines) < 3):
    return '''Your program only displayed two lines of text
to the user. Make sure you have three valid print statements.'''
elif (printed_lines[2] != "Take it easy, pal."):
    return '''The third line you displayed doesn't seem to
match the directions (at least not precisely, including all
punctuation, etc.)'''
elif (len(printed_lines) > 3):
    return '''Your program displayed too many lines of text
to the user. It should display exactly three lines.'''

code_lines = code.splitlines()
is_has_comment_line = False
num_print_statements = 0
for i in range(len(code_lines)):
    if code_lines[i].startswith('print'):
        if is_has_comment_line:
            num_print_statements += 1
            is_has_comment_line = False
        else: return '''The print statement on line %d
is missing a preceding comment line.''' % (i+1)
    elif code_lines[i].startswith('#'):
        is_has_comment_line = True

return True
