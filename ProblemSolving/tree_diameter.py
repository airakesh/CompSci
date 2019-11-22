class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# function to get diameter of a binary tree
def diameter(tree):
    diam = 0

    def height_and_dia(tree):
        nonlocal dia

        if not (tree):
            return 0

        lh = height_and_dia(tree.left)
        rh = height_and_dia(tree.right)

        dia = max(dia, lh + rh + 1)

        return max(lh, rh) + 1

    height_and_dia(tree)
    return dia

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print((diameter(root)))
