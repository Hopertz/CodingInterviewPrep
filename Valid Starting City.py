"""
    Valid Starting City
   Imagine you have a set of cities that are laid out in a circle, connected by a circular road that runs clockwise.
   Each city has a gas station that provides gallons of fuel, and each city is some distance away from the next city.

   You have a car that can drive some number of miles per gallon of fuel, and your goal is to pick a starting city such
   that you can fill up your car with that city's fuel, drive to the next city, refill up your car with that city's fuel,
   drive to the next city, and so on and so forth until you return back to the starting city with 0 or more gallons of
   fuel left.

   This city is called a valid starting city, and it's guaranteed that there will always be exactly one valid starting
   city. For the actual problem, you'll be given an array of distances such that city i is distances[i] away from city
   i + 1.

   Since the cities are connected via a circular road, the last city is connected to the first city.
   
   In other words, the last distance in the distances array is equal to the distance from the last city to the first city.
   You'll also be given an array of fuel available at each city, where fuel[i] is equal to the fuel available at city i.

   The total amount of fuel available (from all cities combined) is exactly enough to travel to all cities. Your fuel tank
   always starts out empty, and you're given a positive integer value for the number of miles that your car can travel
   per gallon of fuel (miles per gallon, or MPG). You can assume that you will always be given at least two cities.

   Write a function that returns the index of the valid starting city.

   Sample Input
      distances = [5, 25, 15, 10, 15]
      fuel = [1, 2, 1, 0, 3]
      mpg = 10

   Sample Output
      4

"""

# O(n*2) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)
	
    for startCityIdx in range(numberOfCities):
	milesRemaining = 0
		
	for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
	    if milesRemaining < 0:
		continue
	    currentCityIdx = currentCityIdx % numberOfCities
			
	    fuelFromCurrentCity = fuel[currentCityIdx]
	    distanceToNextCity = distances[currentCityIdx]
	    milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity

        if milesRemaining >= 0:
	   return startCityIdx
	
     return -1


# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)
    milesRemaining = 0
	
    indexOfStartingCityCandidate = 0
    milesRemainingAtStartingcityCandidate = 0
	
    for cityIdx in range(1, numberOfCities):
	distanceFromPreviousCity = distances[cityIdx - 1]
	fuelFromPreviousCity = fuel[cityIdx - 1]
	milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity 
		
	if milesRemaining < milesRemainingAtStartingcityCandidate:
	   milesRemainingAtStartingcityCandidate = milesRemaining
	   indexOfStartingCityCandidate = cityIdx
			
    return indexOfStartingCityCandidate
			




