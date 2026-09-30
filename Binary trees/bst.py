class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left,data)

    if data > root.data:
        root.right = insert(root.right ,data)
    return root

root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

