class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList_fun:
    def __init__(self):
        self.head = None

    def _record_state(self, action, index=None, value=None):
        lst = []
        current = self.head
        while current:
            lst.append(current.data)
            current = current.next
        return (action, index, value, lst.copy())

    def append(self, value):
        steps = []
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            steps.append(self._record_state("append", 0, value))
            return "append",steps

        current = self.head
        index = 0
        while current.next:
            steps.append(self._record_state("traverse", index))
            current = current.next
            index += 1

        current.next = new_node
        steps.append(self._record_state("append", index + 1, value))
        return "append",steps



    def delete(self, index):
        steps = []
        if not self.head:
            raise IndexError("List is empty")
        if index == 0:
            steps.append(self._record_state("delete_start", 0))
            self.head = self.head.next
            steps.append(self._record_state("delete_end", 0))
            return steps

        current = self.head
        pos = 0
        while current.next and pos < index - 1:
            steps.append(self._record_state("traverse", pos))
            current = current.next
            pos += 1

        if not current.next:
            raise IndexError("Index out of bounds")

        steps.append(self._record_state("delete_start", index))
        current.next = current.next.next
        steps.append(self._record_state("delete_end", index))
        return steps

