"""
  Rearrange Linked List ☆
 Write a function that takes in the head of a Singly Linked List and an integer k , rearranges the list in place (i.e., doesn't
 create a brand new list) around nodes with value k, and returns its new head.
 Rearranging a Linked List around nodes with value k means moving all nodes with a value smaller than k before all
 nodes with value k and moving all nodes with a value greater than k after all nodes with value k.
 All moved nodes should maintain their original relative ordering if possible.
 Note that the linked list should be rearranged even if it doesn't have any nodes with value k.
 Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to
 None / null if it's the tail of the list.
 You can assume that the input Linked List will always have at least one node; in other words, the head will never be
 None / null.

    Sample Input
    head = 3 -> -> 5 -> 2 -> 1 -> 4 // the head node with value 3
    k = 3

    Sample Output
     0 -> 2 -> 1 -> 3 -> 5 -> 4 // the new head node with value 0
    // Note that the nodes with values 0, 2, and i have
    // maintained their original relative ordering, and
    // so have the nodes with values 5 and 4.

"""

# SOLUTION 1

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | 0(1) space where n is the number of nodes in the linked List
def rearrangeLinkedList(head, k):
    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    greaterListHead = None
    greaterListTail = None

    node = head

    while node is not None:
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(smallerListHead, smallerListTail, node)
        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(greaterListHead, greaterListTail, node)
        else:
            equalListHead, equalListTail = growLinkedList(equalListHead, equalListTail, node)
        prevNode = node
        node = node.next
        prevNode.next = None
    firstHead, firstTail = connectLinkedLists(smallerListHead, smallerListTail, equalListHead, equalListTail)
    finalHead, _ = connectLinkedLists(firstHead, firstTail, greaterListHead, greaterListTail)
    return finalHead


def growLinkedList(head, tail, node):
    newHead = head
    newTail = node

    if newHead is None:
        newHead = node

    if tail is not None:
        tail.next = node

    return newHead, newTail


def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo
    if tailOne is not None:
        tailOne.next = headTwo
        return newHead, newTail
