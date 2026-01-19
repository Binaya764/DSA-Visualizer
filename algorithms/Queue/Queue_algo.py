class queue_fun:
    def __init__(self, capacity=5):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.capacity = capacity

    def size(self):
        return self.rear - self.front + 1

    def enqueue(self, value):
        if self.size() >= self.capacity:
            return "overflow", self.queue[self.front:].copy()

        self.queue.append(value)
        self.rear += 1
        return "enqueued", self.queue[self.front:].copy()

    def dequeue(self):
        if self.size() == 0:
            return "underflow", None, []

        value = self.queue[self.front]
        self.front += 1

        # Optional memory cleanup
        if self.front > 5:
            self.queue = self.queue[self.front:]
            self.rear -= self.front
            self.front = 0

        return "dequeued", value, self.queue[self.front:].copy()

    def clear(self):
        self.queue.clear()
        self.front = 0
        self.rear = -1
        return "cleared", None, []
