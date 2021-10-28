"""
     Zip Linked List
   You're given the head of a Singly Linked List of arbitrary length k. Write a function that zips the Linked List in
   place (i.e., doesn't create a
   brand new list) and returns its head.
   A Linked List is zipped if its nodes are in the following order, where k is the length of the Linked List:
   1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...
   Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None /
   null if
   it's the tail of the list.
   You can assume that the input Linked List will always have at least one node; in other words, the head will never be
   None / null.

   Sample Input
       linkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 1
   Sample Output
       1 -> 6 -> 2 -> 5 -> 3 -> 4 // the head node with value 1

"""
# SOLUTION 1

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | 0(1) space where n is the length of the Linked List
def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList

    firstHalfHead = linkedList
    secondHalfHead = splitLinkedList(linkedList)
    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)
    return interweaveLinkedLists(firstHalfHead, reversedSecondHalfHead)

def splitLinkedList(linkedList):
    slowIterator = linkedList
    fastIterator = linkedList
    while fastIterator is not None and fastIterator.next is not None:
        slowIterator = slowIterator.next
        fastIterator = fastIterator.next.next
    secondHalfHead = slowIterator.next
    slowIterator.next = None
    return secondHalfHead

def interweaveLinkedLists(linkedList1, linkedList2):
    linkedList1Iterator = linkedList1
    linkedList2Iterator = linkedList2
    while linkedList1Iterator is not None and linkedList2Iterator is not None:
        linkedList1IteratorNext = linkedList1Iterator.next
        linkedList2IteratorNext = linkedList2Iterator.next

        linkedList1Iterator.next = linkedList2Iterator
        linkedList2Iterator.next = linkedList1IteratorNext
        linkedList1Iterator = linkedList1IteratorNext
        linkedList2Iterator = linkedList2IteratorNext

    return linkedList1

def reverseLinkedList(linkedlist):
    previousNode, currentNode = None, linkedlist
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

