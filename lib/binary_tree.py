# binary_tree.py

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

inorder(root)
preorder(root)
postorder(root)