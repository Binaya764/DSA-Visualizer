import sys
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from PySide6.QtCore import QTimer

# Import
from ui_form import Ui_Widget
from PySide6.QtGui import QColor,QIntValidator,QBrush

soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(46, 125, 50)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)
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

#For Merge sort
from algorithms.sorting.merge_sort import merge_Sort
from visualizer.Sorting_viz.mergeSort_visualizer import mergeSort_Visualizer

#For LinkedList
from algorithms.Linked_List.singly_LinkedList import linkedList_fun
from visualizer.LinkedList_viz.singly_LinkedList_visualizer import LinkedListVisualizer

#For BST
from algorithms.BST.Binary_Search_Tree import BinarySearchTree
from visualizer.BST_viz.BST_visualizer import BST_Visualizer

#FOR BFS
from visualizer.BFS_viz.BFS_visualizer import GraphGenerator,BFSvisualizer,QueueVisualizerBFS

#For DFS
from algorithms.DFS.DFS_algo import dfs_fun
from visualizer.DFS_viz.DFS_visualizer import GraphGenerator, DFSvisualizer,StackVisualizerDFS

import random


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create visualizer for the graphicsView
        self.visualizer = sort_Visualizer(self.ui.visualizer_graphicsView) #main display visualizer
        self.visualizer2 = ref_Visualizer(self.ui.ref_graphicsView)        #display where only original array is displayes
        self.visualizer3 = code_Visualizer(self.ui.code_graphicsView)      #display where the code is displayed


        self.active_visualizer= self.visualizer #creating a varible active_visualizer for all visualizers
        self.currCode_visualizer = self.visualizer3

        # Animation variables
        self.steps = []                                 #stores the animation steps
        self.current_step = 0                           #initializs the first step to be 0
        self.current_array=[]                           #Stores the current updated array
        self.stack = stack_fun(capacity=5)              #creating a stack var for stack algorithm
        self.queue = queue_fun(capacity = 5)
        self.linked_list = linkedList_fun(capacity =5)
        self.BST = BinarySearchTree()
        self.explain_label = self.ui.Explanation_label
        self.extra_edges = 4


        # Connect Start Button
        self.ui.Btnstart.clicked.connect(self.start_sort) #connects start button

        #Button for Bubble sort
        self.ui.Btnrandomize.clicked.connect(lambda: self.random_array("Bubble_sort"))
        self.ui.BtnGenerate.clicked.connect(lambda: self.custom_array("Bubble_sort"))

        #Button for Binary search:
        self.ui.BtnGenerate_Bsearch.clicked.connect(lambda: self.CArray_Bsearch("Binary_search"))
        self.ui.Btnrandomize_Bsearch.clicked.connect(lambda: self.sorted_array("Binary_search"))

        #Buttton for Insertion search:
        self.ui.BtnGenerate_InsertionSort.clicked.connect(lambda: self.custom_array("Insertion_sort"))
        self.ui.BtnRandomize_InsertionSort.clicked.connect(lambda: self.random_array("Insertion_sort"))

        #Button for Stack
        self.ui.BtnPush_stack.clicked.connect(lambda: self.push_stack("Stack"))
        self.ui.BtnPop_stack.clicked.connect(lambda: self.pop_stack("Stack"))
        self.ui.BtnClear_stack.clicked.connect(lambda: self.clear_stack("Stack"))

        #Button for Queue
        self.ui.Btn_Equeue.clicked.connect(lambda: self.enqueue_queue("Queue"))
        self.ui.Btn_Dequeue.clicked.connect(lambda: self.dequeue_queue("Queue"))
        self.ui.BtnClear_Queue.clicked.connect(lambda: self.clear_queue("Queue"))

        #Button for Selection sort
        self.ui.BtnGenerate_SelectionSort.clicked.connect(lambda: self.custom_array("Selection_sort"))
        self.ui.BtnRandomize_SelectionSort.clicked.connect(lambda: self.random_array("Selection_sort"))

        #Button for linear search
        self.ui.BtnRandomize_LSearch.clicked.connect(lambda: self.random_array("Linear_search"))
        self.ui.BtnGenerate_LSearch.clicked.connect(lambda: self.custom_array("Linear_search"))

        #Button for Merge sort:
        self.ui.BtnRandomize_MergeSort.clicked.connect(lambda: self.random_array("Merge_sort"))
        self.ui.BtnGenerate_MergeSort.clicked.connect(lambda: self.custom_array("Merge_sort"))

        #Button for Linked List:
        self.ui.BtnInsert_LinkedList.clicked.connect(lambda: self.InsertHead_LinkedList("Linked_List"))
        self.ui.BtnRemove_LinkedList.clicked.connect(lambda: self.RemoveHead_LinkedList("Linked_List"))
        self.ui.BtnClear_LinkedList.clicked.connect(lambda: self.Clear_LinkedList("Linked_List"))
        self.ui.BtnInsertTail_LinkedList.clicked.connect(lambda: self.InsertTail_LinkedList("Linked_List"))
        self.ui.BtnRemoveTail_LinkedList.clicked.connect(lambda: self.RemoveTail_LinkedList("Linked_List"))

        #Button for BST:
        self.ui.BtnInsert_BST.clicked.connect(self.Insert_BST)
        self.ui.BtnRemove_BST.clicked.connect( self.Remove_BST)
        self.ui.BtnClear_BST.clicked.connect(self.Clear_BST)
        self.ui.BtnSearch_BST.clicked.connect(self.Search_BST)

        #Button for Breadth first search:
        self.ui.BtnTraverse_BFS.clicked.connect(self.Traverse_BFS)
        self.ui.BtnClear_BFS.clicked.connect(self.Clear_BFS)
        self.ui.BtnGenerate_BFS.clicked.connect(self.GenerateGraph_BFS)

        #Button for Depth first search
        self.ui.BtnTraverse_DFS.clicked.connect(self.Traverse_DFS)
        self.ui.BtnClear_DFS.clicked.connect(self.Clear_DFS)
        self.ui.BtnGenerate_DFS.clicked.connect(self.GenerateGraph_DFS)


        #connect combobox
        self.ui.sort_comboBox.currentTextChanged.connect(self.on_sort_changed)
        self.ui.search_comboBox.currentTextChanged.connect(self.on_search_changed)
        self.ui.speed_comboBox.currentTextChanged.connect(self.change_speed)
        self.ui.DS_comboBox.currentTextChanged.connect(self.on_dataStructure_changed)
        self.ui.HDST_comboBox.currentTextChanged.connect(self.on_HDataStucture_changed)
        self.ui.HDSG_comboBox.currentTextChanged.connect(self.on_HDataStuctureGraph_changed)

        #initializing default algorithm
        self.initialize_defaults()
        self.active_algorithm = None                    #Setting the active algorithm to be None
        self.currCode_visualizer = None
        self.animation_speed = 1500                      #Setting the defaul animatio speed 500ms

    def initialize_defaults(self):
            self.ui.sort_comboBox.setCurrentIndex(0)    #Initailzing the default display page
            self.on_sort_changed(self.ui.sort_comboBox.currentText())


    def change_speed(self,text):                        #Controls the speed
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


    def reset_all_comboboxes(self, except_box=None):    #Resets the combobox when another is selected
        comboboxes = [
            self.ui.sort_comboBox,              #sort combobox
            self.ui.search_comboBox,            #Search combobox
            self.ui.DS_comboBox,                #Linear data structure combobox
            self.ui.HDST_comboBox,               #Hierarchial data structure combobox
            self.ui.HDSG_comboBox,

        ]

        for box in comboboxes:
            if box is except_box:       #for not resetting the active combobox
                continue
            box.blockSignals(True)
            box.setCurrentIndex(0)  # reset to placeholder
            box.blockSignals(False)


    def on_sort_changed(self, algo):
            self.reset_all_comboboxes(except_box=self.ui.sort_comboBox)

            mapping = {
                "Bubble Sort": 1,               #represent the text or place of algorithm with its index in Qstacked widgets
                "Selection Sort": 2,
                "Insertion Sort": 3,
                "Merge Sort":4,

            }
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo, 0))
            self.active_algorithm = algo                  #Sets the current selected algorithm to be the active algorithm
            self.active_visualizer = self.visualizer      #sets the current visualizer to be the active visualizer
            if algo == "Bubble Sort":
                    self.active_visualizer = sort_Visualizer(self.ui.visualizer_graphicsView)  #connects the visualizer with the rescpective graphics-scene
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

            elif algo == "Merge Sort":
                    self.active_visualizer = mergeSort_Visualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_MergeSort)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])




            self.active_visualizer.scene.clear()                #clear the main display area
            self.active_visualizer.view.centerOn(0, 0)          #focuses the main screen to the center

            self.visualizer2.scene.clear()                      #clears the original array area
            self.visualizer2.view.centerOn(0, 0)



    def on_search_changed(self,algo):                           #combobox for the search algorithms
            self.reset_all_comboboxes(except_box=self.ui.search_comboBox)
            mapping = {
            "Linear Search": 5,
            "Binary Search": 6,
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
            self.active_visualizer.view.centerOn(0, 0)
            self.visualizer2.scene.clear()
            self.visualizer3.view.centerOn(0, 0)
            #self.visualizer3.scene.clear()

    def on_dataStructure_changed(self,algo):
            self.reset_all_comboboxes(except_box=self.ui.DS_comboBox)
            mapping = {
            "Stack": 7,
            "Queue": 8,
            "Linked List (singly)": 9,

            }
            self.ui.stackedWidget.setCurrentIndex(mapping.get(algo,4))
            self.active_algorithm = algo
            if algo == "Stack":
                    self.active_visualizer = StackVisualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_stack)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])
                    self.clear_stack()
            elif algo == "Queue":
                    self.active_visualizer = QueueVisualizer(self.ui.visualizer_graphicsView)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_Queue)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])
            elif algo == "Linked List (singly)":
                    self.active_visualizer = LinkedListVisualizer(self.ui.visualizer_graphicsView)
                    print(self.active_visualizer)
                    self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_LinkedList)
                    self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])

            self.active_visualizer.scene.clear()
            self.active_visualizer.view.centerOn(0, 0)
            self.visualizer2.scene.clear()


    def on_HDataStucture_changed(self,algo):
        self.reset_all_comboboxes(except_box = self.ui.HDST_comboBox)
        mapping = {
        "Binary Search Tree": 10,}

        self.ui.stackedWidget.setCurrentIndex(mapping.get(algo,5))
        self.active_algorithm = algo
        if algo == "Binary Search Tree":
                self.active_visualizer = BST_Visualizer(self.ui.visualizer_graphicsView)
                self.currCode_visualizer = code_Visualizer(self.ui.code_graphicsView_BST)
                self.currCode_visualizer.show_code(ALGORITHM_CODES[algo])

        self.active_visualizer.scene.clear()
        self.active_visualizer.view.centerOn(0,0)
        self.visualizer2.scene.clear()

    def on_HDataStuctureGraph_changed(self,algo):
        self.reset_all_comboboxes(except_box = self.ui.HDSG_comboBox)
        mapping = {
        "Breadth First Search (BFS)": 11,
        "Depth First Search (DFS)": 12,}

        self.ui.stackedWidget.setCurrentIndex(mapping.get(algo,5))
        self.active_algorithm = algo
        if algo == "Breadth First Search (BFS)":
                print("BFS called")
                self.active_visualizer = BFSvisualizer(self.ui.visualizer_graphicsView, self.ui.label_Traversal_path)
                self.visualizer3 = QueueVisualizerBFS(self.ui.code_graphicsView_BFS)

        elif algo == "Depth First Search (DFS)":
            self.active_visualizer = DFSvisualizer(self.ui.visualizer_graphicsView, self.ui.label_traversal_path)
            self.visualizer3 = StackVisualizerDFS(self.ui.code_graphicsView_DFS)


        self.active_visualizer.scene.clear()
        self.active_visualizer.view.centerOn(0,0)
        self.visualizer2.scene.clear()


        #when the start button is clicked it calls this function
    def start_sort(self):
        if self.active_algorithm == "Bubble Sort":
            self.steps = bubble_sort(self.current_array.copy()) #calls its algorithm
            self.current_step = 0
            self.play_step()            #calls the play step where it connects the algorithm and visualizer

        elif self.active_algorithm == "Insertion Sort":
                print("Insertion sort called")
                self.steps = Insertion_sort(self.current_array.copy())
                self.current_step =0
                self.play_Insertion_sort()

        elif self.active_algorithm == "Selection Sort":
                self.steps = selection_sort(self.current_array.copy())
                self.play_selection_sort()

        elif self.active_algorithm == "Merge Sort":
                self.steps = merge_Sort(self.current_array.copy())
                self.play_merge_sort()



        elif self.active_algorithm == "Binary Search":
                self.active_visualizer.scene.clear()
                self.active_visualizer.view.centerOn(0, 0)

                target_text = self.ui.target_lineEdit.text().strip()
                if not target_text.isdigit():
                    QMessageBox.warning(self, "Invalid Input", "Set a target value!")
                    return
                self.target = int(target_text)

                steps = binary_search(self.current_array.copy(), self.target)
                self.current_step = 0
                self.play_binary_search(steps)
                self.ui.target_lineEdit.clear()

        elif self.active_algorithm == "Linear Search":
                target_text = self.ui.target_lineEdit_LSearch.text().strip()
                if not target_text.isdigit():
                    QMessageBox.warning(self, "Invalid Input", "Enter an integer value")
                    return

                self.target = int(target_text)

                steps, found = linear_search(self.current_array.copy(),self.target)
                self.current_step = 0
                self.play_linear_search(steps)
                self.ui.target_lineEdit_LSearch.clear()

        else:
            print("No algorithm selected!")




    def play_step(self):  # plays animation

                if self.current_step >= len(self.steps):
                    self.active_visualizer.completed_sort()
                    self.explain_label.setText("Sorting completed ")
                    self.ui.Explanation_label.clear()
                    return

                step_type, i, j, state = self.steps[self.current_step]

                a = state[i]
                b = state[j]


                if step_type == "compare":
                    print("compared")

                    self.explain_label.setText(
                        f"Comparing {a} and {b}\n"

                    )

                    self.active_visualizer.draw_array(state)
                    self.active_visualizer.highlight(i, j, soft_yellow)


                elif step_type == "swap":
                    print("swapped")

                    self.explain_label.setText(
                        f"Swapping {b} and {a}\n"

                    )

                    self.active_visualizer.swap_bars(state, i, j)
                    self.active_visualizer.highlight(i, j, soft_blue)

                self.current_step += 1
                QTimer.singleShot(self.animation_speed, self.play_step)

    def play_merge_sort(self):
                # Check if all steps are done
                if self.current_step >= len(self.steps):
                    print("Merge sort completed")
                    self.active_visualizer.completed_sort()
                    return

                # Get current step
                action, i, j, arr_state = self.steps[self.current_step]

                # Highlight based on action
                if action == "compare":
                    print("compare called")
                    self.active_visualizer.draw_array(arr_state)
                    self.active_visualizer.highlight(i, j, soft_yellow)
                elif action == "overwrite":
                    print("overwrite called")
                    self.active_visualizer.draw_array(arr_state)
                    self.active_visualizer.highlight(i, i, soft_purple)

                # Move to next step
                self.current_step += 1

                # Schedule next step
                QTimer.singleShot(self.animation_speed, self.play_merge_sort)


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

            elif step_type == "not found":
                for i in range(len(state)):
                    self.active_visualizer.not_found(i)

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
                self.active_visualizer.highlight(i, j, soft_yellow)

            # Swap bars and highlight them
            elif step_type == "swap":
                self.active_visualizer.swap_bars(state, i, j)
                self.active_visualizer.highlight(i, j, soft_blue)


            self.current_step += 1

            # Controls the speed of the animation
            QTimer.singleShot(self.animation_speed, self.play_selection_sort)


    def play_binary_search(self, steps):
                print("play binary search called")

                if self.current_step >= len(steps):
                    return

                step_type, old_left, mid, old_right, sub_arr, new_left, new_right = steps[self.current_step]

                if step_type == "initial":
                    print("Drawing initial array")
                    self.active_visualizer.Bdraw_array(step_type, sub_arr, old_left)

                elif step_type == "check":
                    # Highlight the mid in current array
                    mid_in_current = mid - old_left
                    self.active_visualizer.highlight(0, mid_in_current, len(sub_arr)-1)

                elif step_type == "low":
                    # Highlight before drawing new array
                    mid_in_current = mid - old_left
                    self.active_visualizer.highlight(0, mid_in_current, len(sub_arr)-1, soft_blue, soft_yellow)
                    # Draw the new smaller array after a moment
                    QTimer.singleShot(self.animation_speed // 4,
                                     lambda: self.active_visualizer.Bdraw_array("low", sub_arr, new_left))

                elif step_type == "high":

                    # Highlight before drawing new array
                    mid_in_current = mid - old_left
                    self.active_visualizer.highlight(0, mid_in_current, len(sub_arr)+1, soft_blue, soft_yellow)
                    # Draw the new smaller array after a moment
                    QTimer.singleShot(self.animation_speed // 4,
                                     lambda: self.active_visualizer.Bdraw_array("high", sub_arr, new_left))

                elif step_type == "found":

                    mid_in_current = mid - old_left
                    self.active_visualizer.found(mid_in_current)

                elif step_type == "not_found":
                    print("Not found")
                    for i in range(len(sub_arr)):
                        self.active_visualizer.not_found(i)

                self.current_step += 1
                QTimer.singleShot(self.animation_speed, lambda: self.play_binary_search(steps))





    def play_Insertion_sort(self):
                if self.current_step >= len(self.steps):
                        self.active_visualizer.completed_sort()
                        self.explain_label.setText(f"Completed sorting")
                        self.ui.Explanation_label.clear()
                        return

                    #step_type, i, j, state = self.steps[self.current_step]
                    # Safe unpacking
                step = self.steps[self.current_step]
                step_type = step[0]
                i = step[1]
                j = step[2]
                state = step[3]
                key = step[4] if len(step) > 4 else None

                self.active_visualizer.draw_array(state)

                if step_type == "compare":
                        print("insertion sort compared called")
                        self.explain_label.setText(f"Comparing....")

                        self.active_visualizer.draw_array(state)
                        self.active_visualizer.highlight(i, j, soft_yellow)

                elif step_type == "shift":
                        print("insertion sort shift called")
                        self.explain_label.setText(f"shifting.....")
                        self.active_visualizer.swap_bars(state, i, j)
                        self.active_visualizer.highlight(i, j, soft_blue)

                elif step_type == "insert":
                        print("insertion sort insert called")
                        self.explain_label.setText(f"Inserting.....")
                        self.active_visualizer.draw_array(state)

                        self.active_visualizer.highlight(i, i, soft_green)

                elif step_type == "key":
                        print("insertion sort insert called")
                        self.explain_label.setText(f"Setting key.....")
                        self.active_visualizer.draw_array(state)

                        self.active_visualizer.highlight(i, i, soft_gray)

                self.current_step += 1
                QTimer.singleShot(self.animation_speed, self.play_Insertion_sort)






    def random_array(self,source="Bubble_sort"):  #Generates random array
        self.active_visualizer.scene.clear()
        self.active_visualizer.view.centerOn(0, 0)
        self.active_visualizer.bars.clear()
        self.visualizer2.scene.clear()

        self.current_step = 0
        self.steps = []


        if source == "Bubble_sort":
                size_text= self.ui.size_array_lineEdit.text() # Sorting size input
                if not size_text:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size = int(size_text)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                if size<6:

                        arr=[random.randint(1,100) for _ in range(size)]
                        self.current_array = arr

                        self.active_visualizer.draw_array(arr)
                        self.active_visualizer.draw_box_color()

                        self.visualizer2.ref_drawArray(arr)

                else:
                        print("invalid size")

                        QMessageBox.warning(
                                self,
                                "Input Error",
                                "Max size 5!"
                            )
                self.ui.size_array_lineEdit.clear()


        elif source == "Insertion_sort":
                print("Random array insertion sort called")
                size_text= self.ui.size_array_lineEdit_InsertionSort.text()
                if not size_text:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size = int(size_text)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                if size<10:
                        arr=[random.randint(1,100) for _ in range(size)]
                        self.current_array = arr
                        self.active_visualizer.draw_array(arr)
                        self.active_visualizer.draw_box_color()
                        self.visualizer2.ref_drawArray(arr)
                        self.ui.size_array_lineEdit_InsertionSort.clear()
                else:

                        print("invalid size")

                        QMessageBox.warning(
                                self,
                                "Input Error",
                                "Max size 10!"
                            )

        elif source == "Selection_sort":
                size_text = self.ui.size_array_lineEdit_SelectionSort.text()
                if not size_text:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size = int(size_text)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                if size<10:
                        arr=[random.randint(1,100) for _ in range(size)]
                        self.current_array = arr
                        self.active_visualizer.draw_array(arr)
                        self.visualizer2.ref_drawArray(arr)
                        self.active_visualizer.draw_box_color()
                        self.ui.size_array_lineEdit_SelectionSort.clear()
                else:
                        print("invalid size")

                        QMessageBox.warning(
                                self,
                                "Input Error",
                                "Max size 10!"
                            )


        elif source == "Linear_search":
                size_text = self.ui.size_array_lineEdit_LSearch.text()
                if not size_text:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size = int(size_text)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                if size < 10:
                        self.ui.size_array_lineEdit_LSearch.setToolTip("Enter numbers between 1-10 only")
                        self.ui.size_array_lineEdit_LSearch.setValidator(QIntValidator(1, 10))
                        arr=[random.randint(1,100) for _ in range(size)]
                        self.current_array = arr
                        self.active_visualizer.draw_array(arr)
                        self.visualizer2.ref_drawArray(arr)
                        self.ui.size_array_lineEdit_LSearch.clear()
                else:
                        print("Invalid size")

                        QMessageBox.warning(
                                self,
                                "Input Error",
                                "Max size 10!"
                            )



        elif source ==  "Merge_sort":
                size_text = self.ui.size_array_lineEdit_MergeSort.text()
                if not size_text:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size = int(size_text)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                if size < 6:

                        arr=[random.randint(1,100) for _ in range(size)]
                        self.current_array = arr
                        self.active_visualizer.draw_box_color()
                        self.active_visualizer.draw_array(arr)
                        self.visualizer2.ref_drawArray(arr)
                else:
                        print("Invalid size")
                self.ui.size_array_lineEdit_MergeSort.clear()


        else:
                return




    def custom_array(self,source ="Bubble_sort"): #Gets array input from the user
        self.active_visualizer.scene.clear()
        self.active_visualizer.bars.clear()
        self.visualizer2.scene.clear()
        self.current_step = 0
        self.steps = []


        if source == "Bubble_sort":

                size_lineEdit = self.ui.size_array_lineEdit
                size= size_lineEdit.text()  # Sorting size input

                if not size:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size_text = int(size)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                lineEdit= self.ui.custom_array_lineEdit

                custom_arr = lineEdit.text()


        elif source == "Insertion_sort":
                size_lineEdit = self.ui.size_array_lineEdit_InsertionSort
                size = size_lineEdit.text()
                if not size:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size_text = int(size)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                lineEdit = self.ui.CArray_lineEdit_InsertionSort
                custom_arr = lineEdit.text()


        elif source == "Selection_sort":
                size_lineEdit = self.ui.size_array_lineEdit_SelectionSort
                size = size_lineEdit.text()
                if not size:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size_text = int(size)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                lineEdit = self.ui.CArray_lineEdit_SelectionSort
                custom_arr = lineEdit.text()


        elif source == "Linear_search":
                size_lineEdit = self.ui.size_array_lineEdit_LSearch
                size = size_lineEdit.text()
                if not size:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size_text = int(size)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                lineEdit = self.ui.CArray_lineEdit_LSearch
                custom_arr = lineEdit.text()




        elif source == "Merge_Sort":
                size_lineEdit = self.ui.size_array_lineEdit_MergeSort
                size = size_lineEdit.text()
                if not size:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Please enter the array size first."
                    )
                    return

                try:
                    size_text = int(size)
                except ValueError:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "Array size must be a valid number."
                    )
                    return
                lineEdit = self.ui.CArray_lineEdit_MergeSort
                custom_arr = lineEdit.text()




        else:
                return


        if size_text == "" or custom_arr == "":
                print("input the required size and value for custom array!")
                QMessageBox.warning(
                self,
                "Input Error",
                "Enter value for custom array!")
                return

        #size = int(size_txt)

        parts = custom_arr.replace(",", " ").split() #splits the string into individual values

        if len(parts) != size_text:
                QMessageBox.warning(
                self,
                "Input Error",
                "Size of array does not match!")
                return
        else:


                arr = [int(x) for x in parts]

                self.current_array = arr
                self.visualizer2.ref_drawArray(arr)
                self.active_visualizer.draw_array(arr)
                #self.active_visualizer.draw_box_color()
        lineEdit.clear()
        size_lineEdit.clear()



    def CArray_Bsearch(self,source = "Binary_serach"):
                self.steps = []
                self.current_step = 0

                self.active_visualizer.clear()
                if source == "Binary_search":
                    size_txt = int(self.ui.size_array_lineEdit_Bsearch.text())  # Searching size input
                    custom_arr = self.ui.lineEdit_Bsearch.text()
                if size_txt == "" or custom_arr == "":
                        QMessageBox.warning(
                        self,
                        "Input Error",
                        "Enter value for custom array!")
                        print("input the required size and value for customr array!")
                        return

                size = int(size_txt)

                parts = custom_arr.replace(",", " ").split() #splits the string into individual values

                if len(parts) != size:
                        QMessageBox.warning(
                        self,
                        "Input Error",
                        "Size of array does not match!")
                        return
                else:

                            arr = [int(x) for x in parts]

                            self.current_array = arr
                            self.current_step = self.steps
                            self.visualizer2.ref_drawArray(arr)
                            self.active_visualizer.Bdraw_array(self.steps,arr)
                self.ui.size_array_lineEdit_Bsearch.clear()
                self.ui.lineEdit_Bsearch.clear()

    def sorted_array(self,source = "Binary_search"):

        self.current_step = 0
        self.active_visualizer.clear()
        self.steps = []
        text = self.ui.size_array_lineEdit_Bsearch.text().strip()

        if not text:
            QMessageBox.warning(
                self,
                "Input Error",
                "Please enter the array size first."
            )
            return

        try:
            size_text = int(text)
        except ValueError:
            QMessageBox.warning(
                self,
                "Input Error",
                "Array size must be a valid number."
            )
            return
        if size_text < 11:

                arr = []
                start = 1
                step_max = 10
                current = start
                for _ in range(size_text):
                        current += random.randint(1, step_max)
                        arr.append(current)
                self.current_array =arr
                self.current_step = self.steps
                self.active_visualizer.Bdraw_array(self.steps,arr)
                self.visualizer2.ref_drawArray(arr)

        else:
                print("Invalid size")
                QMessageBox.warning(
                    self,
                    "Input Error",
                    "Max array size 10!"
                )
                return
        self.ui.size_array_lineEdit_Bsearch.clear()


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

        if action == "stack overflow":
                print("Stack overflow!")
        else:
                self.active_visualizer.draw_stack(state)

        self.ui.Stack_lineEdit.clear()

    def pop_stack(self,source = "Stack"):
        action, value,state = self.stack.pop()

        if action == "stack underflow":
                print("Stack Underflow!")
        else:
                self.active_visualizer.draw_stack(state)

    def clear_stack(self,source = "Stack"):
            action, value,state = self.stack.clear()
            if action == "stack underflow":
                    print("stack is empty!")
            else :
                    self.active_visualizer.draw_stack(state)
                    self.active_visualizer.scene.clear()


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

    def clear_queue(self,source = "Queue"):
            action, value,state = self.queue.clear()
            if action == "Queue underflow":
                    print("Queue is empty!")
            else :
                    self.active_visualizer.draw_queue(state)
                    self.active_visualizer.scene.clear()


    def InsertHead_LinkedList(self, source ="Linked_List"):

                    value_text = self.ui.lineEdit_LinkedList.text().strip()
                    if not value_text:
                            return

                    try:
                            value = int(value_text)
                    except ValueError:
                            print("Invalid input")
                            return

                    steps = self.linked_list.insert_head(self.active_visualizer,value)
                    print("linked list widget steps called")
                    self.active_visualizer.animate_steps(steps)
                    self.ui.lineEdit_LinkedList.clear()

    def RemoveHead_LinkedList(self,source ="Linked List"):
             print("Remove linkedlist At head called")
             steps = self.linked_list.delete_head(self.active_visualizer)
             self.active_visualizer.animate_steps(steps)


    def InsertTail_LinkedList(self, source ="Linked_List"):

                     value_text = self.ui.lineEdit_LinkedList.text().strip()
                     if not value_text:
                             return

                     try:
                             value = int(value_text)
                     except ValueError:
                             print("Invalid input")
                             return

                     steps = self.linked_list.insert_tail(self.active_visualizer,value)
                     print("linked list widget steps called")
                     self.active_visualizer.animate_steps(steps)
                     self.ui.lineEdit_LinkedList.clear()

    def RemoveTail_LinkedList(self,source ="Linked List"):
              print("Remove linkedlist at Tail  called")
              steps = self.linked_list.delete_tail(self.active_visualizer)
              self.active_visualizer.animate_steps(steps)

    def Clear_LinkedList(self,source = "Linked LIst"):
            self.active_visualizer.clear()

    def Insert_BST(self):
                text = self.ui.lineEdit_BST.text().strip()

                if not text.isdigit():
                    QMessageBox.warning(self, "Invalid Input", "Enter an integer value")
                    return

                value = int(text)
                self.active_visualizer.animate_insert(value)
                self.ui.lineEdit_BST.clear()


    def Remove_BST(self):
            value_text= self.ui.lineEdit_BST.text().strip()
            value= int(value_text)
            self.active_visualizer.animate_delete(value)
            self.ui.lineEdit_BST.clear()

    def Search_BST(self):
            value_text= self.ui.Target_lineEdit_BST.text().strip()
            value= int(value_text)
            self.active_visualizer.animate_search(value)
            self.ui.Target_lineEdit_BST.clear()


    def Clear_BST(self):
            self.active_visualizer.clear()

    def GenerateGraph_BFS(self):
        self.active_visualizer.clear()
        text = self.ui.vertex_lineEdit_BFS.text().strip()

        if not text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Enter an integer value")
            return

        node_count = int(text)
        if node_count <= 2:
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Number of vertices must be at least 5"
            )
            return
        max_possible_edges = (node_count * (node_count - 1)) // 2
        max_extra_edges = max_possible_edges - (node_count - 1)
        edges = random.randint(1,max_extra_edges)
        extra_edges = min(4, edges)

        graph = GraphGenerator.generate_graph(node_count, extra_edges)
        positions = GraphGenerator.generate_positions(node_count)
        self.active_visualizer.graph = graph
        self.active_visualizer.draw_graph_edges(graph, positions)
        self.active_visualizer.node_items = self.active_visualizer.draw_graph_nodes(positions)
        self.active_visualizer.QueueVisualizerBFS = self.visualizer3
        self.ui.lineEdit_BST.clear()
        self.ui.vertex_lineEdit_BFS.clear()


    def Traverse_BFS(self):
        raw_vertex = self.ui.lineEdit_BFS.text().strip()
        node_count= int(raw_vertex)
        if not raw_vertex:
               QMessageBox.warning(
                   self,
                   "Input Error",
                   "Please enter a start vertex"
               )
               return
        if node_count < 2:
           QMessageBox.warning(
               self,
               "Invalid Input",
               "Number of vertices must be at least 3"
           )
           return

        if node_count >10:
               QMessageBox.warning(
               self,
               "Invalid Input",
               "Number of veritces must be less than 10")
               return
        vertex = int(raw_vertex)
        self.active_visualizer.start_bfs(vertex)
        self.ui.lineEdit_BFS.clear()


    def Clear_BFS(self):
        self.active_visualizer.clear()
        self.visualizer3.scene.clear()

    def GenerateGraph_DFS(self):
        self.active_visualizer.clear()
        self.visualizer3.scene.clear()
        text = self.ui.vertex_lineEdit_DFS.text().strip()

        if not text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Enter an integer value")
            return

        node_count = int(text)
        if node_count <= 2:
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Number of vertices must be at least 3"
            )
            return

        if node_count >10:
                QMessageBox.warning(
                self,
                "Invalid Input",
                "Number of veritces must be less than 10")
                return
        max_possible_edges = (node_count * (node_count - 1)) // 2
        max_extra_edges = max_possible_edges - (node_count - 1)
        edges = random.randint(1,max_extra_edges)
        extra_edges = min(4, edges)

        graph = GraphGenerator.generate_graph(node_count, extra_edges)
        positions = GraphGenerator.generate_positions(node_count)
        self.active_visualizer.graph = graph
        self.active_visualizer.draw_graph_edges(graph, positions)
        self.active_visualizer.node_items = self.active_visualizer.draw_graph_nodes(positions)
        self.active_visualizer.StackVisualizerDFS = self.visualizer3
        self.ui.lineEdit_BST.clear()
        self.ui.vertex_lineEdit_DFS.clear()

        pass
    def Traverse_DFS(self):
        raw_vertex = self.ui.StartVertex_lineEdit_DFS.text().strip()
        if not raw_vertex:
               QMessageBox.warning(
                   self,
                   "Input Error",
                   "Please enter a start vertex"
               )
               return
        vertex = int(raw_vertex)
        self.active_visualizer.start_dfs(vertex)
        self.ui.StartVertex_lineEdit_DFS.clear()

    def Clear_DFS(self):
        self.active_visualizer.clear()
        self.visualizer3.scene.clear()

















#Run application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
