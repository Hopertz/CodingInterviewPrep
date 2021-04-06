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