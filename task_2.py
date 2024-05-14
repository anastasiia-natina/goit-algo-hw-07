def findMin(node):
    if node is None:
        return None

    leftMin = findMin(node.left)

    if leftMin is not None and leftMin < node.value:
        return leftMin

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

min_value = findMin(root)
print("Найменше значення:", min_value)