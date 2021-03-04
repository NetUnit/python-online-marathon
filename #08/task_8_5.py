import unittest


'''
    Write the programm that calculate total 
    price with discount by the products.

    Use class Product(name, price, count) and class Cart. 
    In class Cart you can add the products.

    Discount depends on count product:

    count	discount
    at least 5	5%
    at least 7	10%
    at least 10	20%
    at least 20	30%
    more than 20	50%
    Write unittest with class CartTest and test all methods with logic
 
    NOTE: The unittest module has decorators that can be applied to selected 
    test methods to control their handling as shown in the code given below.

    Problem here also is:
        - skip or mark selected tests as an 
        anticipated failure in the unit tests
'''


class Worker:

    def __init__(self, name, salary=0):
        self.salary = salary

    def get_tax_value(self):

        taxrate = []
        gradation = {0: 1000, 0.1: 3000, 0.15: 5000, 0.21: 10000,
                     0.30: 20000, 0.40: 50000, 0.47: 200000000000}

        if self.salary in range(0, 1001):
            return float(sum(taxrate))
        elif self.salary < 0:
            raise ValueError

        for i in range(len(gradation)):

            if i == len(gradation) + 1:
                return sum(taxrate)

            value = self.salary - list(gradation.values())[i+1]

            if value >= 0:
                tax = (list(gradation.values())[
                       i+1] - list(gradation.values())[i]) * list(gradation.keys())[i+1]
                taxrate.append(tax)

            if not value >= 0:
                last_value = self.salary - list(gradation.values())[i]
                border_tax = last_value * list(gradation.keys())[i+1]
                taxrate.append(border_tax)
                return sum(taxrate)

            else:
                pass

        return sum(taxrate)


class WorkerTest(unittest.TestCase):

    # skipping isn't necessary
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # creating false statement
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, 'broken')

    def setUp(self):
        self.check1 = Worker('Vasia', 900)  # +++ 0.0
        self.check2 = Worker('Vasia', 1500)  # +++ 50.0
        self.check3 = Worker('Vasia', 4200)  # +++ 380.0
        self.check4 = Worker('Vasia', 8750)  # +++ 1287.5
        self.check5 = Worker('Vasia', 16500)  # +++ 3500.0
        self.check6 = Worker('Vasia', 47000)  # +++ 15350.0
        self.check7 = Worker('Vasia', 80000)  # +++ 30650.0
        self.check8 = Worker('Vasia', 120000)  # +++ 49450.0

    # 0-1000

    def test_salary(self):
        self.assertEqual(self.check1.get_tax_value(), 0.0, 'Correct Tax')  # OK

    # 1000-3000
    def test_salary(self):
        self.assertEqual(self.check2.get_tax_value(),
                         50.0, 'Correct Tax')  # OK

    # 3000-5000
    def test_salary(self):
        self.assertEqual(self.check3.get_tax_value(),
                         380.0, 'Correct Tax')  # OK

    # 5000-10 000
    def test_salary(self):
        self.assertEqual(self.check4.get_tax_value(),
                         1287.50, 'Correct Tax')  # OK

    # 10 000 - 20 000
    def test_salary(self):
        self.assertEqual(self.check5.get_tax_value(),
                         3500.0, 'Correct Tax')  # OK

    # 20 000 - 50 000
    def test_salary(self):
        self.assertEqual(self.check6.get_tax_value(),
                         15350.0, 'Correct Tax')  # OK

    # 50 000 - 100 000 (80 000)
    def test_salary(self):
        self.assertEqual(self.check7.get_tax_value(),
                         30650.0, 'Correct Tax')  # OK

    # > 100 000 (120 000)
    def test_salary(self):
        self.assertEqual(self.check8.get_tax_value(),
                         49450.0, 'Correct Tax')  # OK

    def tearDown(self):
        self.check1 = None
        self.check2 = None
        self.check3 = None
        self.check4 = None
        self.check5 = None
        self.check6 = None
        self.check7 = None
        self.check8 = None


# depicting test launcher
if __name__ == '__main__':
    unittest.main()

# Test1 +++
# print(count_tests > 1) ## >>> True

# Test2 +++
# print(failures) ## >>> 0

# Test3 +++
# print(expectedFailures) ## >>> 1

# # test4 +++
# worker = Worker("Vasia")
# print(worker.get_tax_value())

# # test5 +++ 0
# print(failures)

# # test6 +++
# print(expectedFailures) 1

# # test7 +++  ## 0.0
# worker = Worker("Vasia")
# print(worker.get_tax_value())

# # # test8 +++   ## 0.0
# worker = Worker("Petia", 1000) ## 0.0
# print(worker.get_tax_value())

# # # test9 +++   ## 0.1
# worker = Worker("Natasha", 1001) ## 0.1
# print(worker.get_tax_value())

# worker = Worker("Vika", 100000) ## 40050.0
# print(worker.get_tax_value())
