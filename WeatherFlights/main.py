import WeatherFlights.Trips
import random
import msvcrt as m
import matplotlib.pyplot as plt
import numpy as NP

def Make100Times():
    whole = []	
    slope = .001
    intercept = 0
    sigma = 1
    for i in range(100):
        indepvar = random.randint(-50,50)
        weathervar = WeatherFlights.Trips.WeatherVars(indepvar)			
        dependvar = WeatherFlights.Trips.LinearModel(weathervar,intercept,slope)
        print(dependvar.result)		
        outputtime = WeatherFlights.Trips.GenerateExpectedTime(dependvar.result,sigma)
        whole.append(outputtime.result)			
    return whole
	
def Make100DataPoints():
    whole = []	
    slope = .001
    intercept = 0
    sigma = 1
    for i in range(100):
        point = []	
        indepvar = random.randint(-50,50)
        weathervar = WeatherFlights.Trips.WeatherVars(indepvar)			
        dependvar = WeatherFlights.Trips.LinearModel(weathervar,intercept,slope)
        print(dependvar.result)		
        outputtime = WeatherFlights.Trips.GenerateExpectedTime(dependvar.result,sigma)
        point.append(indepvar)
        point.append(outputtime.result)		
        whole.append(point)			
    return whole	
	
def PrintTimes(whole):
    for i in range(100):
        print(whole[i])
    return 0	

def PrintData(whole):
    for i in range(100):
        print(whole[i][1])
    return 0	
	
times = Make100Times()
#PrintTimes(times)

data = Make100DataPoints()
#PrintData(data)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Weather vs Flight Delay")
ax1.set_xlabel('wind speed')
ax1.set_ylabel('flight delay')
#plotpoints = NP.polyfit(data[0],data[1])

#print ("coefs0" , plotpoints)

ax1.plot(data[0],data[1], c='r')

leg = ax1.legend()
plt.show()


