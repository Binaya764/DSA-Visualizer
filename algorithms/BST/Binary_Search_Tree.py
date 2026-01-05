class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        steps = []

        if self.root is None:
            self.root = BSTNode(value)
            steps.append(("insert", self.root))
            return steps

        current = self.root

        while True:
            steps.append(("visit", current))

            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    steps.append(("insert_left", current.left))
                    return steps
                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = BSTNode(value)
                    steps.append(("insert_right", current.right))
                    return steps
                current = current.right

            else:
                steps.append(("duplicate", current))
                return steps

    def search(self, value):
        current = self.root

        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False


    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children
            successor = self._min_value(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node


