import re

printed_lines = CC.prints()

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

if (len(printed_lines) > 14):
    return '''It looks like you modified the code so that it
sends an unexpected line to the console.
Click the Reset Code button and start over.'''

code_lines = code.splitlines()
line_number = 0
is_in_raise_2_to = False
is_in_log_base_2 = False
is_raise_2_to_uses_while = False
is_log_base_2_uses_while = False
for line in code_lines:
    line_number += 1

    if  (   is_in_raise_2_to
        and (not line.startswith(' '))
        and (not line.startswith('\t'))):
        is_in_raise_2_to = False
    elif    (   line.startswith('def ')
            and (line.find('raise_2_to') > 0)):
        is_in_raise_2_to = True
    if (is_in_raise_2_to):
        if (line.find('**') > 0):
            return '''You cheated on line %d.  Don't use the
exponentiation operator (**) to raise 2 to a power.  Instead,
use repeated multiplication via the while statement as directed.
''' % line_number
        if (line.find('while') > 0):
            is_raise_2_to_uses_while = True

    if  (   is_in_log_base_2
        and (not line.startswith(' '))
        and (not line.startswith('\t'))):
        is_in_log_base_2 = False
    elif    (   line.startswith('def ')
            and (line.find('log_base_2') > 0)):
        is_in_log_base_2 = True
    if (is_in_log_base_2):
        if (line.find('while') > 0):
            is_log_base_2_uses_while = True

if (not is_raise_2_to_uses_while):
    if (exponent == 3):
        return '''Next, modify the definition of the raise_2_to()
function so that it uses the while statement to return 2 raised
to its exponent parameter, as directed.'''
    return '''Your raise_2_to() function should use the while
statement as directed.'''

if (exponent == 3):
    return '''Continue to test your raise_2_to() function using
different exponent values, and checking the result in the console
each time.'''
elif (exponent != 31):
    return '''Continue to test your raise_2_to() function using
different exponent values, and checking the result in the console
each time.  When you're sure it's working properly, set exponent
to 31 to have the SCT test it for you.'''

for exponent_test in range (0, 16):
    expected_result = 2 ** exponent_test
    result = raise_2_to(exponent_test)
    if (result != expected_result):
        return '''Your raise_2_to() function returns %d instead
of %d when its exponent parameter is %d.''' % (result, expected_result, exponent_test)

if (not is_log_base_2_uses_while):
    if (natural_number == 8):
        return '''Next, modify the definition of the log_base_2()
function so that it uses the while statement to return the
exponent of the power of 2 that its natural_number parameter
meets or exceeds, as directed.'''
    return '''Your log_base_2() function should use the while
statement as directed.'''

if (natural_number == 8):
    return '''Continue to test your log_base_2() function using
different natural_number values, and checking the result in the
console each time.'''
elif (natural_number != 65536):
    return '''Continue to test your log_base_2() function using
different natural_number values, and checking the result in the
console each time.  When you're sure it's working properly,
set natural_number to 65536 to have the SCT test it for you.'''

for expected_result in range (0, 16):
    natural_number_test = 2 ** expected_result
    result = log_base_2(natural_number_test)
    if (result != expected_result):
        return '''Your log_base_2() function returns %d instead
of %d when its natural_number parameter is %d.''' % (result, expected_result, natural_number_test)

return True
