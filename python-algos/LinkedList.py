class Node:
    # initialize a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    # initialize an empty linked list
    def __init__(self):
        self.head = None
        self.size = 0
    
    # return the value of the ith node
    def get(self, index: int) -> int:
        if(index < 0):
            print("Index must be non-negative.")
            return -1
        i = 0
        current = self.head
        while(current is not None):
            if i == index:
                return current.data
            current = current.next
            i += 1
        return -1

    # insert a node with val at the head of the list
    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    # insert a node with val at the tail of the list
    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        current = self.head
        while(current.next is not None):
            current = current.next
        current.next = node
        self.size += 1

    # remove the ith node
    def remove(self, index: int) -> bool:
        if(index < 0):
            print("Index must be non-negative.")
            return False
        if(index == 0):
            if(self.head is not None):
                self.head = self.head.next
                return True
            else:
                print("List is empty.")
                return False
        
        i = 0
        current = self.head
        prev = None

        while(current is not None):
            if(i == index):
                prev.next = current.next
                return True
            prev = current
            current = current.next
            i += 1
        
        self.size -= 1
        return False
        
    # return an array of all the values in the linked list
    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while(current is not None):
            values.append(current.data)
            current = current.next
        return values
    