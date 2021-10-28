"""
    Waterfall Streams
  You're given a two-dimensional array that represents the structure of an indoor waterfall and a positive integer that
  represents the column that the waterfall's water source will start at. More specifically, the water source will start
  directly above the structureand will flow downwards.
  Each row in the array contains @s and 1 s, where a represents a free space and a 1 represents a block that water can't
  pass through. You can imagine that the last row of the array contains buckets that the water will eventually flow into;
  thus, the last
  row of the array will always contain only @s. You can also imagine that there are walls on both sides of the structure,
  meaning that water will never leave the structure; it will either be trapped against a wall or flow into one of the
  buckets in the last row.
  As water flows downwards, if it hits a block, it splits evenly to the left and right-hand side of that block. In other
  words, 50% of the water flows left and 50% of it flows right. If a water stream is unable to flow to the left or to the
  right (because of a block or a wall).
  the water stream in question becomes trapped and can no longer continue
  to flow in that direction; it effectively gets stuck in the structure and can no longer flow downwards, meaning that 50%
  of the previous water stream is forever lost.
  Lastly, the input array will always contain at least two rows and one column, and the space directly below the water
  source (in the first row of the array) will always be empty, allowing the water to start flowing downwards.
  Write a function that returns the percentage of water inside each of the bottom buckets after the water has flowed
  through the entire structure.
  You can refer to the first 4.5 minutes of this question's video explanation for a visual example.

     Sample Input
       array = [
         [0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0],
       ]
     source = 3

    Sample Output
      [0, 0, 0, 25, 25, 0, 0]
      The water will flow as follows:
          [
            [0, 0, 0, ., 0, 0, 0],
            [1, ., ., ., ., ., 0],
            [0, ., 1, 1, 1, ., 0],
            [., ., ., ., ., ., .],
            [1, 1, 1, ., ., 1, 0],
            [0, 0, 0, ., ., 0, 1],
            [0, 0, 0, ., ., 0, 0],
          ]


"""

# SOLUTION 1

# O(W^2 * h) tine | O(w) space - where w and h
# are the width and height of the input array
def waterfallStreams(array, source):
    rowAbove = array[0][:]
    # We'll use -1 to represent water, since 1 is used for a block.
    rowAbove[source] = -1
    for row in range(1, len(array)):
        currentRow = array[row][:]
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            haswaterAbove = valueAbove < 0
            hasBlock = currentRow[idx] == 1
            if not haswaterAbove:
                continue
            if not hasBlock:
                # If there is no block in the current column, move the water down.
                currentRow[idx] += valueAbove
                continue
            splitwater = valueAbove / 2
            # Move water right.
            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1:  # if there is a block in the way
                    break
                if currentRow[rightIdx] != 1:  # if there is no block below us
                    currentRow[rightIdx] += splitwater
                    break
            # Move water left.
            leftIdx = idx
            while leftIdx - 1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:  # if there is a block in the way
                    break
                if currentRow[leftIdx] != 1:  # if there is no block below us
                    currentRow[leftIdx] += splitwater
                    break
        rowAbove = currentRow
    # Convert our negative values to positive percentages.
    finalPercentages = list(map(lambda num: num * -100, rowAbove))
    return finalPercentages
