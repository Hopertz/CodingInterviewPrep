"""
   Linked List Construction

   Write a DoublyLinkedList class that has a head and a tail , both of which point to either a linked list Node or None
   / null . The class should support:
      • Setting the head and tail of the linked list.
      • Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1).
      • Removing given nodes and removing nodes with given values.
      • Searching for nodes with given values.
   Note that the setHead , setTail , insertBefore , insertAfter , insert at position, and remove methods all take in
   actual Node s as input parameters—not integers (except for insert at position, which also takes in an integer representing
   the position); this means that you don't need to create any new Node s in these methods. The input nodes can be either
   stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list,
   the methods will effectively be moving the nodes within the linked list. You won't be told if the input nodes are already
   in the linked list, so your code will have to defensively handle this scenario. If you're doing this problem in an
   untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed language
   like Java or TypeScript to get a better idea of what each input parameter is.
   Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node
   or None / null.
   
   Sample Usage
   // Assume the following linked list has already been created:
   1 <-> 2 <-> 3 <-> 4. <-> 5

   // Assume that we also have the following stand-alone nodes:
   3, 3, 6

   setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 || set the existing node with value 4 as the head

   setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail

   insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6

   insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6

   insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5<-> 3 <-> 6 <-> 3 || insert a stand-alone node with value 3 in position 1

   removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
   
   remove(2): 4 <-> 1 <-> 5<-> 6 // remove the existing node with value 2

   containsNodeWithValue(5): true

"""

# SOLUTION 1

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head 
        while node is not None and node.value != value:
            node = node.next
        return node is not None

   # O(1) time | O(1) space
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
