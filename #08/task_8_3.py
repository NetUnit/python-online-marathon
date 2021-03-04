import math as mt
import unittest


'''
    Write the function quadratic_equation with arguments a, b ,c 
    that solution to quadratic equation without comlex solution.

    Write unit tests for this function with QuadraticEquationTest class

    Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0
'''


def quadratic_equation(a, b, c):

    # in case of str representation of digits
    data = tuple(map(lambda x: int(x), (a, b, c)))
    a = data[0]
    b = data[1]
    c = data[2]

    # value check
    zero_a = a == 0
    if zero_a:
        raise ValueError
    else:
        pass

    # discriminant check
    D = pow(b, 2) - 4 * a * c
    negative_discr = D < 0
    if negative_discr:
        return None
    else:
        pass

    # math for regular numbers
    x2 = (-mt.sqrt(D) - b) / (2 * a)
    x1 = (mt.sqrt(D) - b) / (2 * a)

    if x1 == x2:
        return x1
    else:
        return x1, x2


class QuadraticEquationTest(unittest.TestCase):

    ## D < 0;
    def test_discriminant(self):
        self.assertEqual(quadratic_equation(2, 1, -1), (0.5, -1.0))

    ## D > 0;
    def test_discriminant(self):
        self.assertEqual(quadratic_equation('1', '5', '6'), (-2.0, -3.0))

    ## D == 0;
    def test_discriminant(self):
        self.assertEqual(quadratic_equation(1, -4, 4), (2.0))

    # num of values
    def test_num_values(self):
        self.assertEqual(len(quadratic_equation(1, 7, 2)), 2)

        # num of values
    def test_num_values(self):
        self.assertEqual(len([quadratic_equation(1, -6, 9)]), 1)

    # ValueError = Zero Division Error;
    def test_value_div_by_zero(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 5, 6)

    # Value Error;
    def test_value_type(self):
        with self.assertRaises(ValueError):
            quadratic_equation(1, 'abc', 5)


# TEST1 +++++
# The solution are x1=(-2-0j) and x2=(-3+0j)" # + ok  D < 0
print(quadratic_equation(2, 1, -1))

# TEST2 +++++
# test2 - correct - string representation of number
print(quadratic_equation(1, -4, 4))  # (2.0, 2.0)
# test2 - when D > 0;
# print(quadratic_equation(1, -6, 9))  # (3.0, 3.0)

# TEST3 +++++
print(quadratic_equation(4, 1, 2))  # None

# TEST4 ValueError +++++
# need to raise ValueError if
# ZeroDivisionError
try:
    quadratic_equation(0, 0, 0)
except ValueError:
    print('error')

# need to raise Valueerror

# TEST5 +++++ Value Error
try:
    print(quadratic_equation(1, 'abc', 5))
except ValueError:
    print('error')


# depicting test launcher
if __name__ == '__main__':
    unittest.main()
