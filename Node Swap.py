"""
   Node Swap ☆
  Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e., doesn't create a brand
  new list), and returns its new head.
  If the input Linked List has an odd number of nodes, its final node should remain the same.
  Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if
  it's the tail of the list.
  You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.

  Sample Input
      head = 0 -> 1 - 2 - 3 - 4 -> 5 // the head node with value a

  Sample Output
      1 -> -> 3 -> 2 -> 5 -> 4 // the new head node with value 1

"""

# SOLUTION 1

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(n) space where n is the number of nodes in the linked List
def nodeSwap(head):
    if head is None or head.next is None:
        return head
    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head
    return nextNode


# SOLUTION 2

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | 0(1) space - where n is the number of nodes in the Linked List
def nodeSwap(head):
    tempNode = LinkedList(0)
    tempNode.next = head

    prevNode = tempNode
    while prevNode.next is not None and prevNode.next.next is not None:
        firstNode = prevNode.next
        secondNode = prevNode.next.next
        # prevNode -> firstNode -> secondNode -> X

        firstNode.next = secondNode.next
        secondNode.next = firstNode
        prevNode.next = secondNode
        # prevNode -> secondNode -> firstNode -> X

        prevNode = firstNode
    return tempNode.next



