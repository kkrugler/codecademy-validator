# Make sure student didn't introduce a syntax error
if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start again."""

printed_lines = CC.prints()
num_printed_chars = 0
is_found_score = False
for line in printed_lines:
    num_printed_chars += len(line)
    if (line.find("42") >= 0):
        is_found_score = True

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Use a print statement to do so.'''
elif (num_printed_chars < 20):
    return '''You only displayed a total of %d characters.
You can do better than that.  Get creative!''' % num_printed_chars
elif (not is_found_score):
    return '''You forgot to tell the user what his/her score was.'''

return True
