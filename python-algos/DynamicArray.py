class DynamicArray:
    
    # initialize an empty array with a capacity of capacity, where capacity > 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # return the element at index i, assuming i is a valid index
    def get(self, i: int) -> int:
        return self.array[i]

    # set the element at index i to n, assuming i is a valid index
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # push the element n to the end of the array
    def pushback(self, n: int) -> None:
        if self.size < self.capacity:
            self.array[self.size] = n
            self.size += 1
        else:
            self.resize()
            self.pushback(n)

    # pop and return the element at the end of the array, assuming that the array is non-empty
    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]

    # double the capacity of the array
    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    # return the number of elements in the array
    def getSize(self) -> int:
        return self.size
    
    # return the capacity of the array
    def getCapacity(self) -> int:
        return self.capacity
    