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
                """
                Checks if list is empty

		Returns:
		    Bool: returns true if list is empty 
			  returns false if not
		"""
                if self.head == None:
                        return True
                else:
                        return False
                
        def mend(self, node):
                """
                Mends a hole in a linked list

                Args:
                    node (node): Node that is being removed
                """
                last_node = node.prev
                next_node = node.next
                last_node.next = next_node
                next_node.prev = last_node
        
        def getIdx(self, value):
                """
                Finds the first index of a given value

                Args:
                    value (Any): Value of node you wish to find

                Returns:
                    int: Index of a node with given value or None if node doesn't exist
                """
                if self.isEmpty():
                        return None
                n = self.head
                if self.size == 1:
                        if n.value == value:
                                return 0
                for i in range(self.size - 1):
                        if n.value == value:
                                return i
                        n = n.next
                return None

        def makeEmpty(self):
                """
                Empties list re-inizilizing it
		"""
                self.head = None
                self.tail = None
                self.size = 0

        def addToFront(self, value):
                """
                Adds node to the start of the list

		Args:
		    value (Any): value of node added to start of list
		"""
                n = node(value)
                if self.isEmpty():
                        self.head = n
                        self.tail = n
                        self.size += 1
                else:
                        n.next = self.head
                        self.head.prev = n
                        self.head = n
                        self.size += 1

        def addToEnd(self, value):
                """
                Adds node to end of list

		Args:
		    value (Any): Value of node added to end of list
		"""
                if self.isEmpty():
                        self.addToFront(value)
                else:
                        n = node(value)
                        self.tail.next = n
                        n.prev = self.tail
                        self.tail = n
                        self.size += 1

        def add(self, value):
                """
                Adds node to the end of list

		Args:
		    value (Any): The value of the node to be added
		"""
                if self.isEmpty():
                        self.addToFront(value)
                else:
                        self.addToEnd(value)

        def removeFromFront(self):
                """
                Removes node from front of list

		Returns:
		    Any: value of the removed node or None if no node
		"""
                if self.isEmpty():
                        return None
                n = self.head
                if self.size == 1:
                        self.makeEmpty()
                        return n.value
                nnext = n.next
                nnext.prev = None
                self.head = nnext
                self.size -= 1
                return n.value


        def removeFromEnd(self):
                """
                Removes value from end of list

		Returns:
		    Any: Value of the removed node or None if no node
		"""
                if self.isEmpty():
                        return None
                n = self.tail
                if self.size == 1:
                        self.makeEmpty()
                        return n.value
                nprev = n.prev
                self.tail = nprev
                nprev.next = None
                self.size -= 1
                return n.value
                       


        def remove(self, value):
                """
                Removes first node with specified value

		Args:
		    value (Any): Vlaue of node that is to be removed

		Returns:
		    Any: Value of the removed node or None if no node
		"""
                if self.isEmpty():
                        return None
                else:
                        n = self.head
                        if self.size == 1:
                                self.makeEmpty()
                                return n.value
                        for i in range(self.size - 1):
                                if n.value == value:
                                        self.mend(n)
                                        self.size -= 1
                                        return n.value
                                n = n.next
                        return None
                
        def removeAtIdx(self, idx):
                """
                Removes node at given index

                Args:
                    idx (int): Index at which node is to be removed

                Returns:
                    Any: Return value of node remmoved at index or None if node doesn't exist
                """
                if self.isEmpty():
                        return None
                n = self.head
                i = 0
                if idx == 0:
                        return self.removeFromFront()
                if idx == self.size - 1:
                        return self.removeFromEnd()
                if idx > self.size - 1:
                        return None
                while i < idx:
                        n = n.next
                        i += 1
                self.mend(n)
                self.size -= 1
                return n.value
                

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
print(LL)
print(LL.remove("hey"))
LL.addToFront("hey")
LL.addToEnd(3)
print(LL)
print(LL.removeFromFront())
print(LL.removeFromEnd())
print(LL)