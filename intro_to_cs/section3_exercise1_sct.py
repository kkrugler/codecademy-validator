if (error):
    return """You broke the code with your changes so that it is
no longer valid Python syntax.  The cryptic error message to the
right will identify the first line that Python didn't like.
You can try to fix the error you introduced, or just click the
Reset Code button and start over."""

if (true_condition_count != true_condition_count_prediction):
    return '''Your predicted value for true_condition_count was wrong.'''

if (printed_line_count != printed_line_count_prediction):
    return '''Your predicted value for printed_line_count was wrong.'''

return True
