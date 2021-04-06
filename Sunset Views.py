"""
  Sunset Views

  Given an array of buildings and a direction that all of the buildings face,return an
  array of the indices of the buildings that can see the sunset.

  A building can see the sunset if it's strictly taller than all of the buildings that
  come after it in the direction that it faces.

  The input array named buildings contains positive, non-zero integers representing the
  heights of the buildings. A building at index i thus has a height denote by buildings[i].
  All of the buildings face the same direction , and this direction is either east or west,
  denoted by the input string named direction, which will always be equal to either "EAST"
  OR "WEST".In relation to the input array,you can interpret these directions as right for
  east and left for west.

  Important note: the indices in the output array should be sorted in ascending order.

  Sample Input #1
      buildings = [3, 5, 4, 4, 3, 1, 3, 2]
      direction = "EAST"

  Sample Output #1
      [1, 3, 6, 7]


  Sample Input #2
      buildings = [3, 5, 4, 4, 3, 1, 3, 2]
      direction = "WEST"

  Sample Output #2
      [0, 1]

"""

# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    buildingsWithSunsetViews = []

    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    idx = startIdx
    runningMaxHeight = 0
    while 0 <= idx < len(buildings):
        buildingHeight = buildings[idx]

        if buildingHeight > runningMaxHeight:
            buildingsWithSunsetViews.append(idx)

        runningMaxHeight = max(runningMaxHeight, buildingHeight)

        idx += step

    if direction == "EAST":
        return buildingsWithSunsetViews[::-1]

    return buildingsWithSunsetViews

# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    candidateBuildings = []

    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1

    idx = startIdx
    while 0 <= idx < len(buildings):
        buildingHeight = buildings[idx]

        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
            candidateBuildings.pop()

        candidateBuildings.append(idx)

        idx += step

    if direction == "WEST":
        return candidateBuildings[::-1]

    return candidateBuildings
