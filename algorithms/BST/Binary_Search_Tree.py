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
        steps = []
        self.root = self._delete(self.root, value, steps)
        return value, steps

    def _delete(self, node, value, steps):
        if node is None:
            steps.append(("not_found", value))
            return None

        steps.append(("visit", node.value))

        if value < node.value:
            node.left = self._delete(node.left, value, steps)

        elif value > node.value:
            node.right = self._delete(node.right, value, steps)

        else:
            steps.append(("delete", node.value))

            # Case 1: No child
            if node.left is None and node.right is None:
                steps.append(("remove_leaf", node.value))
                return None

            # Case 2: One child
            if node.left is None:
                steps.append(("replace_with_right", node.value))
                return node.right

            if node.right is None:
                steps.append(("replace_with_left", node.value))
                return node.left

            # Case 3: Two children
            successor = self._min_value(node.right)
            steps.append(("successor", successor.value))
            node.value = successor.value
            node.right = self._delete(node.right, successor.value, steps)

        return node


    def _min_value(self, node):
        while node.left:
            node = node.left
        return node


