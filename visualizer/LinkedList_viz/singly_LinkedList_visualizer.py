from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem, QGraphicsLineItem
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import QRectF, Qt, QTimer

class NodeVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.nodes = []  # Stores tuple: (rect, text)
        self.arrows = []  # Stores arrows
        self.node_spacing = 80

    def draw_list(self, lst, highlight_index=None, highlight_color=Qt.yellow):
        """Draws the linked list with optional highlighted node."""
        self.scene.clear()
        self.nodes.clear()
        self.arrows.clear()

        x = 10
        y = 50

        for i, val in enumerate(lst):
            # Draw node rectangle
            rect = QGraphicsRectItem(QRectF(x, y, 50, 50))
            rect.setBrush(QBrush(Qt.gray ))
            self.scene.addItem(rect)

            # Draw value text
            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 15, y + 10)
            self.scene.addItem(text)

            self.nodes.append((rect, text))

            # Draw arrow to next node
            if i < len(lst) - 1:
                line = QGraphicsLineItem(x + 50, y + 25, x + self.node_spacing, y + 25)
                pen = QPen(Qt.white)
                pen.setWidth(2)
                line.setPen(pen)
                self.scene.addItem(line)
                self.arrows.append(line)

            x += self.node_spacing

        # Draw head label
        if lst:
            head_label = QGraphicsSimpleTextItem("Head")
            head_label.setBrush(Qt.green)
            head_label.setPos(10, y - 30)
            self.scene.addItem(head_label)

    def highlight_node(self, index, color=Qt.red):
        """Highlights a node at index."""
        if 0 <= index < len(self.nodes):
            self.nodes[index][0].setBrush(QBrush(color))

    def clear(self):
        self.scene.clear()
        self.nodes.clear()
        self.arrows.clear()

"""
# Animation controller for linked list operations
class LinkedListAnimation:
    def __init__(self, visualizer, algorithm):
        self.visualizer = visualizer
        self.algorithm = algorithm
        self.steps = []
        self.current_step = 0

    def set_steps(self, steps):
        self.steps = steps
        self.current_step = 0

    def play_next(self):
        if self.current_step >= len(self.steps):
            return

        action, index, value, state = self.steps[self.current_step]

        # Draw current linked list state
        highlight_idx = None
        if action in ["traverse", "check"]:
            highlight_idx = index
        elif action in ["found"]:
            highlight_idx = index
        elif action in ["insert", "append", "prepend", "delete_start", "delete_end"]:
            highlight_idx = index

        self.visualizer.draw_list(state, highlight_index=highlight_idx)

        self.current_step += 1
        QTimer.singleShot(800, self.play_next)  # Adjust speed here
"""
