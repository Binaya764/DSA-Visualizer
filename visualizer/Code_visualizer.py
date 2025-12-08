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
            item.setPos(0, y)
            self.scene.addItem(item)
            y += 20   # line spacing


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

ALGORITHM_CODES = {
    "Bubble Sort": BUBBLE_SORT_CODE,
    "Binary Search": BINARY_SEARCH_CODE,

}
