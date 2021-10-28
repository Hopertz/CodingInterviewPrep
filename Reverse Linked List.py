"""
    Reverse Linked List
    Write a function that takes in the head of a Singly Linked List, reverses the list in place (i.e., doesn't create a brand new list), and returns its new
    head.
    Each Linkedlist node has an integer value as well as a next node pointing to the next node in the list or to None/null if it's the tail
    of the list
    You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null .

    Sample Input
       head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

    Sample Output
         5 -> 4 -> 3 -> 2 -> 1 -> 0 // the new head node with value 5

"""
# SOLUTION 1

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | 0(1) space - where n is the number of nodes in the Linked List
def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
