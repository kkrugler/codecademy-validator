if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (not ('is_period_over' in globals())):
    return '''(Not really oops.) Python didn't seem to have any
problem the code you wrote, but that doesn't necessarily mean
that it's doing what was intended.  Have another look
over the description of what it's supposed to do.
If you're confident about your code, call Mr. Schneider over to
have a look.'''

return True
