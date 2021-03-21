"""
  Binary Tree Diameter

  Write a function that takes in a Binary Tree and returns its diameter.The diameter of a binary
  tree is defined as the length of its longest path,,even if that path doesn't pass through the
  root of the tree.

  A path is a collection of connected nodes in a tree,where no node is connected to more than
  two other nodes. The length of a path is the number of edges between the paths's first node
  and its last node.

  Each BinaryTree node node has an integer value, a left child node, and a right child node.Children
  nodes can either be BinaryTree nodes themselves or None/ null.

  Sample Input
                1
              /   \
             3      2
            / \
          7    4
         /      \
        8        5
       /          \
      9            6

    Sample Output
       6  // 9 -> 8 -> 7 -> 3 ->4 -> 5 -> 6
       // There are 6 edges between the first node and the last node of this tree's longest path.

"""