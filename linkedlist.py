class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
            current_node = self.head
            str = ""
            if self.size > 1:
                for i in range(self.size - 1):
                    str += "{0}, ".format(current_node.value)
                    current_node = current_node.next
            str += "{0}".format(current_node.value)
            return str
    
    def size(self):
        return self.size
    
    def first(self):
        return self.head
    
    def last(self):
        return self.tail
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        

    def addToFront(self, value):
        n = node(value)
        if self.head == None:
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
            self.size += 1
            
    def addToEnd(self, value):
        n = node(value)
        if self.isEmpty():
            self.head = n
            self.tail = n
            self.size += 1
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
            self.size += 1
            
    def add(self, value):
        if self.isEmpty():
            self.addToFront(value)
        else:
            self.addToEnd(value)
    
    def remove(self, value):
        if self.isEmpty():
            return False
        else:
            current_node = self.head
            for i in range(self.size - 1):
                if current_node.value == value:
                    last_node = current_node.prev
                    next_node = current_node.next
                    last_node.next = next_node
                    next_node.prev = last_node
                    self.size -= 1
                    return True
                else:
                    current_node = current_node.next
            return False
            
LL = linkedlist()
LL.remove(2)
LL.add(3)
LL.add(2)
LL.add("hey")
LL.add(3)
LL.add(2)
LL.add("hey")
LL.add(3)
LL.add(2)
LL.add("hey")
LL.remove("hey")
LL.addToFront("hey")
LL.addToEnd(3)
print(LL)