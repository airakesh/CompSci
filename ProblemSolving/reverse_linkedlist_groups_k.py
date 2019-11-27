# Python program to reverse a linked list in group of given size
# Node class
class Node:
	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	# Function to initialize head
	def __init__(self):
		self.head = None

    def reverse(self, head, k):
        temp = self.head
        prev = next = None
        count = 0

        while temp and count < k:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        if next is not None:
            head.next = self.reverse(next, k)

        return prev
	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print ('\nReversed Linked list')
llist.printList()
