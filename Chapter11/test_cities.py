import unittest 
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = get_formatted_city("traverse city","united states")
        self.assertEqual(formatted_city,"Traverse City, United States")
    def test_city_country_population(self):
        formatted_city = get_formatted_city("traverse city","united states",10000)
        self.assertEqual(formatted_city,"Traverse City, United States - population 10000")

if __name__ == "__main__":
    unittest.main()