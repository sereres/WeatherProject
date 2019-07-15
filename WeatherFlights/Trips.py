import random

class Trip(object):

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
	    
class City(object):

    def __init__(self, name, lattitude, longitude):
        self.name = name
        self.lattitude = lattitude
        self.longitude = longitude
		
class WeatherVars(object):
    
    def __init__(self, var1):
        #start with just one weather variable -- wind speed along flight path
	    self.var1 = var1
		
class FlightTime(object):

    def __init__(self, time):
        # number of minutes off of scheduled arrival
        self.time = time
	
class LinearModel(object):

    def __init__(self, inputvars, intercept, slope):
        #expects weathervars object, two parameters for linear model, returns predicted flight diff time
        self.var1 = inputvars
        self.intercept = intercept
        self.slope = slope
        self.result = intercept + slope * inputvars.var1

class GenerateExpectedTime(object):

    def __init__(self, prediction, sigma):
        #expects weathervars object, model with 2 parameters, and a variable for adding random noise
        self.prediction = prediction
        self.sigma = sigma
        self.result = 180*self.prediction + random.gauss(0, self.sigma)
        #print(self.result)
		

	
	
	
	
	
    	