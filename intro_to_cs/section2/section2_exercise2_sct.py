printed_lines = CC.prints()

if (type(error) == TypeError):
    return '''This is an example of what's called a "runtime error",
and runtime errors are more common with duck typing.
Review the TypeError information in the console carefully so that
you'll recognize this kind of problem in the future.
Next, follow the instructions to avoid the problem
without modifying the line of code that Python is complaining
about.'''

if (error):
    return '''Your change introduced some other error.
Check the output in the console to see if you can resolve it.
Otherwise, just click the Reset Code button to start over.'''

if (len(printed_lines) < 1):
    return '''Your program didn't display any text to the user.
Click the Reset Code button and start over.'''

if (printed_lines[-1] != "11"):
    return '''The final print statement didn't display the requested
output via the console.'''

code_lines = code.splitlines()
for i in range(len(code_lines)):
    code_line = code_lines[-i-1]
    if (code_line.find("print") >= 0):
        if (code_line == "print len(salutation)"):
            return True
        else:
            break

return '''You modified or deleted the final print
statement.  Click the Reset Code button and start over.'''
