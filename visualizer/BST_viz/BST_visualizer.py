from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsEllipseItem,
    QGraphicsSimpleTextItem,
    QGraphicsLineItem
)
from PySide6.QtGui import QBrush, QPen,QColor,QPainter
from PySide6.QtCore import Qt
import math

soft_blue   = QColor(100, 149, 237)   # Cornflower blue
soft_green  = QColor(46, 125, 50)  # Light green
soft_red    = QColor(240, 128, 128)   # Light coral
soft_gray   = QColor(200, 200, 200)   # Light gray
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)


class BST_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.node_radius = 20
        self.level_gap = 80
        self.horizontal_gap = 40

        self.nodes = {}  # value -> (circle, text)
        self.view.setRenderHint(QPainter.Antialiasing, True)
        self.view.setRenderHint(QPainter.TextAntialiasing, True)

    def draw_tree(self, root):
        self.scene.clear()
        self.nodes.clear()

        if root is None:
            return


        start_x = 0
        start_y = 0
        self.draw_node(root, start_x, start_y, 200)

    def draw_node(self, node, x, y, spread):
        if node is None:
            return
        x = round(x)
        y = round(y)

        # Draw node circle
        circle = QGraphicsEllipseItem(
            x - self.node_radius,
            y - self.node_radius,
            self.node_radius * 2,
            self.node_radius * 2
        )
        pen = QPen(Qt.white)
        pen.setWidth(2)
        pen.setCosmetic(False)
        circle.setBrush(soft_blue)
        circle.setPen(pen)


        # Draw value
        text = QGraphicsSimpleTextItem(str(node.value))
        text.setBrush(Qt.white)
        text.setPos(x - 4, y - 10)

        self.scene.addItem(circle)
        self.scene.addItem(text)

        self.nodes[node.value] = (circle, text)

        # Left child
        if node.left:
            lx = x - spread
            ly = y + self.level_gap
            self.draw_edge(x, y, lx, ly)
            self.draw_node(node.left, lx, ly, spread // 2)

        # Right child
        if node.right:
            rx = x + spread
            ry = y + self.level_gap
            self.draw_edge(x, y, rx, ry)
            self.draw_node(node.right, rx, ry, spread // 2)


    def draw_edge(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        length = math.hypot(dx, dy)

        if length == 0:
            return

        # Normalize
        ux = dx / length
        uy = dy / length

        # Start/end at circle border
        start_x = x1 + ux * self.node_radius
        start_y = y1 + uy * self.node_radius
        end_x   = x2 - ux * self.node_radius
        end_y   = y2 - uy * self.node_radius

        line = QGraphicsLineItem(start_x, start_y, end_x, end_y)
        line.setPen(QPen(Qt.white, 2))
        self.scene.addItem(line)


    def found(self, value):
        self.highlight(value, Qt.green)

    def highlight_node(self, node, action):
            if node not in self.nodes:
                return

            circle = self.nodes[node]

            if action == "visit":
                circle.setBrush(QBrush(QColor(255, 193, 7)))   # soft yellow

            elif action == "insert":
                circle.setBrush(QBrush(QColor(76, 175, 80)))   # soft green

            elif action == "duplicate":
                circle.setBrush(QBrush(QColor(244, 67, 54)))   # soft red
