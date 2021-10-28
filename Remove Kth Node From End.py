"""
   Remove Kth Node From End
"""

# SOLUTION 1

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(n) space
def removeKthNodeFromEnd(head, k):
    nodeList = makeList(head)
    length = len(nodeList)
    indxToBeRemoved = length - k
    indx = 0
    currentNode = head
    prevNode = None
    while currentNode and indx != indxToBeRemoved:
        prevNode = currentNode
        currentNode = currentNode.next
        indx += 1

    if prevNode == None:
        head.value = head.next.value
        head.next = head.next.next

    elif currentNode:
        prevNode.next = currentNode.next
    currentNode.next = None


def makeList(node):
    nodeList = []
    currentNode = node
    nodeList.append(currentNode.value)
    while currentNode.next is not None:
        currentNode = currentNode.next
        nodeList.append(currentNode.value)
    return nodeList

# SOLUTION 2

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next




