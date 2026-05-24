class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = None # Most recently used
        self.last = None # Least recently used
        self.size = 0
        self.key_map = {} # key -> node

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]

            # FIX 1: If the node is already the root, we don't need to move it.
            if node == self.root:
                return node.value

            # Unlink the node from its current position
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            # FIX 2: Correctly update self.last if the accessed node was the last one.
            if node == self.last:
                self.last = node.prev

            # Move the node to the front (make it the new root)
            node.next = self.root
            node.prev = None # New root's prev is always None
            
            if self.root:
                self.root.prev = node
            
            self.root = node
            return node.value
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        # FIX 3: Simplified and correct update logic.
        # If the key exists, just update its value and call get() to move it to the front.
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.get(key)
            self.print_list() # Moved print here to see state after put
            return

        # FIX 4: Correct eviction logic.
        if self.size >= self.capacity:
            if self.last:
                del self.key_map[self.last.key]
                self.last = self.last.prev
                if self.last:
                    self.last.next = None
                else: # Cache capacity was 1
                    self.root = None
                
                self.size -= 1 # Decrement size after eviction

        # Add the new node to the front of the list
        new_node = Node(key, value)
        self.key_map[key] = new_node
        
        if not self.root: # If the cache was empty
            self.root = new_node
            self.last = new_node
        else:
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node
        
        self.size += 1
        self.print_list() # Moved print here to see state after put

    # I've removed your insert/put wrapper for clarity.
    # The new put() method is the correct implementation.

    def print_list(self) -> None:
        curr = self.root
        result = []
        while curr is not None:
            result.append((curr.key, curr.value))
            curr = curr.next
        print(f"Size: {self.size}, List: {result}")