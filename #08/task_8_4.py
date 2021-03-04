import unittest


'''
p = (a + b + c) * 0.5 - semiperimeter
S = p (p - a)(p - b)(p - c) ** 0.5 - square

Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size
Examples:
triangle = Triangle([3, 3, 3])
Use classes TriangleNotValidArgumentException and TriangleNotExistException
Create class TriangleTest with unittest and subTest() context manager for class Triangle.
test data:
valid_test_data = [((3, 4, 5), 6.0), ((10, 10, 10), 43.30), ((6, 7, 8), 20.33),
                ((7, 7, 7), 21.21), ((50, 50, 75), 1240.19), ((37, 43, 22), 406.99),
                ((26, 25, 3), 36.0), ((30, 29, 5), 72.0), ((87, 55, 34), 396.0),
                ((120, 109, 13), 396.0), ((123, 122, 5), 300.0)
                ]

not_valid_triangle = [(1, 2, 3), (1, 1, 2), (7, 7, 15),
                     (100, 7, 90), (17, 18, 35), (127, 17, 33),
                     (145, 166, 700), (1000, 2000, 1), (717, 17, 7),
                     (0, 7, 7), (-7, 7, 7)
                     ]
for instance: (1, 2, 3) - S=0



not_valid_arguments = [('3', 4, 5), ('a', 2, 3), (7, "str", 7), ('1', '1', '1'),
                     'string', (7, 2), (7, 7, 7, 7), 'str', 10, ('a', 'str', 7)
                      ]
'''


class TriangleNotValidArgumentException(Exception):

    message1 = "Not valid arguments"

    def __init__(self, message1=message1):
        self.message1 = message1

    def __str__(self):
        return self.message1


class TriangleNotExistException(Exception):

    message2 = "Can`t create triangle with this arguments"

    def __init__(self, message2=message2):
        self.message2 = message2

    def __str__(self):
        return self.message2


class Triangle():

    def __init__(self, sides):

        self.sides = sides
        # data error1: (returns False if attr is not tuple or list)
        attr_error_pass = isinstance(self.sides, (list, tuple)) == True
        if not attr_error_pass:
            raise TriangleNotValidArgumentException

        error11_pass = len(self.sides) == 3  # True ### +++
        error12_pass = len(
            [i for i in self.sides if isinstance(i, int) == False]) == 0  # True
        condition_error1_pass = error11_pass == error12_pass != False

        if not condition_error1_pass:
            raise TriangleNotValidArgumentException

        a, b, c = self.sides
        error2_pass = all(
            [a + b > c, a + c > b, b + c > a, a > 0, b > 0, c > 0])
        if not error2_pass:
            raise TriangleNotExistException

    def get_area(self):
        # sides assighnment
        a, b, c = self.sides
        # calculation of semi-perimeter
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        return f'{round(area, 2)}'


class TriangleTest(unittest.TestCase):

    longMessage = True

    # sublist for calculation
    valid_test_data = {
        6.0: (3, 4, 5), 43.30: (10, 10, 10), 20.33: (6, 7, 8),
        21.21: (7, 7, 7), 1240.19: (50, 50, 75), 406.99: (37, 43, 22),
        36.0: (26, 25, 3), 72.0: (30, 29, 5), 396.0: (87, 55, 34),
        300.0: (123, 122, 5)
    }

    # sublist for calculation
    invalid_test_data = {
        10.0: (3, 4, 5), 20.30: (10, 10, 10), 25.33: (6, 7, 8),
        21.35: (7, 7, 7), 1250.19: (50, 50, 75), 416.99: (37, 43, 22),
        58.0: (26, 25, 3), 82.0: (30, 29, 5), 399.0: (87, 55, 34),
        305.0: (123, 122, 5)
    }

    # sublist for Exception: TriangleNotExistException
    not_valid_triangle = [
        (1, 2, 3), (1, 1, 2), (7, 7, 15), (100, 7, 90), (17, 18, 35),
        (127, 17, 33), (145, 166, 700), (1000, 2000, 1), (717, 17, 7),
        (0, 7, 7), (-7, 7, 7)
    ]
    # sublist for Exception: TriangleNotValidArgumentException
    not_valid_arguments = [
        (2, 4, 5), ('a', 2, 3), (7, "str", 7),
        ('1', '1', '1'), 'string', (7, 2),
        (7, 7, 7, 7), 'str', 10, ('a', 'str', 7)
    ]

    # equal ## OK ## OK (10 occureneces)
    def test_valid_data(self):
        for name, (a, b, c) in self.valid_test_data.items():
            p = (a + b + c) / 2
            sq = round(((p*(p-a)*(p-b)*(p-c)) ** 0.5), 1)
            with self.subTest(name=name):
                self.assertEqual(sq, round(name, 1))

    # almost equal ## OK (10 occurences)
    def test_valid_data(self):
        for name, (a, b, c) in self.valid_test_data.items():
            p = (a + b + c) / 2
            sq = round(((p*(p-a)*(p-b)*(p-c)) ** 0.5), 1)
            with self.subTest(name=name):
                delta = 0.01
                self.assertAlmostEqual(sq, round(name, 1), delta)

    # OK bad improper formula
    def test_invalid_data(self):
        for name, (a, b, c) in self.invalid_test_data.items():
            p = (a + b + c) / 2
            sq = round(((p*(p-a)*(p-b)*(p-c)) ** 0.5), 1)
            with self.subTest(name=name):
                self.assertNotEqual(sq, round(name, 1))

    # OK  invalid data type (failures=7, 7 bad items)
    def test_integers(self):
        for tuple_ in self.not_valid_arguments:
            if isinstance(tuple_, (list, tuple)):
                for symbol in tuple_:
                    with self.subTest(symbol=symbol):
                        self.assertTrue(isinstance(symbol, int), True)

            if not isinstance(tuple_, (list, tuple)):
                with self.assertRaises(TriangleNotValidArgumentException):
                    raise TriangleNotValidArgumentException

    # OK bad triangle (failures=11, 11 tuples)
    def test_sidess(self):
        dct = dict(enumerate(self.not_valid_triangle))
        for name, (a, b, c) in dct.items():
            result = all([a + b > c, a + c > b, b +
                          c > a, a > 0, b > 0, c > 0])
            with self.subTest(result=result):
                self.assertTrue(result)


# depicting test launcher
if __name__ == '__main__':
    unittest.main()


# not_valid_triangle = [
#         (1, 2, 3), (1, 1, 2), (7, 7, 15), (100, 7, 90), (17, 18, 35),
#         (127, 17, 33), (145, 166, 700), (1000, 2000, 1), (717, 17, 7),
#         (0, 7, 7), (-7, 7, 7)
#     ]


# tests
# OK
# valid_test_data = [
#     (3, 4, 5),
#     (26, 25, 3),
#     (30, 29, 5),
#     (87, 55, 34),
#     (120, 109, 13),
#     (123, 122, 5)
# ]
# for data in valid_test_data:
#     print(Triangle(data).get_area())

# OK
# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     10
# ]
# for data in not_valid_arguments:
#     try:
#         Triangle(data)
#     except TriangleNotValidArgumentException as e:
#         print(e)

# OK
# not_valid_triangle = [
#     (1, 2, 3),
#     (1, 1, 2),
#     (7, 7, 15),
#     (100, 7, 90),
#     (17, 18, 35),
#     (127, 17, 33),
#     (145, 166, 700),
#     (1000, 2000, 1),
#     (717, 17, 7),
#     (0, 7, 7),
#     (-7, 7, 7)
# ]
# for data in not_valid_triangle:
#     try:
#         Triangle(data)
#     except TriangleNotExistException as e:
#         print(e)

# OK
# # Set1
# # Test1
# triangle = Triangle([3, 4, 5])  # +++ correct 6.0
# print(triangle.get_area())
# # Test2
# triangle = Triangle([26, 25, 3])  # +++ correct 36.0
# print(triangle.get_area())
# # Test3
# triangle = Triangle([30, 29, 5])  # +++ correct 72.0
# print(triangle.get_area())
# # Test4
# triangle = Triangle([87, 55, 34])  # +++ correct  396.0
# print(triangle.get_area())
# Test5
# triangle = Triangle([120, 109, 13])  # +++ correct 396.0
# print(triangle.get_area())
# # ### Test6
# triangle = Triangle([123, 122, 5])  # +++ correct 300.0
# print(triangle.get_area())


# ################ TriangleNotExistException ####################
# Set2
# Test1
# triangle = Triangle([1, 2, 3])  # Triangle Not Exist
# print(triangle.get_area())
# # ### Test2
# triangle = Triangle([1, 1, 2])  # Triangle Not Exist
# print(triangle.get_area())
# # ### Test3
# triangle = Triangle([7, 7, 15])  # Triangle Not Exist
# print(triangle.get_area())
# # ### Test4
# triangle = Triangle([100, 7, 90])  # Triangle Not Exist
# print(triangle.get_area())
# # ### Test5
# triangle = Triangle([17, 18, 35])  # Triangle Not Exist
# print(triangle.get_area())
# # Test6
# triangle = Triangle([127, 17, 33])  # Triangle Not Exist
# print(triangle.get_area())
# # Test7
# triangle = Triangle([145, 166, 700])  # Triangle Not Exist
# print(triangle.get_area())
# # Test8
# triangle = Triangle([1000, 2000, 1])  # Triangle Not Exist
# print(triangle.get_area())
# # Test9
# triangle = Triangle([717, 17, 7])  # Triangle Not Exist
# print(triangle.get_area())
# # Test10
# triangle = Triangle([0, 7, 7])  # Triangle Not Exist
# print(triangle.get_area())
# # Test11
# triangle = Triangle([-7, 7, 7])  # Triangle Not Exist
# print(triangle.get_area())


############### TriangleNotValidArgumentException ###################
# Set3
# # not_valid_arguments
# # Test1 ++++
# triangle = Triangle(['3', 4, 5])  # ++++ Triangle Not Valid Argument
# print(triangle.get_area())

# # Test2 ++++
# triangle = Triangle(['a', 2, 3])  # ++++ Triangle Not Valid Argument
# print(triangle.get_area())

# # ## Test3 +++
# # triangle = Triangle([7, "str", 7])
# # print(triangle.get_area())

# # ## Test4 +++
# # triangle = Triangle(['1', '1', '1'])
# # print(triangle.get_area())

# # Test5 +++
# triangle = Triangle('string')
# print(triangle.get_area())

# # Test6 +++
# triangle = Triangle([7, 2])
# print(triangle.get_area())

# # Test7 +++
# triangle = Triangle([7, 7, 7, 7])
# print(triangle.get_area())

# # ## Test8 +++
# # triangle = Triangle('str')
# # print(triangle.get_area())

# # Test9 +++
# triangle = Triangle(10)
# print(triangle.get_area())

# # ## Test10 +++
# # triangle = Triangle(['a', 'str', 7])
# # print(triangle.get_area())
