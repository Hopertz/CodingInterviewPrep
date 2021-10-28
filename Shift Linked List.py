"""
  Shift Linked List ☆
    Write a function that takes in the head of a Singly Linked List and an integer k , shifts the list in place (i.e., doesn't create a brand new
    list) by k positions, and returns its new head.
    Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate. For example,
    shifting a Linked List forward by one position would make its tail become the new head of the linked list.
    Whether nodes are moved forward or backward is determined by whether k is positive or negative.
    Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None null if
    it's the tail of the list.
    You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.
      Sample Input
        head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value ®
        k = 2
      Sample Output
         4 -> 5 -> -> 1 -> 2 -> 3 // the new head node with value 4

"""

# SOLUTION 1

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | 0(1) space - where n is the number of nodes in the Linked List
def shiftLinkedList(head, k):
    listLength = 1
    listTail = head
    while listTail.next is not None:
        listTail = listTail.next
        listLength += 1

    offset = abs(k) % listLength
    if offset == 0:
        return head
    newTailPosition = listLength - offset if k > 0 else offset
    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead
