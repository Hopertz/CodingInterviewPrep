# Node's Depth
# Running time Average Case
# time O(n) space O(h) where n is nodes number in a binary tree,h is node's height

def nodeDepths1(root, depth=0):
    # Write your code here.
    if root is None:
        return 0
    return depth + nodeDepths1(root.left, depth + 1) + nodeDepths1(root.right, depth + 1)


def nodeDepths2(root):
    sumDepths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
