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

    def __init__(self, var1, intercept, slope):
        self.var1 = var1
        self.intercept = intercept
        self.slope = slope
        self.result = intercept + slope * var1

#class GenerateExpectedTime(object):

#    def __init__(self, inputvars, model)
	
	
	
	
	
    	