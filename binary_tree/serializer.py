import random
from visualizer import Visualizer
from binary_tree import TreeNode
from binary_tree import generate_random_tree

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
    root = generate_random_tree(random.randint(4, 8))
    Visualizer.print_tree_as_directory_structure(root)
    print(GeneralizedListSerializer.serialize(root))
    root = GeneralizedListSerializer.deserialize(GeneralizedListSerializer.serialize(root))
    Visualizer.print_tree_as_directory_structure(root)
    print(GeneralizedListSerializer.serialize(root))
