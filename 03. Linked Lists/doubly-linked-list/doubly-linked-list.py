# Node class represents a single element in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the data
        self.prev = None      # Pointer to the previous node
        self.next = None      # Pointer to the next node


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # First node of the list
        self.tail = None      # Last node of the list

    # Insert a node at the beginning of the list
    def insert_front(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head   # New node points to current head
            self.head.prev = new_node   # Current head points back to new node
            self.head = new_node        # Update head

    # Insert a node at the end of the list
    def insert_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node   # Current tail points to new node
            new_node.prev = self.tail   # New node points back to current tail
            self.tail = new_node        # Update tail

    # Insert a node after a given value
    def insert_after(self, key, data):
        current = self.head

        # Traverse the list to find the key
        while current:
            if current.data == key:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next

                # If inserting not at the end
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node

                current.next = new_node
                return
            current = current.next

        print("Key not found")

    # Delete the first node
    def delete_front(self):
        if self.head is None:
            return

        # If only one node exists
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete the last node
    def delete_end(self):
        if self.tail is None:
            return

        # If only one node exists
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Delete a node with a specific value
    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
                # If deleting head
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                # If deleting tail
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                # If deleting middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return

            current = current.next

        print("Key not found")

    # Display the list from head to tail
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Display the list from tail to head
    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_front(5)
    dll.insert_after(10, 15)

    print("Forward traversal:")
    dll.display_forward()

    print("Backward traversal:")
    dll.display_backward()

    dll.delete(15)
    dll.delete_front()
    dll.delete_end()

    print("After deletions:")
    dll.display_forward()


# Key Points
# prev and next pointers allow two-way traversal
# head and tail make insert/delete at ends O(1)