"""
  Ambiguous Measurements o☆
  This problem deals with measuring cups that are missing important measuring labels. Specifically, a measuring cup only
  has two measuring lines, a Low (L) line and a High (H) line. This means that these cups can't precisely measure and
  can only guarantee that the substance poured into them will be between the Land H line. For example, you might have a
  measuring cup that has a Low line at 400ml and a high line at 435ml . This means that when you use this
  measuring cup, you can only be sure that what you're measuring is between 400ml and 435ml .
  You're given a list of measuring cups containing their low and high lines as well as one low integer and one high
  integer representing a range for a target measurement. Write a function that returns a boolean representing whether
  you can use the cups to accurately measure a volume in the specified [low, high] range (the range is inclusive).

  Note that:
   • Each measuring cup will be represented by a pair of positive integers [L, H] , where @ <= [ <= H.
   • You'll always be given at least one measuring cup, and the low and high input parameters will always satisfy the
     following constraint: @ <= low <= high.
   • Once you've measured some liquid, it will immediately be transferred to a larger bowl that will eventually (possibly)
     contain the target measurement.
   • You can't pour the contents of one measuring cup into another cup.

   Sample Input
     measuring Cups = [
       [200, 210],
       [450, 465],
       [800, 850]
      ]
      Low = 2100
      high = 2300

   Sample Output
     true
    // We use cup [450, 465] to measure four volumes:
    // First measurement: Low = 450, High = 465
    // Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
    // Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
    // Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860
    // Then we use cup [200, 210] to measure two volumes:
    // Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
    // Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280
    // We've measured a volume in the range [2200, 2280].
    // This is within our target range, so we return "true".

"""
# SOLUTION 1

# O(low * high * n) time | 0(low * high) space where n is the number of measuring cups
def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
    return canMeasureInRange(measuringCups, low, high, memoization)

def canMeasureInRange(measuringCups, low, high, memoization):
    memoizekey = createHashableKey(low, high)
    if memoizekey in memoization:
        return memoization[memoizekey]

    if low <= 0 and high <= 0:
        return False
    canMeasure = False
    for cup in measuringCups:
        cupLow, cupHigh = cup
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break
        newLow = max(0, low - cupLow)
        newHigh = max(0, high - cupHigh)
        canMeasure = canMeasureInRange (measuringCups, newLow, newHigh, memoization)
        if canMeasure:
            break
    memoization[memoizekey] = canMeasure
    return canMeasure

def createHashableKey(low, high):
    return str(low) + ":" + str(high)
