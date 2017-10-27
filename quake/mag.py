import unittest

class Magnitude:
    """ A class representing the magnitude of an event. """

    def __init__(self, params):
        self.mag = params.get('mag')
        self.mag_type = params.get('mag_type')
        assert self.mag > 0 and self.mag < 10, "Magnitude must be greater than 0 and less than 10."
        assert self.mag_type in ['Mb', 'Ms', 'Mw'], "Supported magnitude sclaes: Mb, Ms, and Mw."
    

    def __str__(self):
        """ Returns a string representation of a Magnitude object. """
        return ("Magnitude: " + str(self.mag) + "    Magnitude Scale: " + self.mag_type)


    def get_Mw(self):
        """ Returns the moment magnitude of an event. """
        if self.mag_type == 'Mw':
            return self.mag_type
        elif self.mag_type == 'Mb':
            # empirical formula to convert body wave magnitude to moment magnitude
            pass
        elif self.mag_type == 'Ms':
            # Formula from U.S. NRC NUREG-2115 P 3-30
            Mw = (2.654 + 0.334 * self.mag + 0.04 * self.mag * self.mag)
            return Mw
        else:
            print("Unrecognized magnitude scale")




class TestEvent(unittest.TestCase):
    """ Unit tests for the Magnitude class. """

    def test_init(self):
        """ Test initialization. """
        mag = Magnitude({'mag': 7.20,'mag_type': 'Mw'})

        self.assertTrue(mag.mag == 7.2)
        self.assertTrue(mag.mag_type == 'Mw')

if __name__ == '__main__':
    unittest.main()