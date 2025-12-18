# Node class for Circular Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data      # Store data
        self.next = None      # Pointer to next node


# Circular Singly Linked List class
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None      # Head of the list

    # Insert a node at the beginning
    def insert_front(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            new_node.next = new_node    # Point to itself
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    # Insert a node at the end
    def insert_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    # Insert a node after a given value
    def insert_after(self, key, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            if current.data == key:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return

            current = current.next
            if current == self.head:
                break

        print("Key not found")

    # Delete the first node
    def delete_front(self):
        if self.head is None:
            return

        # If only one node exists
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next

            self.head = self.head.next
            current.next = self.head

    # Delete the last node
    def delete_end(self):
        if self.head is None:
            return

        # If only one node exists
        if self.head.next == self.head:
            self.head = None
        else:
            prev = None
            current = self.head

            while current.next != self.head:
                prev = current
                current = current.next

            prev.next = self.head

    # Delete a node with a specific value
    def delete(self, key):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                # If only one node exists
                if current.next == current:
                    self.head = None
                # If deleting head
                elif current == self.head:
                    prev = self.head
                    while prev.next != self.head:
                        prev = prev.next
                    self.head = self.head.next
                    prev.next = self.head
                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next
            if current == self.head:
                break

        print("Key not found")

    # Display the circular list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


# Example usage
if __name__ == "__main__":
    csll = CircularSinglyLinkedList()

    csll.insert_end(10)
    csll.insert_end(20)
    csll.insert_front(5)
    csll.insert_after(10, 15)

    csll.display()

    csll.delete(15)
    csll.delete_front()
    csll.delete_end()

    csll.display()
