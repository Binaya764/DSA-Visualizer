class stack_fun:
    def __init__(self, capacity=10):
        self.stack = []
        self.top = -1
        self.capacity = capacity

    def push(self, value):
        if self.top >= self.capacity - 1:
            return "stack overflow", self.stack.copy()
        self.stack.append(value)
        self.top += 1
        return "pushed",self.stack.copy()

    def pop(self):
        if self.top == -1:
            return "stack underflow", None, self.stack.copy()
        value = self.stack.pop()
        self.top -= 1
        return "popped", value, self.stack.copy()

    def peek(self):
        if self.top == -1:
            return "stack is empty", None
        return "peek", self.stack[self.top]

    def clear(self):
        if not self.stack:
            return ("clear", None, "empty")

        self.stack.clear()
        self.top = -1
        return ("clear", None, "cleared")

