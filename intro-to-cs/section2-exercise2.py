# Most programming languages refer to arbitrary
# runs of text as "strings", and Python has a
# data type for them called a String.
# The following assignment statement puts the 
# String "Hello, world!" into a variable named
# salutation.

salutation = "Hello, world!"

# You can ask Python to print the contents of
# a String variable in the same way we've been
# asking it to print Integer variables.
# The following statement will display the text
# "Hello, world!" to the user via the console.

print salutation

# You can even ask Python to return the type of a
# variable.  The following displays somewhat
# cryptic text to the console describing the
# String data type.

print type(salutation)

# Here's what the Integer type looks like.
# Note that you can get the type of a variable
# or of a raw piece of data like the following.

print type(1)

# There are many things you can do with a 
# String that are impossible to do with simpler
# data types, such as return the number of
# characters in it.  Try to guess what the
# following statement will display in the
# console.

print len(salutation)

# As mentioned, Python lets you stuff whatever
# you like into a variable, even if this
# changes the type of that variable.

salutation = "Hello, duck"
print salutation

# However, it's difficult to write code without
# having at least some expectations about the 
# type of each variable.  Trying to get the
# length of an Integer doesn't make sense,
# so the following statement generates a
# TypeError (even though it worked just fine 
# before we changed the value of this variable).
# Note how the TypeError in the console refers
# to the line below (which expects the variable
# to have a length like a String).

print len(salutation)
