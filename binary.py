class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def min_value_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def get_successor(self, root, key):
        current = self.search(root, key)
        if current is None:
            return None
        if current.right:
            return self.min_value_node(current.right)
        successor = None
        ancestor = root
        while ancestor != current:
            if current.val < ancestor.val:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor
# Example Usage
tree = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    tree.root = tree.insert(tree.root, val)

tree.inorder(tree.root)  # Output: 20 30 40 50 60 70 80
