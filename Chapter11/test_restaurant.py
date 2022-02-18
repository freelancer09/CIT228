import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        restaurant_name = "Olive Garden"
        cuisine_type = "Italian"
        number_served = 5
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)
    def test_set_number_served(self):
        served = 200
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,200)
    def test_increment_number_served(self):
        served = 10
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,15)

if __name__ == "__main__":
    unittest.main()