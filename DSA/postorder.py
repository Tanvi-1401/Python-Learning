class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    data = int(input("Enter node value (-1 for no node): "))
    
    if data == -1:
        return None
    
    root = Node(data)

    print("Enter left child of", data)
    root.left = create()

    print("Enter right child of", data)
    root.right = create()

    return root


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = create()

print("Postorder Traversal:")
postorder(root)