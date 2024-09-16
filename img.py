class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Create a linked list with 100 nodes
linked_list = LinkedList()
for i in range(1, 101):
    linked_list.append(i)


import matplotlib.pyplot as plt

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def visualize(self):
        values = []
        labels = []
        current = self.head
        while current:
            values.append(current.data)
            labels.append(f'Node {current.data}')
            current = current.next

        plt.figure(figsize=(10, 6))
        plt.bar(labels, values)
        plt.xlabel('Nodes')
        plt.ylabel('Values')
        plt.title('Visualization of Linked List Nodes')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()


# Create a linked list with 100 nodes
linked_list = LinkedList()
for i in range(1, 101):
    linked_list.append(i)

# Visualize the linked list
linked_list.visualize()
