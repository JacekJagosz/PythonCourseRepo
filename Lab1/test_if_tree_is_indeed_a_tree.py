import unittest
from tree_is_a_class import *

class TestTreeStructure(unittest.TestCase):
    def setUp(self):
        """
        Set up a sample tree for testing.
        """
        # Create a sample tree structure
        self.tree = Tree("Root")
        self.child1 = TreeNode("Child 1")
        self.child2 = TreeNode("Child 2")
        self.grandchild = TreeNode("Grandchild")

        # Build the tree
        self.tree.root.add_child(self.child1, "Edge to Child 1")
        self.tree.root.add_child(self.child2, "Edge to Child 2")
        self.child1.add_child(self.grandchild, "Edge to Grandchild")

    def test_tree_root_value(self):
        """
        Test that the root node's value is correctly set.
        """
        self.assertEqual(self.tree.root.value, "Root")

    def test_add_child(self):
        """
        Test that children are correctly added to a node.
        """
        self.assertEqual(len(self.tree.root.children), 2)
        self.assertEqual(self.tree.root.children[0][0].value, "Child 1")
        self.assertEqual(self.tree.root.children[1][0].value, "Child 2")

    def test_edge_value(self):
        """
        Test that edge values are correctly set.
        """
        self.assertEqual(self.tree.root.children[0][1], "Edge to Child 1")
        self.assertEqual(self.tree.root.children[1][1], "Edge to Child 2")
        self.assertEqual(self.child1.children[0][1], "Edge to Grandchild")

    def test_traverse(self):
        """
        Test that the tree traversal yields all nodes and their edge values.
        """
        expected_nodes = ["Root", "Child 1", "Child 2", "Grandchild"]
        expected_edges = [None, "Edge to Child 1", "Edge to Child 2", "Edge to Grandchild"]

        nodes = []
        edges = []
        for node, edge in self.tree.traverse():
            nodes.append(node.value)
            edges.append(edge)

        self.assertEqual(nodes, expected_nodes)
        self.assertEqual(edges, expected_edges)

    def test_str_representation(self):
        """
        Test that the string representation of the tree is correct.
        """
        expected_output = (
            "Node(value=Root) --> Children: Node(value=Child 1), Node(value=Child 2)\n"
            "Node(value=Child 1) --(Edge to Child 1)--> Children: Node(value=Grandchild)\n"
            "Node(value=Child 2) --(Edge to Child 2)--> Children: \n"
            "Node(value=Grandchild) --(Edge to Grandchild)--> Children: "
        )
        print()
        print(self.tree)
        print()
        self.assertEqual(str(self.tree), expected_output)


if __name__ == "__main__":
    unittest.main()
