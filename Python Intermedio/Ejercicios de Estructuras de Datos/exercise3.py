 # ==============================================================================
# CLASE NODE: Representa cada nodo individual del árbol
# ==============================================================================
class Node:
    def __init__(self, data):
        self.data = data    # Value stored in the node
        self.left = None    # Reference to the left child
        self.right = None   # Reference to the left child
        
# ==============================================================================
# CLASE BINARY TREE: Estructura principal del árbol
# ==============================================================================

class BinaryTree:
    def __init__(self):
        self.root = None    # Main root of the tree

    # Method to insert values while maintaining the basic structure of a binary search tree
    def insert(self, data): 
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)
    
    # Method to print the entire structure in order (In-Order traversal)            
    def print_tree(self):
        print("=== Inicio del Binary Tree ===")
        self._print_in_order(self.root)
        print("=== Fin del Binary Tree ===")
        
    def _print_in_order(self, current):
        if current is not None:
            self._print_in_order(current.left)  # Traverse the left subtree
            print(current.data)                 # Print the current node
            self._print_in_order(current.right) # Traverse the right subtree
            
# ==============================================================================
# CASO DE PRUEBA Y DEMOSTRACIÓN
# ==============================================================================

if __name__ == "__main__":
    my_tree = BinaryTree()
    
    # Elements are inserted into the tree
    my_tree.insert(50)
    my_tree.insert(30)
    my_tree.insert(70)
    my_tree.insert(20)
    my_tree.insert(40)
    my_tree.insert(10)
    
    my_tree.print_tree()