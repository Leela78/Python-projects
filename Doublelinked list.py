class Node:
    # Node of a doubly linked list
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    # Doubly Linked List
    def __init__(self):
        self.head = None

    # Display elements
    def traverse(self):
        if self.head is None:
            print("Empty DLL")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    # Insert at the beginning
    def insert_at_begin(self, data):
        nb = Node(data)
        temp = self.head
        nb.next = temp
        nb.prev = None
        if temp is not None:   
            temp.prev = nb
        self.head = nb

    # Insert at the end
    def insert_at_end(self, data):
        ne = Node(data)
        if self.head is None:   
            self.head = ne
            return
        temp = self.head
        while temp.next:  
            temp = temp.next
        temp.next = ne
        ne.prev = temp


# Creating DLL manually
l = Dll()
n1 = Node(3)
l.head = n1
n2 = Node(4)
n1.next = n2
n2.prev = n1
n3 = Node(5)
n2.next = n3
n3.prev = n2
n4 = Node(7)
n3.next = n4
n4.prev = n3

print("Creation of Doubly Linked List:")
l.traverse()

l.insert_at_begin(45)
print("After inserting at beginning:")
l.traverse()

l.insert_at_end(30)
print("After inserting at end:")
l.traverse()
