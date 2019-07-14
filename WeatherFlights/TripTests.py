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
        self.destinationLatt = 33.7490
        self.destinationLong = 84.3880
        self.aTrip = WeatherFlights.Trips.Trip(self.originName, self.destinationName)
        self.aCity = WeatherFlights.Trips.City(self.originName, self.originLatt, self.originLong)
        self.aCity2 = WeatherFlights.Trips.City(self.destinationName, self.destinationLatt, self.destinationLong)		
        self.aCityTrip = WeatherFlights.Trips.Trip(self.aCity, self.aCity2)
        self.interceptVal = 0
        self.slopeVal = .001
        self.var1 = 20
        self.ModelTime = WeatherFlights.Trips.LinearModel(self.var1,self.interceptVal,self.slopeVal)
		
		
    def testOrigin(self):
        self.assertEqual(self.aTrip.origin, self.originName, "Trips origin set")	
		
    def testPath(self):
        self.assertNotEqual(self.aTrip.origin, self.aTrip.destination, "Trip must have some length")
		
    def testCity(self):
        self.assertEqual(self.aCity.lattitude, self.originLatt, "city lattitude set")
		
    def testCityTrip(self):
        self.assertEqual(self.aCityTrip.origin.name, self.aCity.name, "test trips between cities")
		
    def testLinearModel(self):
        self.assertEqual(self.ModelTime.result, .02, "Test Simple Model Prediction")
		
    		
	

		
if __name__ == "__main__":
    unittest.main()