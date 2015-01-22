if (error):
    return '''It looks like your program contains an error.
The console window to the right should identify the first line of
your program that Python doesn't like.  Note that you do need
at least one valid Python statement in your program, or it will
complain with an EOF SyntaxError.'''

printed_lines = CC.prints()

if (len(printed_lines) < 1):
    return '''(Not really oops.) Python didn't seem to have any 
problem the code you wrote, but that doesn't mean it's doing
anything particularly interesting. You should probably have it
print text to the console window to prove that your code is
operating as you expect it to.'''

if (not ('is_period_over' in globals())):
    return '''(Not really oops.) Python didn't seem to have any
problem the code you wrote, so check the console output to see
if it's behaving as you expect. Continue to try other things
(and to test them via print) until the end of the class period.'''

return True
