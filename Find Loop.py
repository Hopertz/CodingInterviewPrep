"""
    Find Loop ☆
    Write a function that takes in the head of a Singly Linked List that contains a loop (in other words,
    the list's tail node points to some node in the list instead of None / null ). The function should return the node
    (the actual node-not just its value) from which the loop originates in constant space.

    Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

    Sample Input
        head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 ->  6 // the head node with value 0
                                   ^          v
                                   9 <- 8 <- 7
    Sample Output
        4 -> 5 ->  6 // the node with value 4
        ^          V
        9 <- 8 - 7

"""

# SOLUTION 1

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | 0(1) space
def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first

