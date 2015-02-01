if error and (type(error) == SyntaxError):
    if code.find("bug.") > 0:
        message = """It's not important to include a period
at the end of each sentence, because this isn't an English class
(it's a Python class).
However, the """
    else:
        message = "The "
    message += """text you are trying to display must have the same kind of
    quotation mark at both the beginning and the end."""
    return message
return True
