# The backslash symbol (\) is the line continuation character.

print "This statement extends \
across five physical source code lines, \
but the line breaks (and backslash symbols) \
are ignored by Python. Note the importance \
of the space before each backslash symbol."

print 'Text strings can be delimited'
print "with either type of quotation mark."

print 'Single quotation marks are preferred,'
print "but double quotation marks make contractions"
print "much easier, don't you think?"
print 'You\'d have to "escape" the apostrophe otherwise.'

# Did I mention that the backslash symbol (\) also defeats the
# special nature of the next character (known as "escaping" that
# character)?  Note that when it appears at the end of a line,
# it actually escapes the new line character.

'''Three single quote marks can allow text to
span multiple lines even more naturally.'''

# They can also make it easy to quickly "comment out" a section
# of code.
'''
print 'This code has been "commented out"
so the syntax errors, etc. aren't really a problem
x = 1/0
'''

print """Three double quote marks are
just as good."""

is_period_over = True
