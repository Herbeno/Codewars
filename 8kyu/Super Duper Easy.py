 # Make a function that returns the value multiplied by 50 and increased by 6. if the value entered is a string shold return "Error".
def problem(a):
    if (type(a)) == int or (type(a)) == float:
        f = (a * 50) + 6   
        return f
    else:
        return "Error"