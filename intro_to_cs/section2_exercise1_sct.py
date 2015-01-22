if (type(error) == NameError):
    return '''Did you fix the error in the first print statement?'''
elif (type(error) == SyntaxError):
    return '''The syntax of the program was not valid.
Are all of the variables using legal identifiers?
Did you remember to type your predicted value?'''
elif (error):
    return '''There's an error in the program.
You might want to click the Reset Code button and then start over.'''

if (predicted_num_citrus_fruit != 7):
    return '''Your predicted value for num_citrus_fruit was wrong.'''
return True