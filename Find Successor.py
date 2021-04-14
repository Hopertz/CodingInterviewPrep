"""
  Find Successor

  Write a function that takes in a Binary Tree(where nodes have an additional pointer to their parent node)
  as well as a node contained in that tree and returns the given node's successor.

  A node's successor is the next node to be visited(immediately after the given node) when traversing its
  tree using the in-order tree-traversal technique. A node hs no successor if it's the last node to be visited
  in the in-order traversal.

  If a node has no successor, your function should return None/ null.

  Each BinaryTree node has an integer value,a parent node, a left child node, and a right child node.
  Children nodes can either be BinaryTree nodes themselves or None / null.
  
  Sample Input

       tree =  1
             /   \
            2     3
          /  \
         4    5
        /
       6
       node = 5

   Sample Output

       1
       // This tree's in-order traversal order is:
       // 6 -> 4 -> 2 -> 5 -> 1 -> 3
       // 1 comes immediately after 5.
"""