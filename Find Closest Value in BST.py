# Find the closest Value in BST

# Using Recursion

# time - O(log(n)) space - O(log(n)) because of frames in call stack

def findclosestvaluebst(tree, target):
    return closestvaluebstfinder(tree, target, tree.value)


def closestvaluebstfinder(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return closestvaluebstfinder(tree.left, target, closest)
    elif target > tree.value:
        return closestvaluebstfinder(tree.right, target, closest)
    else:
        return closest


# Using while Loop
# time - O(log(n)) space - O(1)
def findclosestvaluebst2(tree, target):
    return closestvaluebstfinder2(tree, target, tree.value)


def closestvaluebstfinder2(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest
