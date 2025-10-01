
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()  # new line after printing list

    def insert_at_begin(self, data):
        nb = Node(data)
        temp = self.head
        nb.next = temp
        if temp is not None:
            temp.prev = nb
        self.head = nb

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

    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Element not found!")

# ------------------ MAIN PROGRAM ------------------
dll = Dll()

# Step 1: Create DLL with user input
n = int(input("Enter number of nodes to create: "))
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    dll.insert_at_end(data)

print("\nInitial Doubly Linked List:")
dll.traverse()

# Step 2: Operations Menu
while True:
    print("\nChoose operation:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete a Node")
    print("4. Display List")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data to insert at beginning: "))
        dll.insert_at_begin(data)
        dll.traverse()

    elif choice == 2:
        data = int(input("Enter data to insert at end: "))
        dll.insert_at_end(data)
        dll.traverse()

    elif choice == 3:
        key = int(input("Enter node value to delete: "))
        dll.delete(key)
        dll.traverse()

    elif choice == 4:
        dll.traverse()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
