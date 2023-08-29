def square(n):
#   print("harry") # if it is not commented then docs will be commented automatically and __doc__ returns none
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__) # it is not comment , it is doc string both are different things , 
# docstring can be visible in output but comments can never be
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

print(add(2,5))
print(add.__doc__)