"""
  Linked List Palindrome o ☆
 Write a function that takes in the head of a Singly Linked List and returns a boolean representing whether the linked
 list's nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.
 A palindrome is usually defined as a string that's written the same forward and backward. For a linked list's nodes to
 form a palindrome, their values must be the same when read from left to right and from right to left. Note that single-
 character strings are palindromes, which means that single-node linked lists form palindromes.
 Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to
 None 1 null if it's the tail of the list.
 You can assume that the input linked list will always have at least one node; in other words, the head will never be
 None / null.

  Sample Input
    head = 0 -> 1 -> 2 -> 2 -> 1 -> p // the head node with value o

 Sample Output
    true

"""

# Solution One
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(n) space - where n is the number of nodes in the Linked List
def linkedListPalindrome(head):
    isPalindromeResults = ispalindrome(head, head)
    return isPalindromeResults.outerNodesAreEqual


def ispalindrome(leftNode, rightNode):
    if rightNode is None:
        return LinkedListInfo(True, leftNode)

        recursiveCallResults = ispalindrome(leftNode, rightNode.next)
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare
    outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual

    recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value
    nextLeftNodeToCompare = leftNodeToCompare.next

    return LinkedListInfo(recursiveIsEqual, nextLeftNodeToCompare)


class LinkedListInfo:
    def __init__(self, outerNodesAreEqual, leftNodeToCompare):
        self.outerNodesAreEqual = outerNodesAreEqual
        self.leftNodeToCompare = leftNodeToCompare


# Solution Two
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | 0(1) space where n is the number of nodes in the Linked List
def linkedListPalindrome(head):
    slowNode = head
    fastNode = head
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    reversedSecondHalfNode = reverselinkedList(slowNode)
    firstHalfNode = head
    while reversedSecondHalfNode is not None:
        if reversedSecondHalfNode.value != firstHalfNode.value:
            return False
        reversedSecondHalfNode = reversedSecondHalfNode.next
        firstHalfNode = firstHalfNode.next

    return True


def reverselinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
