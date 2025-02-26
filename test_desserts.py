import unittest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

class TestDessertItem(unittest.TestCase):
    def test_default_values(self):
        item = DessertItem()
        self.assertEqual(item.name, "")

    def test_initialized_values(self):
        item = DessertItem("Brownie")
        self.assertEqual(item.name, "Brownie")

    def test_update_values(self):
        item = DessertItem()
        item.name = "Cake"
        self.assertEqual(item.name, "Cake")

class TestCandy(unittest.TestCase):
    def test_default_values(self):
        candy = Candy()
        self.assertEqual(candy.name, "")
        self.assertEqual(candy.candy_weight, 0.0)
        self.assertEqual(candy.price_per_pound, 0.0)

    def test_initialized_values(self):
        candy = Candy("Gummy Bears", 2.5, 3.99)
        self.assertEqual(candy.name, "Gummy Bears")
        self.assertEqual(candy.candy_weight, 2.5)
        self.assertEqual(candy.price_per_pound, 3.99)

    def test_update_values(self):
        candy = Candy()
        candy.name = "Chocolate"
        candy.candy_weight = 1.2
        candy.price_per_pound = 5.50
        self.assertEqual(candy.name, "Chocolate")
        self.assertEqual(candy.candy_weight, 1.2)
        self.assertEqual(candy.price_per_pound, 5.50)

class TestCookie(unittest.TestCase):
    def test_default_values(self):
        cookie = Cookie()
        self.assertEqual(cookie.name, "")
        self.assertEqual(cookie.cookie_quantity, 0)
        self.assertEqual(cookie.price_per_dozen, 0.0)

    def test_initialized_values(self):
        cookie = Cookie("Chocolate Chip", 12, 4.99)
        self.assertEqual(cookie.name, "Chocolate Chip")
        self.assertEqual(cookie.cookie_quantity, 12)
        self.assertEqual(cookie.price_per_dozen, 4.99)

    def test_update_values(self):
        cookie = Cookie()
        cookie.name = "Oatmeal Raisin"
        cookie.cookie_quantity = 6
        cookie.price_per_dozen = 3.75
        self.assertEqual(cookie.name, "Oatmeal Raisin")
        self.assertEqual(cookie.cookie_quantity, 6)
        self.assertEqual(cookie.price_per_dozen, 3.75)

class TestIceCream(unittest.TestCase):
    def test_default_values(self):
        ice_cream = IceCream()
        self.assertEqual(ice_cream.name, "")
        self.assertEqual(ice_cream.scoop_count, 0)
        self.assertEqual(ice_cream.price_per_scoop, 0.0)

    def test_initialized_values(self):
        ice_cream = IceCream("Vanilla", 3, 1.50)
        self.assertEqual(ice_cream.name, "Vanilla")
        self.assertEqual(ice_cream.scoop_count, 3)
        self.assertEqual(ice_cream.price_per_scoop, 1.50)

    def test_update_values(self):
        ice_cream = IceCream()
        ice_cream.name = "Strawberry"
        ice_cream.scoop_count = 2
        ice_cream.price_per_scoop = 2.25
        self.assertEqual(ice_cream.name, "Strawberry")
        self.assertEqual(ice_cream.scoop_count, 2)
        self.assertEqual(ice_cream.price_per_scoop, 2.25)

class TestSundae(unittest.TestCase):
    def test_default_values(self):
        sundae = Sundae()
        self.assertEqual(sundae.name, "")
        self.assertEqual(sundae.scoop_count, 0)
        self.assertEqual(sundae.price_per_scoop, 0.0)
        self.assertEqual(sundae.topping_name, "")
        self.assertEqual(sundae.topping_price, 0.0)

    def test_initialized_values(self):
        sundae = Sundae("Hot Fudge Sundae", 2, 1.75, "Hot Fudge", 1.25)
        self.assertEqual(sundae.name, "Hot Fudge Sundae")
        self.assertEqual(sundae.scoop_count, 2)
        self.assertEqual(sundae.price_per_scoop, 1.75)
        self.assertEqual(sundae.topping_name, "Hot Fudge")
        self.assertEqual(sundae.topping_price, 1.25)

    def test_update_values(self):
        sundae = Sundae()
        sundae.name = "Caramel Sundae"
        sundae.scoop_count = 3
        sundae.price_per_scoop = 2.00
        sundae.topping_name = "Caramel"
        sundae.topping_price = 1.50
        self.assertEqual(sundae.name, "Caramel Sundae")
        self.assertEqual(sundae.scoop_count, 3)
        self.assertEqual(sundae.price_per_scoop, 2.00)
        self.assertEqual(sundae.topping_name, "Caramel")
        self.assertEqual(sundae.topping_price, 1.50)

if __name__ == '__main__':
    unittest.main()
