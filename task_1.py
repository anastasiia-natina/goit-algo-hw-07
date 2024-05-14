def findMax(node):
    if node is None:
        return None

    rightMax = findMax(node.right)

    if rightMax is not None and rightMax > node.value:
        return rightMax

    return node.value

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(8)
root.left.right = Node(7)

max_value = findMax(root)
print("Максимальне значення:", max_value)