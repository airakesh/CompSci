class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        
        if self.right:
            self.right.inorder()

def merge_tree(A, B):
    if A.left and B.left:
        A.left.data += B.left.data
        merge_tree(A.left, B.left)
        
    if A.right and B.right:
        A.right.data += B.right.data
        merge_tree(A.right, B.right)
        
    if B.left and not A.left:
        A.left = B.left
        
    if B.right and not A.right:
        A.right = B.right

if __name__ == "__main__":
    A = Node(2)
    A.left = Node(1)
    A.left.left = Node(5)
    A.right = Node(4)

    B = Node(3)
    B.left = Node(6)
    B.left.right = Node(2)
    B.right = Node(1)
    B.right.right = Node(7)

    A.data += B.data
    merge_tree(A, B)

    A.inorder()
