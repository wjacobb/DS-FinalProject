"""
    Solve: Complete the __reversed__ function
"""
# Create our BST Class
class BST:
    # Create our Node subclass
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # This allows us to insert data into the BST
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    # This is called recursively until we find an empty slot to insert
    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        # Compares nodes and passes over if they match data
        elif data == node.data:
            pass
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    # Loop through forwards
    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
    
    # Loops recursively
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):        
        # Hint: Start at the root
        yield "???"

    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left) 

# Insert something into the tree object
tree = BST()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)

print("========PRINT FORWARD==========")
# This is a visual as ot what iterating forward prints
for x in tree:
    print(x, end = " ") # 1 2 3 4 5 6 7 8 9

print("\n========PRINT BACKWARDS========")
# Currently print "???"
for x in reversed(tree):
    print(x, end = " ") # 9 8 7 6 5 4 3 2 1