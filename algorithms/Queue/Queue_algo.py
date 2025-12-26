class queue_fun:
    def __init__(self, capacity=10):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.capacity = capacity

    def enqueue(self, value):
        if self.rear - self.front + 1 >= self.capacity:
            return "queue overflow", self.queue.copy()

        self.queue.append(value)
        self.rear += 1
        return "enqueued", self.queue.copy()

    def dequeue(self):
        if self.front > self.rear:
            return "queue underflow", self.queue.copy()

        value = self.queue[self.front]
        self.front += 1
        return "dequeued", value, self.queue[self.front:].copy()

    def peek(self):
        if self.front > self.rear:
            return "queue is empty", None

        return "peek", self.queue[self.front]
