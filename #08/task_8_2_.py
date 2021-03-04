import unittest
import string


'''
    You have function divide

    Please, write the code with unit tests for the function "divide":
    minimum 3 tests
    must chek all flows
    all test must be pass
    no failures
    no skip

'''


def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):

    # ZeroDivisionError
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10.0, 0)

    # TypeError - float division to str
    def test_divide_correct_value(self):
        with self.assertRaises(TypeError):
            divide(10.0, 'abc')

    ## TypeError - num of Values
    def test_divide_correct_value(self):
        with self.assertRaises(TypeError):
            divide(10.0, 15, 'abc')

    # ValueError - convert str to float 
    def test_divide_correct_value(self):
        with self.assertRaises(ValueError):
            divide('abc', 5)
    
    ## reg digits first is float
    def test_divide(self):
        self.assertEqual(divide(10.0, 5), 2.0)

    ## reg digits second is float
    def test_divide(self):
        self.assertEqual(divide(10, 5.0), 2.0)

    # both integers
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2.0)


## Test1 +++
##  ZeroDivisionError - division by zero
# try:
#     divide(10.0, 0) # >>> True
# except ZeroDivisionError:
#     print ('division by zero')

# Test2
# ## Type - float division to str
# try:
#     divide(10.0, 'abc')
# except TypeError:
#     print(' float division to str')

# # Test3
# ## Type - number of Values
# try:
#     divide(1, 'abc', 5)
# except TypeError:
#     print('num of values')

# #######
# ## Test4 +++
# # notIsInsatnce
# try:
#     divide(10, '5')
# except TypeError:
#     'unsupported operand type(s) for /: float and str'
# ###########

# Test5
# try:
#     divide('abc', 5)
# except ValueError:
#     print('could not convert string to abc')

#### regular division
## Test6 +++
# divide(10.0, 5)

## Test7 +++
# divide(10, 5.0)

## Test8 +++ 2.0
# divide(10, 5) 

## Test9 +++ 
# divide(float('10.0'), 5)


# depicting test launcher
if __name__ == '__main__':
    unittest.main()

