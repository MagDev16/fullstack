class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def pop_left(self):
        if self.head is None:
            raise IndexError("La cola esta vacia")
        data = self.head.data
        if self. head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data
    
    def pop_irght(self):
        if self.tail is None:
            raise IndexError("La cola esta vacia")
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data
    
    def print_queue(self):
        current = self.head
        print("=== Inicio de la cola ===")
        while current is not None:
            print(current.data)
            current = current.next
        print("=== Final de la Cola ===")
        
        
        
if __name__ == "__main__":
    my_deque = Deque()
    
    my_deque.push_right(10)
    my_deque.push_right(20)
    my_deque.push_left(5)
    
    my_deque.print_queue()
    
    removed_left = my_deque.pop_left()
    print(f"\nElemento eliminado de por la izquierda: {removed_left}\n")
    
    
    my_deque.print_queue()
    