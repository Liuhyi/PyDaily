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

    def zigzag_level_order(self):
        if self.tree is None:
            return []
        queue = [self.tree]
        result = []
        reverse = False
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                level = level[::-1]
            result.append(level)
            reverse = not reverse
        return result

    def vertical_order(self):
        if self.tree is None:
            return []
        queue = [(self.tree, 0)]
        result = {}
        while queue:
            node, hd = queue.pop(0)
            if hd in result:
                result[hd].append(node.data)
            else:
                result[hd] = [node.data]
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        return [result[hd] for hd in sorted(result)]

    def inorder_iterative(self):
        if self.tree is None:
            return []
        stack = []
        node = self.tree
        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.data)
            node = node.right
        return result

    def preorder_iterative(self):
        if self.tree is None:
            return []
        stack = [self.tree]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def postorder_iterative_with_reverse(self):
        if self.tree is None:
            return []
        stack = [self.tree]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    def postorder_iterative_with_last_visited(self):
        if self.tree is None:
            return []
        stack = []
        current = self.tree
        last_visited = None
        result = []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    result.append(peek_node.value)
                    last_visited = stack.pop()
        return result
