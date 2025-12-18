# Node class represents a single element in the singly linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store data
        self.next = None      # Pointer to next node


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None      # First node of the list

    # Insert a node at the beginning
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node at the end
    def insert_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Insert a node after a given value
    def insert_after(self, key, data):
        current = self.head

        while current:
            if current.data == key:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print("Key not found")

    # Delete the first node
    def delete_front(self):
        if self.head:
            self.head = self.head.next

    # Delete the last node
    def delete_end(self):
        if self.head is None:
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    # Delete a node with a specific value
    def delete(self, key):
        if self.head is None:
            return

        # If head needs to be deleted
        if self.head.data == key:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next

        while current:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Key not found")

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.insert_end(10)
    sll.insert_end(20)
    sll.insert_front(5)
    sll.insert_after(10, 15)

    sll.display()

    sll.delete(15)
    sll.delete_front()
    sll.delete_end()

    sll.display()
