class LinkedList_fun:
    def __init__(self):
        self.data = []   # internal list representation

    def append(self, value):
        """
        Append node at the end.
        Returns: (action, state)
        """
        self.data.append(value)
        return ("append", self.data.copy())

    def delete(self):
        """
        Delete node from the end (tail).
        Returns: (action, value, state)
        """
        if not self.data:
            return ("empty", None, [])
        removed = self.data.pop()
        return ("delete", removed, self.data.copy())

    def clear(self):
        """
        Clear the entire linked list.
        Returns: (action, state)
        """
        self.data.clear()
        return ("clear", self.data.copy())
