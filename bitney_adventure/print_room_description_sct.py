# Make sure student didn't introduce a syntax error
if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start again."""

printed_lines = CC.prints()
is_found_description = False
is_found_key = False
is_found_donut = False
is_found_hamster = False
for line in printed_lines:
    line = line.strip()
    if (line.find("The hallway is filled with colorful murals. There are doors to the north and east") >= 0):
        is_found_description = True
    if (line.find("key") >= 0):
        is_found_key = True
    if (line.find("donut") >= 0):
        is_found_donut = True
    if (line.find("hamster") >=0):
        is_found_hamster = True

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Use a print statement to do so.'''
elif (not is_found_description):
    return '''You forgot to include the room description.'''
elif    (   (not is_found_key)
        or  (not is_found_donut)
        or  (not is_found_hamster)):
    return '''You forgot to list at least one of the items in the room.'''

return True
