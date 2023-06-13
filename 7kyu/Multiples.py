#  Make a program thet takes a value (x) and returns "Bang" if the number is divisible by 3, "Boom" if it is divisible by 5, "BangBoom" if it is divisible by 3 and 5, and "Miss" if it isn't divisible by any  of them. You program shold onlu return one value.
def multiple(x):
    # we will use "if" to make a condition for our code and we describe the conditions. First the condition that says that return "Bang" if "x" is divisible by 3 'and' isn't divisible by 5.
    # to know if the number is divisible, we will use '%', that return the rest of division.
    if x % 3 == 0 and x % 5 != 0:
        return "Bang"
    # next, we will use "elif" to code other condition that return "Boom" if x is divisible by 5 'and' in't divisible by 3.
    elif x % 5 == 0 and x % 3 != 0:
        return "Boom"
    # The last comand is 'else', that means that any other possibility of division return 'Miss'
    else:
        return "Miss"
    