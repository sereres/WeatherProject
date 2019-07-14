import unittest
#import WeatherFlights.Trip

class TripTest(unittest.TestCase):
    def testTests(self):
        pass
		
    def testTrip(self):
        self.origin = "Chicago"
        self.destination = "Atlanta"
        self.assertNotEqual(self.origin, self.destination, 
                            "Trip must have some length")
		
#        self.Trip = WeatherFlights.Trip.Path(self.origin, self.destination)
	
if __name__ == "__main__":
    unittest.main()