import unittest
import WeatherFlights.Trips

class TripTest(unittest.TestCase):
    def testTests(self):
        pass
		
    def testTrip(self):
        self.origin = "Chicago"
        self.destination = "Atlanta"
        self.assertNotEqual(self.origin, self.destination, 
                            "Trip must have some length")
		
    def setTrip(self):
        self.originName = "Chicago"
        self.destinationName = "Atlanta"
        self.aTrip = WeatherFlights.Trips.Trip(self.originName, self.destinationName)
		
    def testOrigin(self):
        self.assertEqual(self.aTrip.origin, self.DestinationName, "Trips start from Chicago")	
#        self.Trip = WeatherFlights.Trip.Path(self.origin, self.destination)
	
if __name__ == "__main__":
    unittest.main()