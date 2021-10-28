"""
   Airport Connections o ☆
 For the purpose of this question, the phrases "airport route" and "airport connection" are used interchangeably.
 You're given a list of airports (three-letter codes like "JEK" ), a list of routes (one-way flights from one airport to
 another like ("JEK", "SF0"] ). and a starting airport.
 Write a function that returns the minimum number of airport connections (one-way flights) that need to be added in order
 for someone to be able to reach any airport in the list, starting at the starting airport.
 Note that routes only allow you to fly in one direction; for instance, the route ("JFK", "SFO"] only allows you to fly
 from "JEK" to "SFO".
 Also note that the connections don't have to be direct; it's okay if an airport can only be reached from the starting
 airport by stopping at other airports first.

  Sample Input
     airports = [
     "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
     "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "ILV", "BUD",
     ]
     routes = [
     ["DSM", "ORD"],
     ["ORD", "BGI"],
     ["BGI", "LGA"],
     ["SIN", "CDG"],
     ["CDG", "SIN"],
     ["CDG", "BUD"],
     ["DEL", "DOH"],
     ["DEL", "CDG"],
     ["TLV", "DEL"],
     ["EWR", "HND"],
     ["HND", "ICN"],
     ["HND", "JFK"],
     [ICN", "JFK"],
     ["JFK", "LGA"],
     ["EYW", "LHR"],
     ["LHR", "SF0"],
     ["SFO", "SAN"],
     [SFO", "DSM"],
     ["SAN", "EYW"],
     ]
    startingAirport = "LGA"

  Sample Output
      3 // ["LGA", "TLV"], ["LGA", "SF0"], and ["LGA", "EWR"]

"""


# SOLUTION 1

# 0(a * (a + r) + a + r + alog(a)) time | 0(a + r) space where a is the number of airports and r is the number of routes
def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)


# 0(a + r) time (a + r) space
def createAirportGraph(airports, routes):
    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirportNode(airport)
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    return airportGraph


# o(a + r) time | (a) space
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    visitedAirports = {}
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes


def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstTraverseAirports(airportGraph, connection, visitedAirports)


# o(a(a + r)) time | 0(a) space
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddunreachableConnections(airportGraph, airport, unreachableConnections, {})
        airportNode.unreachableConnections = unreachableConnections


def depthFirstAddunreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstAddunreachableConnections(airportGraph, connection, unreachableConnections, visitedAirports)


# O(alog(a) + a + r) time | 0(1) space
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(key=lambda airport: len(airport.unreachableConnections), reverse=True)
    numberOfNewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True
    return numberOfNewConnections


class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unreachableConnections = []
