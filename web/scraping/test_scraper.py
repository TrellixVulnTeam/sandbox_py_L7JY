import unittest
import scraper


class ScraperTest(unittest.TestCase):
    def test_extract_displacement(self):
        displacement = scraper.extract_displacement(
            'something 70.0 cubic inches')
        self.assertEqual(70, displacement)


if __name__ == '__main__':
    unittest.main()
