# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
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
        y = 0
        for line in code_text.split("\n"):
            item = QGraphicsSimpleTextItem(line)
            item.setBrush(Qt.white)
            item.setPos(-5, y)
            self.scene.addItem(item)
            y += 25  # line spacing


# Only keep insertion sort and merge sort
ALGORITHM_CODES = {
    "Insertion Sort": """
Time complexity = O(n²)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
""",
    "Merge Sort": """
Time complexity = O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
"""
}
