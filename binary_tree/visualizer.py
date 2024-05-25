import random

from binary_tree import TreeNode
from binary_tree import generate_random_tree


class Visualizer:

    @staticmethod
    def print_tree_as_directory_structure(root: None | TreeNode, prefix=""):
        if root is None:
            return
        print(prefix + "├─ " + str(root.val))

        if root.left or root.right:
            if root.left:
                Visualizer.print_tree_as_directory_structure(root.left, prefix + "│  ")
            else:
                print(prefix + "│  " + "├─ None")

            if root.right:
                Visualizer.print_tree_as_directory_structure(root.right, prefix + "│  ")
            else:
                print(prefix + "│  " + "├─ None")

    @staticmethod
    def print_tree_as_indented_list(root: None | TreeNode, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left or root.right:
                if root.left:
                    Visualizer.print_tree_as_indented_list(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    Visualizer.print_tree_as_indented_list(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
        else:
            print(" " * (level * 4) + prefix + "None")


if __name__ == '__main__':
    root = generate_random_tree(random.randint(4, 8))
    Visualizer.print_tree_as_directory_structure(root)
    Visualizer.print_tree_as_indented_list(root)
