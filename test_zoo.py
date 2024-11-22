import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    # Equivalence
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(40), 150)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

    # Boundary - low
    def test_child_low_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    
    def test_teen_low_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_adult_low_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    # Boundary - high
    def test_child_high_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    
    def test_teen_high_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_high_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_senior_high_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()