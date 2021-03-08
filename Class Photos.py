"""
   Class Photos

   It's photo day at the school,and you're the photographer assigned to take class photos.
   The class that you'll be photographing has an even number of students,and all these
   students are wearing red or blue shirts.In fact,exactly half of the class is wearing
   red shirts, and the other half is wearing blue shirts.You're responsible for arranging
   the students in two rows before taking the photo.each row should contain the same number
   of the students and should adhere to the following guidelines:

      - All students wearing red shirts must be in the same row.
      - All students wearing blue shirts must be in the same row.
      - Each students in the back row must be strictly taller than
        the student directly in front of them in the front row.

   You're given two input arrays: one containing the heights of all the students with
   red shirts and another one containing the heights of all the students with blue shirts.
   These arrays will always have the same Length and each height will a positive integer

   Write a function that returns whether or not a class photo that follows the stated
   guidelines can be taken.

   Note: You can assume that each class has at least 2 students.

   Sample Input

     redShirtsHeights = [5, 8, 1, 3, 4]
     blueShirtHeights = [6, 9, 2, 4, 5]

   Sample Output
     true
"""

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




