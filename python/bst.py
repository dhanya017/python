class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class bst:
    def create_node(self,value):
        return Node(value)
    def insert_node(self,node,value):
        if node is None:
            return self.create_node(value)
        if value<node.data:
            node.left=self.insert_node(node.left,value)
        else:
            node.right=self.insert_node(node.right,value)
        return node
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def preorder(self,node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
tree=bst()
root=tree.create_node(5)
tree.insert_node(root,2)
tree.insert_node(root,10)
tree.insert_node(root,8)
tree.insert_node(root,15)
print("---inorder---")
tree.inorder(root)
print("---preorder---")
tree.preorder(root)
print("---postorder---")
tree.postorder(root)