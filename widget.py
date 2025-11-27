import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer, Qt

# Import UI
from ui_form import Ui_Widget

# Import Visualizer + Algorithms
from visualizer.sorting_visualizer import sort_Visualizer
from algorithms.sorting.Bubble_sort import bubble_sort


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create visualizer for the graphicsView
        self.visualizer = sort_Visualizer(self.ui.graphicsView)

        # Animation variables
        self.steps = []
        self.current_step = 0

        # Connect Start Button
        self.ui.Btnstart.clicked.connect(self.start_sort)
        self.ui.Btnrandomize.clicked.connect(self.random_array)
        # NOTE: change button name if yours is different (pushButton_2, startButton, etc.)

    # ----------------------------------------------------------------------
    # Start Sorting
    # ----------------------------------------------------------------------
    def start_sort(self):
        # Using sample array for now
        arr = [4, 1, 3, 2,24,56,32,67,34]

        # Draw initial array
        self.visualizer.draw_array(arr)

        # Get bubble sort steps
        self.steps = bubble_sort(arr)

        self.current_step = 0
        self.play_step()

    # ----------------------------------------------------------------------
    # Play Animation Step-by-Step
    # ----------------------------------------------------------------------
    def play_step(self):
        if self.current_step >= len(self.steps):
            return  # animation finished

        step_type, i, j, state = self.steps[self.current_step]

        # Highlight comparisons
        if step_type == "compare":
            self.visualizer.draw_array(state)
            self.visualizer.highlight(i, j, Qt.yellow)

        # Swap bars and highlight them
        elif step_type == "swap":
            self.visualizer.swap_bars(state, i, j)
            self.visualizer.highlight(i, j, Qt.red)


        self.current_step += 1

        # Delay for next step (speed control)
        QTimer.singleShot(600, self.play_step)


    def random_array(self):
        size= int(self.ui.size_array_lineEdit.text())
        print(size)



# --------------------------------------------------------------------------
# Run Application
# --------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
