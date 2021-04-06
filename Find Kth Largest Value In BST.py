"""
   Find Kth Largest Value In BST

   Write a function that takes in a Binary Search Tree(BST) and a positive integer k and returns the kth
   largest integer contained in the BST.

   You can assume that there will only be integer values in the BST and that k is less than or equal to
   the number of nodes in the tree.

   Also,for the purpose of this question ,duplicate integers will be treated as distinct values.In other
   words,the second largest value in a BST containing values {5, 7, 7} will be 7 - not 5.

   Each BST node has an integer value, a left child node, and a right child node.A node is said to be a
   valid BST node if and only if it satisfies the BST property: its value is less than or equal to the
   values of every node to its left; its value is less than or equal to the values of every node to its
   right; and its children nodes are either valid BST nodes themselves or None / null.

   Sample Input
     tree =     15
              /   \
             5      20
            / \    /  \
           2    5 17   22
         /  \
        1    3

    k = 3

    Sample Output
       17

"""