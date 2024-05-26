import random
from visualizer import Visualizer
from binary_tree import TreeNode
from binary_tree import generate_random_tree, is_same_tree


class PreorderSerializer:
    @staticmethod
    def serialize(root):
        if not root:
            return "#"
        return str(root.val) + "," + PreorderSerializer.serialize(root.left) + "," + PreorderSerializer.serialize(
            root.right)

    @staticmethod
    def deserialize(data):
        def helper():
            val = next(values)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        values = iter(data.split(","))
        return helper()


class GeneralizedListSerializer:

    @staticmethod
    def serialize(root):
        """Encodes a tree to a single string."""
        if not root:
            return ""

        res = str(root.val)
        if root.left or root.right:
            res += "("
            res += GeneralizedListSerializer.serialize(root.left)
            res += "."
            res += GeneralizedListSerializer.serialize(root.right)
            res += ")"
        return res

    @staticmethod
    def deserialize(data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        stack = []
        root = None
        p = None
        left = False
        n = len(data)
        i = 0

        while i < n:
            if data[i] == '(':
                stack.append(p)
                left = True
            elif data[i] == ')':
                stack.pop()
            elif data[i] == '.':
                left = False
            else:
                l = i
                while i + 1 < n and data[i + 1] not in "().":
                    i += 1
                p = TreeNode(data[l:i + 1])
                if not root:
                    root = p
                else:
                    if left:
                        stack[-1].left = p
                    else:
                        stack[-1].right = p
            i += 1

        return root


if __name__ == '__main__':
    tree = generate_random_tree(random.randint(4, 8))
    print("Original Tree:")
    Visualizer.print_tree_as_directory_structure(tree)

    # test PreorderSerializer
    preorder_string = PreorderSerializer.serialize(tree)
    print("Preorder Serialization:", preorder_string)
    deserialized_tree = PreorderSerializer.deserialize(preorder_string)
    assert is_same_tree(tree, deserialized_tree), "Preorder Serialization failed"

    # test GeneralizedListSerializer
    generalized_list_string = GeneralizedListSerializer.serialize(tree)
    print("Generalized List Serialization:", generalized_list_string)
    deserialized_tree = GeneralizedListSerializer.deserialize(generalized_list_string)
    assert is_same_tree(tree, deserialized_tree), "Generalized List Serialization failed"

    print("Serialization and Deserialization successful")