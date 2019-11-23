# Python3 program to find sum of nodes at each level and maximum level sum in binary tree

# Helper function that allocates a new
# node with the given data and None
# left and right poers.
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def printArr(arr):
    count = 0
    for i in arr:
        print('Sum of', count, 'level is', i)
        count += 1

    print('Maximum level sum is', max(arr))

def level_sum(root, arr, n, level):
    if root is None:
        return

    if (root != None):
        # Recursively calling left-subtree while incrementing the level:
        level_sum(root.left, arr, n, (level + 1))

        # Adding all nodes values belonging to same level
        arr[level] += root.data

        # Recursively calling right-subtree while incrementing the level
        level_sum(root.right, arr, n, (level + 1))

def Height(root):
    # Finding the height of the tree:
    # Height of tree = Max(Height(leftsubtree,rightsubtree) + 1)
    if root is None:
        return 0

    lheight = Height(root.left)
    rheight = Height(root.right)

    return(max(lheight, rheight) + 1)

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    levels = Height(root)
    arr = [0]*levels
    n_elements = [0]*levels

    level_sum(root, arr, n_elements, 0)

    printArr(arr)
