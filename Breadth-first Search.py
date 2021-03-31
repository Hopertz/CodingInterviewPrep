"""
   Breadth-first Search

   You're given a Node class that has a name and an array of optional children
   nodes.When put together,nodes form an acyclic tree-like structure.

   Implement the breadthFirstSearch method on the Node class,which takes in
   an empty array,traverses the tree using the Breadth-first Search approach
   (specifically navigating the tree from left to right), stores all of the nodes
   names in the input array,and returns it.

   Sample Input

   graph =      A
              / | \
             B  C  D
            / \   /  \
           E   F G   H
              /\  \
            I  J   K

   Sample Output
     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K']
"""