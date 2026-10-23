# ==============================================================================
# CLASE NODE: Representa cada elemento individual en la memoria Heap
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data # Stores the value of the node
        self.next = None # Memory reference to the next node in the stack
        
    
# ==============================================================================
# CLASE STACK: Estructura de control basada en nodos enlazados
# ==============================================================================\\
    
class Stack:
        def __init__(self):
            self.top = None # Always point to the top node of the stack
            
        # Push method: Adds a new node to the top    
        def push(self, data):
            new_node = Node(data) # The new node points to the old top
            new_node.next = self.top # The 'top' pointer is updated to the new node
            self.top = new_node
        
        # Pop method: Removes and returns the top node
        def pop(self):
            if self.top is None:
                raise IndexError("Error: Pop desde una pila vacia. (Stack Underflow).")
            data_to_remove = self.top.data
            self.top = self.top.next
            return data_to_remove
        
        def print_stack(self):
            current = self.top
            print("=== Cima del Stack ===")
            while current is not None:
                print(current.data)
                current = current.next
            print("=== Base del Stack ===")
            
# ==============================================================================
# CASO DE PRUEBA Y DEMOSTRACIÓN
# ==============================================================================

if __name__ == "__main__":
    my_pila = Stack()
    
    my_pila.push(10)
    my_pila.push(20)
    my_pila.push(30)
    
    my_pila.print_stack
    
    eliminated = my_pila.pop()
    print(f"\nEl elemento eliminado con pop: {eliminated}\n")
    
    my_pila.print_stack()