class Traverser:
    def __init__(self, tree):
        self.tree = tree

    def inorder(self):
        return self._inorder(self.tree)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

    def preorder(self):
        return self._preorder(self.tree)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.data] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.tree)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.data]

    def level_order(self):
        if self.tree is None:
            return []
        queue = [self.tree]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def level_order_with_levels(self):
        if self.tree is None:
            return []
        queue = [(self.tree, 0)]
        result = []
        while queue:
            node, level = queue.pop(0)
            result.append((node.data, level))
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result

    def level_order_with_list(self):
        if self.tree is None:
            return []
        queue = [self.tree]
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

