def findSum(node):
    if node is None:
        return 0

    leftSum = findSum(node.left)
    rightSum = findSum(node.right)

    return node.value + leftSum + rightSum
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
totalSum = findSum(root)

print("Сума всіх значень:", totalSum)