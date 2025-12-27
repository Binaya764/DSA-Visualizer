import sys
import random
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QColor

# UI
from ui_form import Ui_Widget

# Colors
soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(144, 238, 144)
soft_red    = QColor(240, 128, 128)
soft_yellow = QColor(240, 200, 120)

# =========================
# Visualizers & Algorithms
# =========================
from visualizer.sorting_viz.insertionSort_visualizer import InsertionSortVisualizer
from visualizer.sorting_viz.mergeSort_visualizer import mergeSort_Visualizer
from visualizer.code_visualizer import code_Visualizer, ALGORITHM_CODES

from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort

# =========================
# Main Widget Class
# =========================
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Visualizers
        self.active_visualizer = None
        self.visualizer2 = None  # Reference view, make sure you add graphicsView for it in UI
        self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView)

        # Animation variables
        self.steps = []
        self.current_step = 0
        self.current_array = []
        self.active_algorithm = None
        self.animation_speed = 500

        # =========================
        # Connect Buttons
        # =========================
        self.ui.Btnstart.clicked.connect(self.start_sort)
        # Reuse Insertion Sort buttons for both algorithms
        self.ui.BtnRandomize_InsertionSort.clicked.connect(lambda: self.random_array())
        self.ui.BtnGenerate_InsertionSort.clicked.connect(lambda: self.custom_array())

        # Combobox
        self.ui.sort_comboBox.currentTextChanged.connect(self.on_sort_changed)
        self.ui.speed_comboBox.currentTextChanged.connect(self.change_speed)

        # Initialize defaults
        self.initialize_defaults()

    # =========================
    # Initialization & Speed
    # =========================
    def initialize_defaults(self):
        self.ui.sort_comboBox.setCurrentIndex(0)
        self.on_sort_changed(self.ui.sort_comboBox.currentText())

    def change_speed(self, text):
        speed_map = {"1x":500, "0.50x":800, "0.75x":600, "0.25x":1500,
                     "1.25x":400, "1.5x":300, "2x":200, "3x":100}
        self.animation_speed = speed_map.get(text, 500)

    # =========================
    # Sort selection
    # =========================
    def on_sort_changed(self, algo):
        algo = algo.strip().title()
        self.active_algorithm = algo
        print("Sort selected:", self.active_algorithm)

        if algo == "Insertion Sort":
            self.active_visualizer = InsertionSortVisualizer(self.ui.visualizer_graphicsView)
            self.currCode_visualizer.show_code(ALGORITHM_CODES.get(algo, ""))
        elif algo == "Merge Sort":
            self.active_visualizer = mergeSort_Visualizer(self.ui.visualizer_graphicsView)
            self.currCode_visualizer.show_code(ALGORITHM_CODES.get(algo, ""))
        else:
            print("No valid algorithm selected")
            return

        # Clear scene
        self.active_visualizer.scene.clear()
        if self.visualizer2:
            self.visualizer2.scene.clear()

    # =========================
    # Sorting
    # =========================
    def start_sort(self):
        if not self.current_array:
            print("Array is empty!")
            return

        if self.active_algorithm == "Insertion Sort":
            self.steps = insertion_sort(self.current_array.copy())
            self.current_step = 0
            self.play_insertion_sort()
        elif self.active_algorithm == "Merge Sort":
            self.steps = merge_sort(self.current_array.copy())
            self.current_step = 0
            self.play_merge_sort()

    # =========================
    # Animation Functions
    # =========================
    def play_insertion_sort(self):
        if self.current_step >= len(self.steps):
            self.active_visualizer.completed_sort()
            return
        step_type, i, j, state = self.steps[self.current_step]
        self.active_visualizer.draw_array(state)
        if step_type == "compare":
            self.active_visualizer.highlight(i, j, soft_yellow)
        elif step_type == "shift":
            self.active_visualizer.highlight(i, j, soft_red)
        elif step_type == "insert":
            self.active_visualizer.highlight(i, i, soft_green)
        elif step_type == "key":
            self.active_visualizer.highlight(i, i, soft_blue)
        self.current_step += 1
        QTimer.singleShot(self.animation_speed, self.play_insertion_sort)

    def play_merge_sort(self):
        if self.current_step >= len(self.steps):
            self.active_visualizer.completed_sort()
            return
        step_type, i, j, state = self.steps[self.current_step]
        self.active_visualizer.draw_array(state)
        if step_type == "compare":
            self.active_visualizer.highlight(i, j, Qt.yellow)
        elif step_type == "overwrite":
            self.active_visualizer.highlight(i, j, Qt.blue)
        self.current_step += 1
        QTimer.singleShot(self.animation_speed, self.play_merge_sort)

    # =========================
    # Array Generation
    # =========================
    def random_array(self):
        size_txt = self.ui.size_array_lineEdit_InsertionSort.text()
        if not size_txt:
            print("Enter size!")
            return
        size = int(size_txt)
        arr = [random.randint(1, 100) for _ in range(size)]
        self.current_array = arr
        self.active_visualizer.draw_array(arr)
        if self.visualizer2:
            self.visualizer2.ref_drawArray(arr)

    def custom_array(self):
        size_txt = self.ui.size_array_lineEdit_InsertionSort.text()
        custom_arr_txt = self.ui.CArray_lineEdit_InsertionSort.text()
        if not size_txt or not custom_arr_txt:
            print("Enter size and array!")
            return
        size = int(size_txt)
        arr = [int(x) for x in custom_arr_txt.replace(",", " ").split()]
        if len(arr) != size:
            print("Array size does not match!")
            return
        self.current_array = arr
        self.active_visualizer.draw_array(arr)
        if self.visualizer2:
            self.visualizer2.ref_drawArray(arr)

# =========================
# Run Application
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
