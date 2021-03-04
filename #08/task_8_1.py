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

    NOTE: Do the Cart - updatable dict
    update automatically when adding new product.

    alter Cart with remove/add item
'''


class Product:

    def __init__(self, name=0, price=0, count=0):
        self.name = name
        self.price = price
        self.count = count


class Cart(Product):

    def __init__(self, products=0):
        self.product = products
        if len(self.product) != 0:
            self.product = products
        else:
            self.product = 0

    def get_total_price(self):

        dct = {}
        for i in range(len(self.product)):
            dct[self.product[i].price] = self.product[i].count

        lst = []

        for key, value in dct.items():
            item = value * key

            if value in tuple(range(1, 5)):
                lst.append(item)

            if value in tuple(range(5, 7)):
                lst.append(item*0.95)

            if value in tuple(range(7, 10)):
                lst.append(item*0.9)

            if value in tuple(range(10, 20)):
                lst.append(item*0.8)

            if value == 20:
                lst.append(item*0.7)

            if value > 20:
                lst.append(item*0.5)

        return sum(lst)


class CartTest(unittest.TestCase):

    # skipped in test
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # skipped in test
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, 'broken')

    def setUp(self):
        self.check1 = Product('p1', 10, 4)
        self.check2 = Product('p2', 100, 5)
        self.check3 = Product('p3', 200, 6)
        self.check4 = Product('p4', 300, 7)
        self.check5 = Product('p5', 400, 9)
        self.check6 = Product('p6', 500, 10)
        self.check7 = Product('p7', 1000, 20)

        self.check8 = Cart((self.check1, self.check2, self.check3))
        self.check9 = Cart((self.check4, self.check5, self.check6))
        self.check10 = Cart((self.check1, self.check2, self.check3,
                             self.check4, self.check5, self.check6, self.check7))

    def test_cart(self):
        self.assertEqual(self.check8.get_total_price(),
                         1655.0, 'Correct')

    def test_cart(self):
        self.assertEqual(self.check8.get_total_price(),
                         1655.0, 'Correct')

    def test_cart(self):
        self.assertEqual(self.check9.get_total_price(),
                         9130.0, 'Correct')

    def test_cart(self):
        self.assertEqual(self.check10.get_total_price(),
                         24785.0, 'Correct')

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
