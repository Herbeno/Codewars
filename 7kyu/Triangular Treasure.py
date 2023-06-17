# Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.
# You need to return the nth triangular number. You should return 0 for out of range values:

def triangular(n):
    return n * (n + 1) // 2 if n > 0 else 0
# if you do it with a integer division(//) your code cell will be better, because quotient is rounded to he next smallest whole number, the result always has type int.