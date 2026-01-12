from PySide6.QtGui import QColor,QIntValidator

soft_blue   = QColor(100, 149, 237)   # Cornflower blue
soft_green  = QColor(46, 125, 50)  # Light green
soft_red    = QColor(240, 128, 128)   # Light coral
soft_gray   = QColor(200, 200, 200)   # Light gray
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)

class linkedList_fun:
        def __init__(self, capacity=5):
                self.capacity = capacity




        @staticmethod
        def insert_head(visualizer, value):
                steps = []
                steps.append(("insertHead", None, value))  # None means insert at head

                return steps

        @staticmethod
        def delete_head(visualizer):
                steps = []

                if visualizer.head is None:
                    return steps

                old_head = visualizer.head
                steps.append(("deleteHead", old_head, None))  # Mark for deletion
                steps.append(("removeHead", old_head, None))  # Actually remove it
                return steps


        @staticmethod
        def insert_tail(visualizer, value):
            steps = []
            steps.append(("insertTail", None, value))  # None means insert at head

            return steps

        @staticmethod
        def delete_head(visualizer):
            steps = []

            if visualizer.head is None:
                return steps

            old_head = visualizer.head
            steps.append(("deleteTail", old_head, None))  # Mark for deletion
            steps.append(("removeTail", old_head, None))  # Actually remove it
            return steps
