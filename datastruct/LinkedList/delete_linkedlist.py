'''Python program to delete a node from linked list.'''

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class
class LinkedList:

    # Function to intialize the linked list object
    def __init__(self):
        self.head = None  # Initialize head as null

    # The function to insert a new node at the beginning
    def push(self, new_data):

        # 1 & 2: Allocate the Node and put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new node
        self.head = new_node

    # Given a reference to the head to a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head itself holds the key to be deleted
        if (temp is not None):
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlinked the node from linked list
        prev.next = temp.next

        temp = None

    # Function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

# Driver code
llist = LinkedList()
llist.push(7)  # 7->None
llist.push(1)  # 1->7->None
llist.push(3)  # 3->1-7->None
llist.push(2)  # 2->3->1->7->None

print('Created Linked List: ')
llist.printList()
llist.deleteNode(1)
print('Linked List after Deletion of 1:')
llist.printList()


'''
Output:
    Created Linked List:
    2  3  1  7
    Linked List after Deletion of 1:
    2  3  7
'''
