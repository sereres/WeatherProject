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
        self.origin = "Chicago"
        self.destination = "Atlanta"
        self.Trip = WeatherFlights.Trips.Trip(self.origin, self.destination)
		
    def testOrigin(self):
        self.assertEqual(WeatherFlights.Trips.Trip.origin, "Chicago", "Trips start from Chicago")	
#        self.Trip = WeatherFlights.Trip.Path(self.origin, self.destination)
	
if __name__ == "__main__":
    unittest.main()