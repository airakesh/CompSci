# All of its root-to-leaf paths for a tree
class Node:
    # A binary tree node has data, pointer to left child and a pointer to right child
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

def printRoute(stack, root):
    if root == None:
        return

    # append this node to the path array
    stack.append(root.data)
    if (root.left == None and root.right == None):
        # print out all of its root - to - leaf
        print(' '.join([str(i) for i in stack]))

    # otherwise try both subtrees
    printRoute(stack, root.left)
    printRoute(stack, root.right)
    stack.pop()

if __name__ == '__main__':

    root = Node(1);
    root.left = Node(2);
    root.right = Node(3);
    root.left.left = Node(4);
    root.left.right = Node(5);
    printRoute([], root)
