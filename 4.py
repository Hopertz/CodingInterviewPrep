# Branch Sums
# Running time O(N) space O(N), where N represents the number of Nodes

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calcbranchsums(root, 0, sums)
    return sums


def calcbranchsums(node, runningsums, sums):
    if node is None:
        return
    newrunningsums = runningsums + node.value
    if node.left is None and node.right is None:
        sums.append(newrunningsums)
    calcbranchsums(node.left, newrunningsums, sums)
    calcbranchsums(node.right, newrunningsums, sums)
