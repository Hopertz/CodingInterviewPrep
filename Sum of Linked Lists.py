"""
   Sum of LInked Lists

   You're given two Linked lists of potentially unequal length.Each Linked list represents
   a non-negative integer,where each node in the Linked list is a digit of that integer,
   and the first node in each Linked List always represents the least significant digit
   of the integer.Write a function that returns the head of a new Linked list that represents
   the sum of the integers represented by the two input Linked list.

   Each Linked list node has an integer value as well as a next node pointing to the next
   node in the list or to None / null if it's the tail of the list.The value of each Linked list
   node is always in the range of 0 - 9.

   Note: your function must create and return a new Linked list,and you're not allowed to modify
   either of the input Linked lists.

   Sample Input
    linkedListOne = 2 -> 4 -> 7 -> 1
    linkedListTwo = 9 -> 4 -> 5

   Sample Output
     1 -> 9 -> 2 -> 2
     // linkedListOne represents 1742
     // linkedListTwo represents 549
     // 1742 + 549 = 2291

"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n,m)) time | O(max(n,m)) space where n is the length of the first Linked list
# m is the length of the second Linked list
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHeaderPointer = LinkedList(0)
    currentNode = newLinkedListHeaderPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode

        carry = sumOfValues // 10

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedListHeaderPointer.next





class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m) time | 0(n + m) space where n is the length of the first Linked list
# # m is the length of the second Linked list
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    one = makeIntegers(linkedListOne)
    two = makeIntegers(linkedListTwo)
    oneadd = int(''.join(str(i) for i in one))
    twoadd = int(''.join(str(i) for i in two))
    total = oneadd + twoadd
    total = str(total)[::-1]
    head = LinkedList(total[0])
    parent = head
    for i in range(1, len(total)):
        head.next = LinkedList(i)
        head = head.next

    return parent


def makeIntegers(node):
    arr = []
    if node is None:
        return arr[::-1]
    arr.append(node.value)
    makeIntegers(node.next)
