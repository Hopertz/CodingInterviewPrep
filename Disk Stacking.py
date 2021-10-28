"""
    Disk Stacking
You're given a non-empty array of arrays where each subarray holds three integers and represents a disk. These integers
denote each disk's width,
depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the stack. A
disk must have a strictly smaller width, depth, and height than any other disk below it.

Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the
bottom disk. Note that you can't rotate disks; in other words, the integers in each subarray must represent [width,
depth, height] at all times.

You can assume that there will only be one stack with the greatest total height.

Sample Input
  disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

Sample Output

[[2, 1, 2], (3, 2, 3], [4, 4, 5]]

// 10 (2 + 3 + 5) is the tallest height we can get by
// stacking disks following the rules laid out above.

"""

# SOLUTION 1

# O(n^2) time | O(n) space
def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i

    return buildSequence(disks, sequences, maxHeightIdx)


def areValidDimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))
