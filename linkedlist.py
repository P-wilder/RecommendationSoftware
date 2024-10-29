"""
Author: Persephone Wilder
"""

class node:
        def __init__(self, data):
                self.data = data
                self.next = None
                self.prev = None
                
        def __str__(self):
                str = "({0})".format(self.data)
                return str

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
                                        str += "{0}".format(current_node.data)
                                        current_node = current_node.next
                        str += "{0}".format(current_node.data)
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
        
        def getIdx(self, data):
                """
                Finds the first index of a given data

                Args:
                    data (Any): data of node you wish to find

                Returns:
                    int: Index of a node with given data or None if node doesn't exist
                """
                if self.isEmpty():
                        return None
                n = self.head
                if self.size == 1:
                        if n.data == data:
                                return 0
                for i in range(self.size):
                        if n.data == data:
                                return i
                        n = n.next
                return None

        def makeEmpty(self):
                """
                Empties list re-initializing it
		"""
                self.head = None
                self.tail = None
                self.size = 0

        def addToFront(self, data):
                """
                Adds node to the start of the list

		Args:
		    data (Any): data of node added to start of list
		"""
                n = node(data)
                if self.isEmpty():
                        self.head = n
                        self.tail = n
                        self.size += 1
                else:
                        n.next = self.head
                        self.head.prev = n
                        self.head = n
                        self.size += 1

        def addToEnd(self, data):
                """
                Adds node to end of list

		Args:
		    data (Any): data of node added to end of list
		"""
                if self.isEmpty():
                        self.addToFront(data)
                else:
                        n = node(data)
                        self.tail.next = n
                        n.prev = self.tail
                        self.tail = n
                        self.size += 1

        def add(self, data):
                """
                Adds node to the end of list

		Args:
		    data (Any): The data of the node to be added
		"""
                if self.isEmpty():
                        self.addToFront(data)
                else:
                        self.addToEnd(data)

        def removeFromFront(self):
                """
                Removes node from front of list

		Returns:
		    Any: data of the removed node or None if no node
		"""
                if self.isEmpty():
                        return None
                n = self.head
                if self.size == 1:
                        self.makeEmpty()
                        return n.data
                nnext = n.next
                nnext.prev = None
                self.head = nnext
                self.size -= 1
                return n.data


        def removeFromEnd(self):
                """
                Removes data from end of list

		Returns:
		    Any: data of the removed node or None if no node
		"""
                if self.isEmpty():
                        return None
                n = self.tail
                if self.size == 1:
                        self.makeEmpty()
                        return n.data
                nprev = n.prev
                self.tail = nprev
                nprev.next = None
                self.size -= 1
                return n.data
                       


        def remove(self, data):
                """
                Removes first node with specified data

		Args:
		    data (Any): data of node that is to be removed

		Returns:
		    Any: data of the removed node or None if no node
		"""
                if self.isEmpty():
                        return None
                else:
                        n = self.head
                        if self.size == 1:
                                self.makeEmpty()
                                return n.data
                        for i in range(self.size - 1):
                                if n.data == data:
                                        self.mend(n)
                                        self.size -= 1
                                        return n.data
                                n = n.next
                        return None
                
        def removeAtIdx(self, idx):
                """
                Removes node at given index

                Args:
                    idx (int): Index at which node is to be removed

                Returns:
                    Any: Return data of node removed at index or None if node doesn't exist
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
                return n.data