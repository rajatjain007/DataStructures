class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def preorder(self,start,trav)->str:
        if start:
            trav += str(start.value) + "-"
            trav = self.preorder(start.left,trav)
            trav = self.preorder(start.right,trav)
        return trav


"""
Creating a tree

        1
       / \_
     2     3
    / \   / \_
   4   5 6   7
"""

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.preorder(tree.root,""))

