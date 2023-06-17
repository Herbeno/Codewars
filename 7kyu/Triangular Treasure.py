# Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.
# You need to return the nth triangular number. You should return 0 for out of range values:

def triangular(n):
    x = s = 0
    for x in range(0, n + 1):
        s += x
    return s
# or you can do this way
#   return sum(range(n + 1))