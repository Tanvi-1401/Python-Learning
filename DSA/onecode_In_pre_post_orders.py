class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree using user input
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


# Inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main
root = create()

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)