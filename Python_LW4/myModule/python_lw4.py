import doctest
import myModule

"""
# parašyti funkciją apskaičiuojančią n-ąjį Fibonačio skaičių

>>> get_fibonacci_nth_nm(8)
13
>>> get_fibonacci_nth_nm(-1)
-1
"""

def get_fibonacci_nth_nm(n):
    if n <= 0:
        return -1
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return get_fibonacci_nth_nm(n-1)+get_fibonacci_nth_nm(n-2)

doctest.testmod()

# status = spam.system("ls ;l")