import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer, Qt

# Import UI
from ui_form import Ui_Widget

# Import Visualizer and  algorithms

#For Bubble sort
from visualizer.sorting_visualizer import sort_Visualizer
from visualizer.Code_visualizer import code_Visualizer
from visualizer.Code_visualizer import ALGORITHM_CODES
from visualizer.sorting_visualizer import ref_Visualizer
from algorithms.sorting.Bubble_sort import bubble_sort

#For Binary search
from algorithms.Searching.Binary_Search import binary_search
from visualizer.searching_viz.BinarySearch_visualizer import Binary_Visualizer


import random


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create visualizer for the graphicsView
        self.visualizer = sort_Visualizer(self.ui.visualizer_graphicsView)
        self.visualizer2 = ref_Visualizer(self.ui.ref_graphicsView)
        self.visualizer3 = code_Visualizer(self.ui.code_graphicsView)


        self.active_visualizer= self.visualizer
        self.currCode_visualizer = self.visualizer3

        # Animation variables
        self.steps = []
        self.current_step = 0
        self.current_array=[] #Stores the current updated array

        # Connect Start Button
        #for Bubble sort
        self.ui.Btnstart.clicked.connect(self.start_sort) #connects start button

        self.ui.Btnrandomize.clicked.connect(lambda: self.random_array("sort"))
        self.ui.Btnrandomize_Bsearch.clicked.connect(lambda: self.random_array("search"))

        self.ui.BtnGenerate.clicked.connect(lambda: self.custom_array("sort"))
        self.ui.BtnGenerate_Bsearch.clicked.connect(lambda: self.custom_array("search"))




        #connect combobox
        self.ui.sort_comboBox.currentTextChanged.connect(self.on_sort_changed)
        self.ui.search_comboBox.currentTextChanged.connect(self.on_search_changed)
        self.ui.speed_comboBox.currentTextChanged.connect(self.change_speed)

        self.active_algorithm = None
        self.currCode_visualizer = None
        self.animation_speed = 500

    def change_speed(self,text):
            speed_map ={
            "1x" : 500,
            "0.50x" : 800,
            "0.75x" : 600,
            "0.25"  : 1000,
            "1.25x" : 400,
            "1.5x" : 300,
            "2x" : 200,
            "3x" : 100,}
            self.animation_speed = speed_map.get(text, 500)
            print("Animation speed set to:", self.animation_speed)

    def on_sort_changed(self, algo):
            mapping = {
                "Bubble Sort": 0,
                "Selection Sort": 1,

            }
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo, 0))
            self.active_algorithm = algo
            self.active_visualizer = self.visualizer
            if algo == "Bubble Sort":
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])


            self.active_visualizer.scene.clear()
            self.visualizer2.scene.clear()
            #self.visualizer3.scene.clear()

    def on_search_changed(self,algo):
            mapping = {
            "Linear Search": 2,
            "Binary Search": 3,
            }
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo, 2))
            self.active_algorithm= algo


            if algo == "Binary Search":
                self.active_visualizer = Binary_Visualizer(self.ui.visualizer_graphicsView )
                self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_Bsearch)
                self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])

            self.active_visualizer.scene.clear()
            self.visualizer2.scene.clear()
            #self.visualizer3.scene.clear()


      #for sorting

    def start_sort(self):

        if self.active_algorithm == "Bubble Sort":
            self.steps = bubble_sort(self.current_array.copy())
            self.play_step()

        elif self.active_algorithm == "Binary Search":
                target_text = self.ui.target_lineEdit.text().strip()
                if target_text == "":
                        print("Please enter a target value for Binary Search!")
                        return
                try:
                        self.target = int(target_text)
                except ValueError:
                        print("Invalid input! Enter a number.")
                        return
                steps = binary_search(self.current_array.copy(), self.target)
                self.current_step = 0
                self.play_binary_search(steps)


        else:
            print("No algorithm selected!")

    def play_binary_search(self, steps):
                if self.current_step >= len(steps):
                    return

                step_type, index, state = steps[self.current_step]

                # Draw the array
                self.active_visualizer.draw_array(state)

                if step_type == "check":
                    print("checking")
                    self.active_visualizer.highlight(index, index, Qt.yellow)

                elif step_type == "found":
                    print("found")
                    self.active_visualizer.found(index)

                elif step_type == "not_found":
                    for i in range(len(state)):
                        self.active_visualizer.highlight(i, i, Qt.red)

                self.current_step += 1
                QTimer.singleShot(self.animation_speed, lambda: self.play_binary_search(steps))




    def play_step(self):        #plays animation
        if self.current_step >= len(self.steps):
           self.active_visualizer.completed_sort()
           return# animation finished

        step_type, i, j, state = self.steps[self.current_step]

        # Highlight comparisons
        if step_type == "compare":
            self.active_visualizer.draw_array(state)
            self.active_visualizer.highlight(i, j, Qt.green)

        # Swap bars and highlight them
        elif step_type == "swap":
            self.active_visualizer.swap_bars(state, i, j)
            self.active_visualizer.highlight(i, j, Qt.green)


        self.current_step += 1

        # Controls the speed of the animation
        QTimer.singleShot(self.animation_speed, self.play_step)


    def random_array(self,source="sort"):  #Generates random array
        if source == "sort":
                size= int(self.ui.size_array_lineEdit.text())  # Sorting size input
        elif source == "search":
                size = int(self.ui.size_array_lineEdit_Bsearch.text())  # Searching size input
        else:
                return
        print(size)
        arr=[random.randint(1,100) for _ in range(size)]
        self.active_visualizer.draw_array(arr)
        self.visualizer2.ref_drawArray(arr)

        self.current_array = arr


    def custom_array(self,source ="sort"): #Gets array input from the user

        if source == "sort":
                size_txt= int(self.ui.size_array_lineEdit.text())  # Sorting size input
                custom_arr = self.ui.custom_array_lineEdit.text()
        elif source == "search":
                size_txt = int(self.ui.size_array_lineEdit_Bsearch.text())  # Searching size input
                custom_arr = self.ui.lineEdit_Bsearch.text()
        else:
                return


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
                self.visualizer2.ref_drawArray(arr)
                self.active_visualizer.draw_array(arr)




#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
