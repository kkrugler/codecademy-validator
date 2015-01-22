import re

# Make sure student didn't introduce a syntax error
if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start again."""


def check_comment(lines, i):
    '''Make sure there is a non-trivial comment on line[i]'''
    commented_line_re = re.compile(r'^[^#]+#.*$')
    empty_commented_line_re = re.compile(r'^[^#]+#[ \t]*$')
    better_commented_line_re = re.compile(r'^[^#]+ #.*$')
    if not commented_line_re.match(lines[i]):
        return """It doesn't look like you have a valid comment
on line %d.""" % (i+1)
    elif empty_commented_line_re.match(lines[i]):
        return """Please add a little more substance to your
comment on line %d.""" % (i+1)
    elif not better_commented_line_re.match(lines[i]):
        return """Although it's not absolutely necesssary,
your code will be a little easier to read if you include
a space in between the end of the statement and the hash symbol
on line %d.""" % (i+1)
    else:
        return True

def check_multi_line_comment(lines):
    '''Make sure there are at least two comment-only lines
after line 20.'''
    comment_line_re = re.compile(r'^#.*$')
    empty_comment_line_re = re.compile(r'^#[ \t]*$')
    num_comment_lines = 0
    for i in range(20, len(lines)):
        if comment_line_re.match(lines[i]):
            num_comment_lines += 1
        if empty_comment_line_re.match(lines[i]):
            return """Please add a little more substance to your
comment on line %d.""" % (i+1)
    if (num_comment_lines < 1):
        return """There are no comment lines after line 20."""
    elif (num_comment_lines < 2):
        return """There is only one comment line after line 20.  
Your comment there should span multiple physical lines,
where each line begins with a hash symbol."""
    else:
        return True
    
lines = code.splitlines()

for i in (5, 20):
    result = check_comment(lines, i-1)
    if (result != True):
        return result

result = check_multi_line_comment(lines)
if (result != True):
    return result
    
return True