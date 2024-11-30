import random

# Node class to represent each node in the binary tree
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Function to build the Christmas tree binary tree
def build_christmas_tree(levels):
    # Start with the root of the tree
    root = Node("*")
    current_level = [root]

    # Build the tree by adding left and right children at each level
    for _ in range(1, levels):
        next_level = []
        for node in current_level:
            # Assign random decorations to left and right children
            node.left = Node(random.choice(["@", "$", "*", "+"]))
            node.right = Node(random.choice(["@", "$", "*", "+"]))
            next_level.extend([node.left, node.right])
        current_level = next_level

    return root

# Function to visualize the tree in a Christmas tree shape
def visualize_tree(root, levels):
    if not root:
        return

    # Queue for level-order traversal
    queue = [root]
    
    # Iterate through each level of the tree
    for level in range(levels):
        level_nodes = 2 ** level  # Number of nodes at the current level
        padding = " " * (levels - level - 1)  # Padding for centering the tree
        line = padding

        # Build the string representation for this level
        for _ in range(level_nodes):
            if queue:
                current = queue.pop(0)
                line += f"{current.value} "
                # Add the left and right children to the queue
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            else:
                line += " "
        print(line)

# Build a Christmas tree with 4 levels and visualize it
tree_root = build_christmas_tree(4)
visualize_tree(tree_root, 4)

