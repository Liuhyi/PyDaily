import random
import string


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_random_tree(depth, prob=0.5):
    if depth == 0 or random.random() > prob:
        return None
    root = TreeNode(val=random.choice(string.ascii_letters + string.digits))
    root.left = generate_random_tree(depth - 1, prob)
    root.right = generate_random_tree(depth - 1, prob)
    return root
