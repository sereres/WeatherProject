import unittest
import WeatherFlights.Trips

class TripTest(unittest.TestCase):
    def testTests(self):
        pass
		
    def testTrip(self):
        self.TripOrigin = "Chicago"
        self.TripDestination = "Atlanta"
        self.assertNotEqual(self.TripOrigin, self.TripDestination, 
                            "Trip must have some length")
		
    def setUp(self):
        self.originName = "Chicago"
        self.destinationName = "Atlanta"
        self.aTrip = WeatherFlights.Trips.Trip(self.originName, self.destinationName)
		
    def testOrigin(self):
        self.assertEqual(self.aTrip.origin, self.originName, "Trips origin set")	
	
if __name__ == "__main__":
    unittest.main()