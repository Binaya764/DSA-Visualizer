from PySide6.QtGui import QColor,QIntValidator

soft_blue   = QColor(100, 149, 237)   # Cornflower blue
soft_green  = QColor(46, 125, 50)  # Light green
soft_red    = QColor(240, 128, 128)   # Light coral
soft_gray   = QColor(200, 200, 200)   # Light gray
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)

class linkedList_fun:
    """Simple algorithms for insert and delete at head"""

    @staticmethod
    def insert(visualizer, value):
        """Insert a new node at the head of the list"""
        steps = []
        steps.append(("message", f"Inserting {value} at head", soft_green))
        steps.append(("insert", None, value))  # None means insert at head
        steps.append(("message", f"Inserted {value} successfully!", soft_green))
        return steps

    @staticmethod
    def delete(visualizer):
        """Delete the head node"""
        steps = []

        if visualizer.head is None:
            steps.append(("message", "List is empty, nothing to delete", soft_red))
            return steps

        old_head = visualizer.head
        steps.append(("message", f"Deleting head node with value {old_head.value}", soft_red))
        steps.append(("delete", old_head, None))  # Mark for deletion
        steps.append(("remove", old_head, None))  # Actually remove it
        steps.append(("message", "Head node deleted!", soft_green))
        return steps
