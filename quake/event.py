import os
import unittest

class Event:
    """ A class to represent earthquakes. """

    def __init__(self):
        self.time = 0 #TO-DO: Research Python time class
        self.easting = -1
        self.northing = -1
        self.depth = -1
        self.mag = 0
        self.mag_type = 'Mw'
        


class TestEvent(unittest.TestCase):
    """ Unit tests for the Event class. """

    def test_init(self):
        eq = Event()

        self.assertTrue(eq.time == 0)
        self.assertTrue(eq.mag_type == 'Mw')

if __name__ == '__main__':
    unittest.main()