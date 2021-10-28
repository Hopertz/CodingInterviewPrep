"""
   Merge Linked Lists
   Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively. The function should merge the lists in place
   (i.e., it shouldn't create a brand new list) and return the head of the merged list; the merged list should be in sorted order.
   Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of
   the list.
   You can assume that the input linked lists will always have at least one node; in other words, the heads will never be None / null.
    Sample Input
       headone = 2 -> 6 -> 7 -> 8 // the head node with value 2
       headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10 // the head node with value 1
    Sample Output
       1 -> 2 -> 3 -> 4 - 5 - 6 - 7 - 8 - 9 -> 10 // the new head node with value 1

"""

# SOLUTION 1

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time 0(1) space - where n is the number of nodes in the first
# Linked List and m is the number of nodes in the second Linked List
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            if p1Prev is not None:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    if p1 is None:
        p1Prev.next = p2
    return headOne if headOne.value < headTwo.value else headTwo


# SOLUTION 2

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | O(n + m) space - where n is the number of nodes in the first
# Linked List and m is the number of nodes in the second Linked List
def mergeLinkedLists(headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerge(p1, p2, p1Prev):
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return

    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev is not None:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, newP2, p2)

