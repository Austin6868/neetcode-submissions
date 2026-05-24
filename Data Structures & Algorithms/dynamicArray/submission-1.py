from collections import deque

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        result = None
        if array and i < len(self.array):
            index = 0
            while index <= i:
                result = self.array[index]
                index += 1
        return result

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.array.append(n)
        if(len(self.array) > self.capacity):
            self.resize()

    def popback(self) -> int:
        result = self.array.pop()
        return result

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity