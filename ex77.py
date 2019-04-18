#!/home/wizard/anaconda3/bin/python

"""
Test factorial function

>>> factorial(5)
120

Test with negative value

>>> factorial(-5)
Traceback (most recent call last):
...
ValueError: n    cannot be negative

Test with collection

>>> [factorial(x) for x in range(7)]
[1, 1, 2, ..., 120, 720]
"""

def factorial(n):
    if n < 0:
        raise ValueError('n cannot be negative')
    if type(n) is not int:
        raise TypeError('Type of n must be integer')
    
    if n > 1:
        return n * factorial(n-1)
    return 1

def foo(n):
    """
    Test with 6
    
    >>> foo(6)
    True

    >>> foo(5)
    False

    """
    return (n % 2) == 0


if __name__ == '__main__':
    import doctest
    opts = doctest.DONT_ACCEPT_TRUE_FOR_1 \
           | doctest.ELLIPSIS \
           | doctest.NORMALIZE_WHITESPACE \
           | doctest.IGNORE_EXCEPTION_DETAIL    
    doctest.testmod(verbose=True, optionflags=opts)