import string
import math as mt
import cmath as cm


'''
    Write  the function solve_quadric_equation(a, b, c) the three input
     parameters of which are numbers. The function should return 
    the solution of quadratic equation ax2+bx+c=0, where coefficients 
    a, b, c are input parameters of  the function solve_quadric_equation:

    in case of correct data the function should displayed the corresponding
     message – "The solution are x1=… and x2=…"

    in the case of division by zero the function should displayed the 
    corresponding message – "Zero Division Error" 

    in the case of incorrect data the function should displayed the message –
    "Could not convert string to float"
    Note: in the function you must use the "try except" construct.

    NOTE: in a case of D < 0: when using math module - 'ValueError: math domain error'
    will be raised, so that we need to import cmath
'''


def solve_quadric_equation(a, b, c):

    try:
        # in case of str represantation of digits
        data = tuple(map(lambda x: int(x), (a, b, c)))
        a = data[0]
        b = data[1]
        c = data[2]

        # cmath for complex numbers
        x1 = (-cm.sqrt(pow(b, 2) - 4 * a * c) - b) / (2 * a)
        x2 = (cm.sqrt(pow(b, 2) - 4 * a * c) - b) / (2 * a)
        return f'The solution are x1={x1} and x2={x2}'

    except ZeroDivisionError:
        return 'Zero Division Error'
    except (TypeError, ValueError):
        return 'Could not convert string to float'

# ValueError: math domain error

# test Soft Serve
# test1 - correct
# print(solve_quadric_equation(1, 4, 5)) # The solution are x1=(-2-0j) and x2=(-3+0j)" # + ok

# test2 - correct - string representation of number
# print(solve_quadric_equation('1', '5', '6')) # The solution are x1=(-2-0j) and x2=(-3+0j)" # + ok

# test3 - incorrect
# print(solve_quadric_equation(0, 5, 6)) # ZeroDivisionerror # + ok

# test4 - incorrect
# print(solve_quadric_equation('0', '8', '1')) #Zero Division Error" because a could not be 0 # + ok

# test5 - incorrectstr input letters
# print(solve_quadric_equation(1, 'abc', 5)) # ValueError "Could not convert string to float" # + ok

# test6 - incorrect input improper data
# print(solve_quadric_equation([0], '8', '1')) # TypeError # + ok

# test7
# print(solve_quadric_equation('4', op, 'abc')) # NameError: name 'op' is not defined # + ok

# test8 case when D < 0
# print(solve_quadric_equation(5, 2, 12)) # The solution are x1=(-0.2+1.5362291495737215j) and x2=(-0.2-1.5362291495737215j) + ok

# when using math module - ValueError: math domain error (need cmath)
# a = -236 - D when a, b, c are 5, 12, 12
# print(pow(a, 0.5))
