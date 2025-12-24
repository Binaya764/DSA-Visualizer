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
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

"""

BINARY_SEARCH_CODE = """
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

SELECTION_SORT_CODE= """ """

ALGORITHM_CODES = {
    "Bubble Sort": BUBBLE_SORT_CODE,
    "Binary Search": BINARY_SEARCH_CODE,
    "Insertion Sort":INSERTION_SORT_CODE,
    "Selection Sort": SELECTION_SORT_CODE,
    "Stack": STACK_CODE,

}
