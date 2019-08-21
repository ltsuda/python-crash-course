import unittest
from city_function import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_country(self):
        """Does 'city' and 'country' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile.')

    def test_city_country_population(self):
        """Does 'city, country - population' work?"""
        formatted_city = get_formatted_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000.')

if __name__ == '__main__':
    unittest.main()
