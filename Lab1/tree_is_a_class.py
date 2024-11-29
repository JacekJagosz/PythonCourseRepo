class TreeNode:
    def __init__(self, value=None):
        # Initialize a tree node.

        self.value = value
        self.children = []  # List of tuples (child_node, edge_value)

    def add_child(self, child, edge_value=None):
        # Add a child to this node.

        self.children.append((child, edge_value))


class Tree:
    def __init__(self, root_value=None):
        # Initialize the tree with an optional root value.

        self.root = TreeNode(root_value)

    def traverse(self):
        # Perform a breadth-first traversal of the tree, yielding each node and its edge values.
        #
        # Yields:
        #     (TreeNode, edge_value): A tuple containing the current node and the value of the edge that leads to it.

        if not self.root:
            return

        queue = [(self.root, None)]  # (node, edge_value)
        while queue:
            current_node, edge_value = queue.pop(0)
            yield current_node, edge_value
            for child, child_edge_value in current_node.children:
                queue.append((child, child_edge_value))

    def __str__(self):
        # Return a string representation of the tree.

        lines = []
        for node, edge_value in self.traverse():
            node_info = f"Node(value={node.value})"
            if edge_value is not None:
                node_info += f" --({edge_value})--> "
            else:
                node_info += " --> "
            lines.append(node_info + "Children: " +
                         ", ".join(f"Node(value={child.value})" for child, _ in node.children))
        return "\n".join(lines)
