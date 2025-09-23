# Creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Creating Linked List class
class Sll:
    def __init__(self):
        self.head = None

    # Traversal
    def traversal(self):
        count = 0
        if self.head is None:
            print("Linkedlist is empty") 
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                count += 1
                a = a.next
            print()

    # Insertion at beginning
    def insert(self, data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb     

    # Insertion at end
    def insert_end(self, data):
        print()
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    # Insertion at specific position
    def insert_position(self, position, data):
        ns = Node(data)
        a = self.head
        print()
        if position == 1:   # insert at head
            ns.next = self.head
            self.head = ns
            return
        for i in range(1, position-1):
            if a is None:
                return  # position out of range
            a = a.next
        ns.next = a.next
        a.next = ns    

    # Deletion at begin
    def deletion_at_begin(self):
        print()
        if self.head is None:
            return
        self.head = self.head.next

    # Deletion at end
    def deletion_at_end(self):
        print()
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None           

    # Deletion at specific position 
    def deletion_at_position(self, position):
        print()
        if self.head is None:
            return
        if position == 1:
            self.head = self.head.next
            return
        prev = self.head
        a = self.head.next
        for i in range(1, position-1):
            if a is None:
                return
            a = a.next
            prev = prev.next
        if a is None:
            return
        prev.next = a.next
        a.next = None                       
    def countt(self):
        print()
        count=0
        a=self.head
        while a is not None:
            count +=1
            a=a.next 
        return count
    def searching(self, s):
        a = self.head
        print()
        while a is not None:
            if a.data == s:   # check node's data
                return True   # element found
            a = a.next
        return False   # element not found


# Creating nodes                
n1 = Node(4)
n2 = Node(8)
n3 = Node(3)
n4 = Node(12)

# Linking nodes together
n1.next = n2
n2.next = n3
n3.next = n4

# Creating linked list and set head
sll = Sll()
sll.head = n1

# Demonstrating operations
print("Original linkedlist")
sll.traversal()
#insert at begin
sll.insert(1)
print("After insertion at begin")
sll.traversal()
#insert at end
sll.insert_end(21)
print("After insertion at end")
sll.traversal()
#insert at specific position
sll.insert_position(3, 78)
print("After insertion at specific position")
sll.traversal()
#delete at begin
sll.deletion_at_begin()
print("After deletion at begin")
sll.traversal()
#delete at end
sll.deletion_at_end()
print("After deletion at end")
sll.traversal()
#deleting the specific part
sll.deletion_at_position(4)
print("After deletion at specific position")
sll.traversal()
#retreieving the length of the array
print("count is:",sll.countt())
sll.traversal()
s=40
print("searching for",s,":",sll.searching(s))