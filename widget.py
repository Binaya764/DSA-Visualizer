import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer, Qt

# Import UI
from ui_form import Ui_Widget

# Import Visualizer and  algorithms

#For Bubble sort
from visualizer.sorting_visualizer import sort_Visualizer
from visualizer.sorting_visualizer import code_Visualizer
from algorithms.sorting.Bubble_sort import bubble_sort
import random


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create visualizer for the graphicsView
        self.visualizer = sort_Visualizer(self.ui.visualizer_graphicsView)
        self.visualizer2 = code_Visualizer(self.ui.code_graphicsView)

        # Animation variables
        self.steps = []
        self.current_step = 0
        self.current_array=[] #Stores the current updated array

        # Connect Start Button
        self.ui.Btnstart.clicked.connect(self.start_sort) #connects start button
        self.ui.Btnrandomize.clicked.connect(self.random_array) #conncts the randomize button
        self.ui.BtnGenerate.clicked.connect(self.custom_array) #connects the generate button


    def start_sort(self):   #for sorting

        # Get bubble sort steps
        self.steps = bubble_sort(self.current_array.copy())

        self.current_step = 0
        self.play_step()


    def play_step(self):        #plays animation
        if self.current_step >= len(self.steps):
           self.visualizer.completed_sort()
           return# animation finished

        step_type, i, j, state = self.steps[self.current_step]

        # Highlight comparisons
        if step_type == "compare":
            self.visualizer.draw_array(state)
            self.visualizer.highlight(i, j, Qt.green)

        # Swap bars and highlight them
        elif step_type == "swap":
            self.visualizer.swap_bars(state, i, j)
            self.visualizer.highlight(i, j, Qt.green)


        self.current_step += 1

        # Controls the speed of the animation
        QTimer.singleShot(400, self.play_step)


    def random_array(self):  #Generates random array
        size= int(self.ui.size_array_lineEdit.text())
        print(size)
        arr=[random.randint(1,100) for _ in range(size)]
        self.visualizer.ref_drawArray(arr)
        self.visualizer.draw_array(arr)
        self.current_array = arr


    def custom_array(self): #Gets array input from the user
        size_txt = self.ui.size_array_lineEdit.text()  #gets the size of the array
        custom_arr = self.ui.custom_array_lineEdit.text() #gets the custom array

        if size_txt == "" or custom_arr == "":
                return

        size = int(size_txt)

        parts = custom_arr.replace(",", " ").split() #splits the string into individual values

        if len(parts) != size:
                print("Array size does not match!")
                return
        else:

                arr = [int(x) for x in parts]

                self.current_array = arr
                self.visualizer.draw_array(arr)




#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
