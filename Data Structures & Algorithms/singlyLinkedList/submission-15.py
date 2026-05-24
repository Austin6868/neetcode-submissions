from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
        # It's good practice to keep track of the size for O(1) size checks
        self.size = 0 
    
    def get(self, index: int) -> int:
        # Check for invalid index or empty list
        if index < 0 or not self.root:
            return -1
        
        curr_node = self.root
        for i in range(index):
            if curr_node.next is None: # We've reached the end before the desired index
                return -1
            curr_node = curr_node.next
        
        # If curr_node is None here, it means index was out of bounds
        if curr_node:
            return curr_node.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.root
        self.root = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.root:
            self.root = new_node
            self.size += 1
            return
        
        curr_node = self.root
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        # Check for invalid index or empty list
        if index < 0 or not self.root:
            return False
        
        # Case 1: Remove the head (index 0)
        if index == 0:
            self.root = self.root.next
            self.size -= 1
            return True
        
        # Case 2: Remove a node other than the head
        curr_node = self.root
        # Iterate to the node *before* the one to be removed
        for i in range(index - 1):
            if curr_node.next is None: # Index is out of bounds
                return False
            curr_node = curr_node.next
            
        # If curr_node.next is None here, it means the index was out of bounds
        # (e.g., trying to remove the 4th element in a 3-element list)
        if curr_node.next is None:
            return False
            
        # Skip the node to be removed
        curr_node.next = curr_node.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        curr_node = self.root
        while curr_node is not None: # Iterate as long as curr_node exists
            result.append(curr_node.val)
            curr_node = curr_node.next
        return result

    # Optional: Add a size method
    def getSize(self) -> int:
        return self.size