import unittest

class GeoPoint():
    """ An abstract base class to represent a location on Earth. """

    def __init__(self):
        self.easting
        self.northing
        self.depth


    
class TestEvent(unittest.TestCase):
    """ Unit tests for the GeoPoint class. """

    def test_init(self):
        self.assertTrue(0 == 0)
        self.assertFalse(42 == 'Mw')

if __name__ == '__main__':
    unittest.main()