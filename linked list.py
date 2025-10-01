class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    # Display list
    def traversal(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            a = self.head
            while a:
                print(a.data, end=" ")
                a = a.next
            print()

    # Insert at beginning
    def insert_begin(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    # Insert at end
    def insert_end(self, data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return
        a = self.head
        while a.next:
            a = a.next
        a.next = ne

    # Insert at specific position
    def insert_position(self, position, data):
        ns = Node(data)
        if position == 1:
            ns.next = self.head
            self.head = ns
            return
        a = self.head
        for i in range(1, position-1):
            if a is None:
                print("Position out of range")
                return
            a = a.next
        ns.next = a.next
        a.next = ns

    # Delete at beginning
    def delete_begin(self):
        if self.head:
            self.head = self.head.next

    # Delete at end
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        prev = self.head
        a = self.head.next
        while a.next:
            a = a.next
            prev = prev.next
        prev.next = None

    # Delete at specific position
    def delete_position(self, position):
        if self.head is None:
            return
        if position == 1:
            self.head = self.head.next
            return
        prev = self.head
        a = self.head.next
        for i in range(1, position-1):
            if a is None:
                print("Position out of range")
                return
            a = a.next
            prev = prev.next
        if a is None:
            print("Position out of range")
            return
        prev.next = a.next

    # Count nodes
    def count_nodes(self):
        count = 0
        a = self.head
        while a:
            count += 1
            a = a.next
        return count

    # Search element
    def search(self, key):
        a = self.head
        while a:
            if a.data == key:
                return True
            a = a.next
        return False

# ----------------- MAIN PROGRAM -----------------
sll = Sll()

# Step 1: Ask user for initial data
n = int(input("How many elements do you want in the linked list? "))
for i in range(n):
    data = int(input(f"Enter element {i+1}: "))
    sll.insert_end(data)

print("\nInitial linked list:")
sll.traversal()

# Step 2: Menu-driven operations
while True:
    print("\n--- Linked List Operations ---")
    print("1. Display List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Position")
    print("5. Delete at Beginning")
    print("6. Delete at End")
    print("7. Delete at Specific Position")
    print("8. Count Nodes")
    print("9. Search Element")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.traversal()
    elif choice == 2:
        data = int(input("Enter data to insert at beginning: "))
        sll.insert_begin(data)
        sll.traversal()
    elif choice == 3:
        data = int(input("Enter data to insert at end: "))
        sll.insert_end(data)
        sll.traversal()
    elif choice == 4:
        position = int(input("Enter position to insert: "))
        data = int(input("Enter data: "))
        sll.insert_position(position, data)
        sll.traversal()
    elif choice == 5:
        sll.delete_begin()
        sll.traversal()
    elif choice == 6:
        sll.delete_end()
        sll.traversal()
    elif choice == 7:
        position = int(input("Enter position to delete: "))
        sll.delete_position(position)
        sll.traversal()
    elif choice == 8:
        print("Number of nodes:", sll.count_nodes())
    elif choice == 9:
        key = int(input("Enter element to search: "))
        found = sll.search(key)
        print(f"{key} is {'found' if found else 'not found'} in the list")
    elif choice == 10:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
