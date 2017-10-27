import os
import unittest
import datetime
from mag import Magnitude

class Event:
    """ A class to represent earthquakes. """

    def __init__(self, params):
        """ Init takes a dictionary of parameters to build the object """
        self.time = params.get('time') 
        self.easting = params.get('easting')
        self.northing = params.get('northing')
        self.depth = params.get('depth')
        self.mag = Magnitude({'mag': params.get('mag'), 'mag_type': params.get('mag_type')})
        #self.mag = params.get('mag')
        #self.mag_type = params.get('mag_type')




class TestEvent(unittest.TestCase):
    """ Unit tests for the Event class. """

    def test_init(self):
        params = {'time': datetime.datetime.now(),'easting': -122.4,'northing': 37.8,'depth': 6.3,'mag': 5.43,'mag_type': 'Mw'}
        eq = Event(params)

        self.assertTrue(eq.northing == 37.8)
        self.assertTrue(eq.mag.mag_type == 'Mw')

if __name__ == '__main__':
    unittest.main()