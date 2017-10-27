import unittest

class BaseSource:
    """ This is an Abstract Base Class for seismic source based objects. """

    def __init__(self, params):
        self.name = params.get('name')
        self.region = params.get('region')
        self.weight = params.get('weight')
        self.GMPE_Set = params.get('GMPE_Set')


    

class TestEvent(unittest.TestCase):
    """ Unit tests for the Source class. """

    def test_init(self):
        """ Test initialization. """
        pass

if __name__ == '__main__':
    unittest.main()