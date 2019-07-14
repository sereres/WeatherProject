import unittest
import WeatherFlights.Trips

class TripTest(unittest.TestCase):
    def testTests(self):
        pass
		
    def setUp(self):
        self.originName = "Chicago"
        self.originLatt = 41.8781
        self.originLong = 87.6298
        self.destinationName = "Atlanta"
        #self.destinationLatt = 33.7490
        #self.destinationLong = 84.3880
        self.aTrip = WeatherFlights.Trips.Trip(self.originName, self.destinationName)
        self.aCity = WeatherFlights.Trips.City(self.originName, self.originLatt, self.originLong)
		
    def testOrigin(self):
        self.assertEqual(self.aTrip.origin, self.originName, "Trips origin set")	
		
    def testPath(self):
        self.assertNotEqual(self.aTrip.origin, self.aTrip.destination, "Trip must have some length")
		
    def testCity(self):
        self.assertEqual(self.aCity.lattitude, self.originLatt, "city lattitude set")

		
if __name__ == "__main__":
    unittest.main()