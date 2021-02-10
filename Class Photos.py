# Class Photo

# O(nlogn) time | O(1) space where n is the length of array.
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColourInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for idx in range(len(blueShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColourInFirstRow == 'RED':
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False

    return True

# O(nlogn) time | O(n) space where n is the length of array.
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    arr = []
    if len(redShirtHeights) != len(blueShirtHeights):
        return False
    for idx in range(len(blueShirtHeights)):
        diff = abs(blueShirtHeights[idx] - redShirtHeights[idx])
        arr.append(diff > 0)

    return all(arr)
