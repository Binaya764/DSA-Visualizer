import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer, Qt

# Import UI
from ui_form import Ui_Widget

# Import Visualizer and  algorithms

#For Bubble sort
from visualizer.sorting_visualizer import sort_Visualizer
from algorithms.sorting.Bubble_sort import bubble_sort
import random


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
        self.current_array=[] #Stores the current updated array

        # Connect Start Button
        self.ui.Btnstart.clicked.connect(self.start_sort) #connects start button
        self.ui.Btnrandomize.clicked.connect(self.random_array) #conncts the randomize button


    def start_sort(self,arr):   #for sorting

        # Get bubble sort steps
        self.steps = bubble_sort(self.current_array)

        self.current_step = 0
        self.play_step()


    def play_step(self):        #plays animation
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

        # Controls the speed of the animation
        QTimer.singleShot(600, self.play_step)


    def random_array(self):  #Generates random array
        size= int(self.ui.size_array_lineEdit.text())
        print(size)
        arr=[random.randint(1,100) for _ in range(size)]
        self.visualizer.draw_array(arr)
        self.current_array = arr



#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
