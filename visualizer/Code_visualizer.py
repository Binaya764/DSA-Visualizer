from PySide6.QtWidgets import QGraphicsScene, QGraphicsSimpleTextItem
from PySide6.QtGui import Qt

class code_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

    def show_code(self, code_text: str):
        """Displays multi-line code inside the QGraphicsScene."""
        self.scene.clear()
        print("show code called")

        y = 0
        for line in code_text.split("\n"):
            item = QGraphicsSimpleTextItem(line)
            item.setBrush(Qt.white)
            item.setPos(-5, y)
            self.scene.addItem(item)
            y += 25   # line spacing


# Store your codes in constants or a dictionary

BUBBLE_SORT_CODE = """
Time complexity = O(n²)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

"""

BINARY_SEARCH_CODE = """
Time complexity = O(log n)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

"""
INSERTION_SORT_CODE="""
Time complexity = O(n²)
def Insertion_sort(arr):
    steps = []
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Highlight key
        steps.append(("key", i, j, arr.copy()))

        while j >= 0 and arr[j] > key:
            # Compare
            steps.append(("compare", j, j + 1, arr.copy()))

            arr[j + 1] = arr[j]  # shift
            steps.append(("shift", j, j + 1, arr.copy()))

            j -= 1

        arr[j + 1] = key
        steps.append(("insert", j + 1, i, arr.copy()))

    return steps

"""

STACK_CODE="""
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
        return "pushed", self.stack.copy()

    def pop(self):
        if self.top == -1:
            return "stack underflow", self.stack.copy()
        value = self.stack.pop()
        self.top -= 1
        return "popped", value, self.stack.copy()

    def peek(self):
        if self.top == -1:
            return "stack is empty", None
        return "peek", self.stack[self.top]


"""
QUEUE_CODE= """
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

"""


SELECTION_SORT_CODE= """
Time complexity = O(n²)
def selection_sort(arr):
    steps = []
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps.append(("compare", min_idx, j, arr.copy()))
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(("swap", i, min_idx, arr.copy()))

    return steps

"""

LINEAR_SEARCH_CODE= """
def linear_search(arr, target):
    steps = []

    for i in range(len(arr)):
        steps.append(("check", arr.copy()))


        if arr[i] == target:
            steps.append(("found",arr.copy()))
            return steps, True  # found

    steps.append(("not found",arr.copy()))

    return steps, False  # not found"""

MERGE_SORT_CODE="""

def merge_Sort(arr):

    steps = []

    def merge(left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            steps.append(("compare", left + i, mid + 1 + j, arr.copy()))
            if L[i] <= R[j]:
                arr[k] = L[i]
                steps.append(("overwrite", k, left + i, arr.copy()))
                i += 1
            else:
                arr[k] = R[j]
                steps.append(("overwrite", k, mid + 1 + j, arr.copy()))
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            steps.append(("overwrite", k, left + i, arr.copy()))
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            steps.append(("overwrite", k, mid + 1 + j, arr.copy()))
            j += 1
            k += 1

    def merge_sort_recursive(left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(left, mid)
            merge_sort_recursive(mid + 1, right)
            merge(left, mid, right)

    merge_sort_recursive(0, len(arr) - 1)
    return steps"""
LINKED_LIST_CODE = """

"""

BST_CODE = """
"""

ALGORITHM_CODES = {
    "Bubble Sort": BUBBLE_SORT_CODE,
    "Binary Search": BINARY_SEARCH_CODE,
    "Insertion Sort":INSERTION_SORT_CODE,
    "Selection Sort": SELECTION_SORT_CODE,
    "Stack": STACK_CODE,
    "Linear Search":   LINEAR_SEARCH_CODE,
    "Queue" : QUEUE_CODE,
    "Merge Sort": MERGE_SORT_CODE,
    "Linked List": LINKED_LIST_CODE,
    "Binary Search Tree": BST_CODE,

}
