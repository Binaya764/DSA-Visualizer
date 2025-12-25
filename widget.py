import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer, Qt

# Import UI
from ui_form import Ui_Widget
from PySide6.QtGui import QColor

soft_blue   = QColor(100, 149, 237)   # Cornflower blue
soft_green  = QColor(144, 238, 144)   # Light green
soft_red    = QColor(240, 128, 128)   # Light coral
soft_gray   = QColor(200, 200, 200)   # Light gray
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)


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

#For Insertion Sort
from algorithms.sorting.insertion_sort import Insertion_sort
from visualizer.Sorting_viz.InsertionSort_visualizer import  insertionSort_Visualizer

#For Stack
from algorithms.Stack import stack_fun
from visualizer.Stack_visualizer import StackVisualizer

#For Queue
from algorithms.Queue.Queue_algo import queue_fun
from visualizer.queue_viz.Queue_visualizer import QueueVisualizer

#For selection sort
from algorithms.sorting.Selection_sort import selection_sort
from visualizer.Sorting_viz.SelectionSort_visualizer import SelectionSortVisualizer

#For Linear search
from algorithms.Searching.Linear_search import linear_search
from visualizer.searching_viz.LinearSearch_Visualizer import Linear_Visualizer




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
        self.stack = stack_fun(capacity=5)
        self.queue = queue_fun(capacity = 10)

        # Connect Start Button
        #for Bubble sort
        self.ui.Btnstart.clicked.connect(self.start_sort) #connects start button

        self.ui.Btnrandomize.clicked.connect(lambda: self.random_array("Bubble_sort"))
        self.ui.Btnrandomize_Bsearch.clicked.connect(lambda: self.random_array("Binary_search"))
        self.ui.BtnRandomize_InsertionSort.clicked.connect(lambda: self.random_array("Insertion_sort"))

        self.ui.BtnGenerate.clicked.connect(lambda: self.custom_array("Bubble_sort"))
        self.ui.BtnGenerate_Bsearch.clicked.connect(lambda: self.custom_array("Binary_search"))
        self.ui.BtnGenerate_InsertionSort.clicked.connect(lambda: self.custom_array("Insertion_sort"))

        #Button for Stack
        self.ui.BtnPush_stack.clicked.connect(lambda: self.push_stack("Stack"))
        self.ui.BtnPop_stack.clicked.connect(lambda: self.pop_stack("Stack"))
        self.ui.BtnPeek_stack.clicked.connect(lambda: self.peek_stack("Stack"))

        #Button for Queue
        self.ui.Btn_Equeue.clicked.connect(lambda: self.enqueue_queue("Queue"))
        self.ui.Btn_Dequeue.clicked.connect(lambda: self.dequeue_queue("Queue"))

        #Button for Selection sort
        self.ui.BtnGenerate_SelectionSort.clicked.connect(lambda: self.custom_array("Selection_sort"))
        self.ui.BtnRandomize_SelectionSort.clicked.connect(lambda: self.random_array("Selection_sort"))

        #Button for linear search
        self.ui.BtnRandomize_LSearch.clicked.connect(lambda: self.random_array("Linear_search"))
        self.ui.BtnGenerate_LSearch.clicked.connect(lambda: self.custom_array("Linear_search"))









        #connect combobox
        self.ui.sort_comboBox.currentTextChanged.connect(self.on_sort_changed)
        self.ui.search_comboBox.currentTextChanged.connect(self.on_search_changed)
        self.ui.speed_comboBox.currentTextChanged.connect(self.change_speed)
        self.ui.DS_comboBox.currentTextChanged.connect(self.on_dataStructure_changed)

        self.active_algorithm = None
        self.currCode_visualizer = None
        self.animation_speed = 500

    def change_speed(self,text):
            speed_map ={
            "1x" : 500,
            "0.50x" : 800,
            "0.75x" : 600,
            "0.25x"  : 1500,
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
                "Insertion Sort": 2,

            }
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo, 0))
            self.active_algorithm = algo
            self.active_visualizer = self.visualizer
            if algo == "Bubble Sort":
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])

            elif algo =="Insertion Sort":
                    self.active_visualizer = insertionSort_Visualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_InsertionSort)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])

            elif algo == "Selection Sort":
                    self.active_visualizer = SelectionSortVisualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_SelectionSort)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])




            self.active_visualizer.scene.clear()
            self.visualizer2.scene.clear()
            #self.visualizer3.scene.clear()

    def on_search_changed(self,algo):
            mapping = {
            "Linear Search": 3,
            "Binary Search": 4,
            }
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo, 2))
            self.active_algorithm= algo


            if algo == "Binary Search":
                self.active_visualizer = Binary_Visualizer(self.ui.visualizer_graphicsView )
                self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_Bsearch)
                self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])

            if algo == "Linear Search":
                self.active_visualizer = Linear_Visualizer(self.ui.visualizer_graphicsView )
                self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_LSearch)
                self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])


            self.active_visualizer.scene.clear()
            self.visualizer2.scene.clear()
            #self.visualizer3.scene.clear()

    def on_dataStructure_changed(self,algo):
            mapping = {
            "Stack": 5,
            "Queue": 6,}
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo,4))
            self.active_algorithm = algo
            if algo == "Stack":
                    self.active_visualizer = StackVisualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_stack)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])
            elif algo == "Queue":
                    self.active_visualizer = QueueVisualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_Queue)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])
            self.active_visualizer.scene.clear()
            self.visualizer.scene.clear()


      #for sorting

    def start_sort(self):

        if self.active_algorithm == "Bubble Sort":
            self.steps = bubble_sort(self.current_array.copy())
            self.play_step()

        elif self.active_algorithm == "Insertion Sort":
                print("Insertion sort called")
                self.steps = Insertion_sort(self.current_array.copy())
                self.play_Insertion_sort()

        elif self.active_algorithm == "Selection Sort":
                self.steps = selection_sort(self.current_array.copy())
                self.play_selection_sort()

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

        elif self.active_algorithm == "Linear Search":
                target_text = self.ui.target_lineEdit_LSearch.text().strip()
                if target_text == "":
                        print("Please enter a target value for linear Search!")
                        return
                try:
                        self.target = int(target_text)
                except ValueError:
                        print("Invalid input! Enter a number.")
                        return
                steps, found = linear_search(self.current_array.copy(),self.target)
                self.current_step = 0
                self.play_linear_search(steps)


        else:
            print("No algorithm selected!")

    def play_linear_search(self,steps):
            if self.current_step >= len(steps):
                return

            step_type, index ,state= steps[self.current_step]

            # Draw the array
            self.active_visualizer.draw_array(state)

            if step_type == "check":
                print("checking")
                self.active_visualizer.highlight(index)

            elif step_type == "found":
                print("found")
                self.active_visualizer.found(index)

            elif step_type == "not_found":
                for i in range(len(state)):
                    self.active_visualizer.highlight(i)

            self.current_step += 1
            QTimer.singleShot(self.animation_speed, lambda: self.play_linear_search(steps))


    def play_selection_sort(self):
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

    def play_Insertion_sort(self):
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
                    QTimer.singleShot(self.animation_speed, self.play_step)










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


    def random_array(self,source="Bubble_sort"):  #Generates random array
        if source == "Bubble_sort":
                size= int(self.ui.size_array_lineEdit.text())  # Sorting size input

        elif source == "Insertion_sort":
                print("Random array insertion sort called")
                size= int(self.ui.size_array_lineEdit_InsertionSort.text())

        elif source == "Binary_search":
                size = int(self.ui.size_array_lineEdit_Bsearch.text())  # Searching size input

        elif source == "Selection_sort":
                size = int(self.ui.size_array_lineEdit_SelectionSort.text())

        elif source == "Binary_search":
                size = int(self.ui.size_array_lineEdit_BSearch.text())
        elif source == "Linear_search":
                size = int(self.ui.size_array_lineEdit_LSearch.text())


        else:
                return
        print(size)
        arr=[random.randint(1,100) for _ in range(size)]
        self.active_visualizer.draw_array(arr)
        self.visualizer2.ref_drawArray(arr)

        self.current_array = arr


    def custom_array(self,source ="Bubble_sort"): #Gets array input from the user

        if source == "Bubble_sort":
                size_txt= int(self.ui.size_array_lineEdit.text())  # Sorting size input
                custom_arr = self.ui.custom_array_lineEdit.text()
        elif source == "Binary_search":
                size_txt = int(self.ui.size_array_lineEdit_Bsearch.text())  # Searching size input
                custom_arr = self.ui.lineEdit_Bsearch.text()

        elif source == "Insertion_sort":
                size_txt = int(self.ui.size_array_lineEdit_InsertionSort.text())
                custom_arr = self.ui.CArray_lineEdit_InsertionSort.text()

        elif source == "Selection_sort":
                size_txt = int(self.ui.size_array_lineEdit_SelectiontionSort.text())
                custom_arr = self.ui.CArray_lineEdit_SelectionSort.text()

        elif source == "Linear_search":
                size_txt = int(self.ui.size_array_lineEdit_LSearch.text())
                custom_arr = self.ui.CArray_lineEdit_LSearch.text()


        else:
                return


        if size_txt == "" or custom_arr == "":
                print("input the required size and value for customr array!")
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

        #for stacks
    def push_stack(self,source ="Stack"):
        value_text = self.ui.Stack_lineEdit.text().strip()
        if not value_text:
                return

        try:
                value = int(value_text)
        except ValueError:
                print("Invalid input")
                return

        action, state = self.stack.push(value)

        if action == "overflow":
                print("Stack overflow!")
        else:
                self.active_visualizer.draw_stack(state)

        self.ui.Stack_lineEdit.clear()

    def pop_stack(self,source = "Stack"):
        action, value,state = self.stack.pop()

        if action == "underflow":
                print("Stack Underflow!")
        else:
                self.active_visualizer.draw_stack(state)

    def peek_stack(self,source = "Stack"):
        action, value, state = self.stack.peek()
        if action == "underflow":
                print("Stack is empty!")
        else:
                self.active_visualizer.draw_stack(state)

        #Functions for Queue
    def enqueue_queue(self,source = "Queue"):
            value_text = self.ui.lineEdit_Queue.text().strip()
            if not value_text:
                    return

            try:
                    value = int(value_text)
            except ValueError:
                    print("Invalid input")
                    return

            action, state = self.queue.enqueue(value)

            if action == "overflow":
                    print("Queue overflow!")
            else:
                    self.active_visualizer.draw_queue(state)

            self.ui.lineEdit_Queue.clear()

    def dequeue_queue(self, source = "Queue"):
                action,value, state = self.queue.dequeue()
                if action == "underflow":
                        print("Queue underflow!")
                else:
                        self.active_visualizer.draw_queue(state)










#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
