# Node class for Circular Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data      # Store node data
        self.prev = None      # Pointer to previous node
        self.next = None      # Pointer to next node


# Circular Doubly Linked List class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None      # Head of the list

    # Insert a node at the beginning
    def insert_front(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            new_node.next = new_node    # Point to itself
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev       # Last node

            new_node.next = self.head
            new_node.prev = tail

            tail.next = new_node
            self.head.prev = new_node

            self.head = new_node        # Update head

    # Insert a node at the end
    def insert_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev

            new_node.next = self.head
            new_node.prev = tail

            tail.next = new_node
            self.head.prev = new_node

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
                new_node.prev = current

                current.next.prev = new_node
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
            tail = self.head.prev
            self.head = self.head.next

            self.head.prev = tail
            tail.next = self.head

    # Delete the last node
    def delete_end(self):
        if self.head is None:
            return

        # If only one node exists
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            new_tail = tail.prev

            new_tail.next = self.head
            self.head.prev = new_tail

    # Delete a node with a specific value
    def delete(self, key):
        if self.head is None:
            return

        current = self.head

        while True:
            if current.data == key:
                # If only one node exists
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    # If deleting head
                    if current == self.head:
                        self.head = current.next
                return

            current = current.next
            if current == self.head:
                break

        print("Key not found")

    # Display the list in forward direction
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    # Display the list in backward direction
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        tail = self.head.prev
        current = tail

        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == tail:
                break
        print("(back to tail)")


# Example usage
if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    cdll.insert_end(10)
    cdll.insert_end(20)
    cdll.insert_front(5)
    cdll.insert_after(10, 15)

    print("Forward traversal:")
    cdll.display_forward()

    print("Backward traversal:")
    cdll.display_backward()

    cdll.delete(15)
    cdll.delete_front()
    cdll.delete_end()

    print("After deletions:")
    cdll.display_forward()
