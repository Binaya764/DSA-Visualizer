from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsScene
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt,QTimer
from PySide6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsSimpleTextItem
)
from PySide6.QtGui import QBrush,QPainter,QColor
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtCore import QRectF
from algorithms.BFS.BFS_algo import bfs_fun

import random
import math
from PySide6.QtCore import QPointF
from algorithms.DFS.DFS_algo import dfs_fun


soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(46, 125, 50)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)


class GraphGenerator:
    def __init__(self,node_count=8, extra_edges=3):
        self.node_count = node_count
        self.extra_edges = extra_edges



    def generate_graph(node_count, extra_edges):
        graph = {i: [] for i in range(node_count)}

        # Spanning tree to ensure connectivity
        for i in range(1, node_count):
            parent = random.randint(0, i - 1)
            graph[i].append(parent)
            graph[parent].append(i)

        #adding extra edges
        added = 0
        while added < extra_edges:
            u = random.randint(0, node_count - 1)
            v = random.randint(0, node_count - 1)

            if u != v and v not in graph[u]:
                graph[u].append(v)
                graph[v].append(u)
                added += 1

        return graph

    def generate_positions(node_count, center=(300, 250), radius=180):

        cx, cy = center
        positions = {}

        for i in range(node_count):
            angle = 2 * math.pi * i / node_count
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            positions[i] = QPointF(x, y)

        return positions

class DFSvisualizer:
    def __init__(self, graphics_view, traversal_label):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.node_items = {}
        self.edge_items = {}
        self.stack = {}
        self.step_index=0
        self.traversal_label = traversal_label
        self.traversal_path = []


        self.view.setRenderHint(QPainter.Antialiasing, True)
        self.view.setRenderHint(QPainter.TextAntialiasing, True)


    def draw_graph_edges(self, graph, positions):
        pen = QPen(soft_gray, 2)

        for u in graph:
            for v in graph[u]:
                if u < v:  # avoid duplicate edges
                    p1 = positions[u]
                    p2 = positions[v]

                    line = QGraphicsLineItem(
                        p1.x(), p1.y(),
                        p2.x(), p2.y()
                    )
                    line.setPen(pen)
                    self.scene.addItem(line)
                    # store edge for both directions
                    self.edge_items[(u, v)] = line
                    self.edge_items[(v, u)] = line


    def draw_graph_nodes(self, positions, radius=20):
        node_items = {}

        for node, pos in positions.items():
            circle = QGraphicsEllipseItem(
                pos.x() - radius,
                pos.y() - radius,
                radius * 2,
                radius * 2
            )
            circle.setBrush(soft_blue)
            circle.setPen(QPen(Qt.white, 2))
            self.scene.addItem(circle)

            label = QGraphicsSimpleTextItem(str(node))
            label.setPos(pos.x() - 6, pos.y() - 10)
            self.scene.addItem(label)

            node_items[node] = circle

        return node_items

    def clear(self):
        self.scene.clear()
        self.node_count = 0
        self.extra_edges = 0

    def start_dfs(self, start):
        self.traversal_path = []


        #self.active_visualizer.node_items = node_item
        for node in self.node_items.values():
            node.setBrush(QBrush(soft_blue))

        # reset edges
        for edge in self.edge_items.values():
            edge.setPen(QPen(soft_gray, 2))

        self.steps = dfs_fun(self.graph, start)
        self.step_index = 0
        self.stack = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_dfs_step)
        self.timer.start(800)

    def animate_dfs_step(self):
        if self.step_index >= len(self.steps):
            self.timer.stop()
            return

        step = self.steps[self.step_index]
        action = step[0]

        if action == "push":
            _, node = step
            self.stack.append(node)
            self.node_items[node].setBrush(QBrush(soft_yellow))

        elif action == "pop":
            _, node = step

            if self.stack and self.stack[-1] == node:
                self.stack.pop()


        elif action == "visit":
            _, node = step

            self.traversal_path.append(node)
            self.update_traversal_text()
            self.node_items[node].setBrush(QBrush(soft_green))

        elif action == "edge":
            _, u, v = step
            edge = self.edge_items.get((u, v))
            if edge:
                edge.setPen(QPen(soft_yellow, 3))

        elif action == "back-edge":
            _, u, v = step
            edge = self.edge_items.get((u, v))
            if edge:
                edge.setPen(QPen(soft_red, 3))

        self.StackVisualizerDFS.draw_stack(self.stack)
        self.step_index += 1

    def clear(self):
        self.scene.clear()
        self.node_items.clear()
        self.edge_items.clear()
        self.steps = []
        self.step_index = 0
        self.traversal_label.clear()

    def update_traversal_text(self):
        text =  " → ".join(map(str, self.traversal_path))
        self.traversal_label.setText(text)



class StackVisualizerDFS:

    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.blocks = []

    def draw_stack(self, stack):
        self.scene.clear()
        self.blocks.clear()
        self.view.setSceneRect(self.scene.itemsBoundingRect())
        self.view.centerOn(0,0)


        width = 80
        height = 40
        spacing = 5
        base_y = 250  # bottom of stack

        # Draw stack blocks
        for i, val in enumerate(stack):
            x = 100
            y = base_y - (i + 1) * (height + spacing)

            rect = QGraphicsRectItem(QRectF(x, y, width, height))
            rect.setBrush(QBrush(Qt.darkCyan))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 30, y + 10)

            self.scene.addItem(rect)
            self.scene.addItem(text)
            self.blocks.append((rect, text))

        # Draw TOP label
        if stack:
            top_label = QGraphicsSimpleTextItem("TOP")
            top_label.setBrush(Qt.yellow)
            top_label.setPos(190, base_y - len(stack)*(height+spacing))
            self.scene.addItem(top_label)

    def highlight_top(self):
        if self.blocks:
            self.blocks[-1][0].setBrush(QBrush(Qt.red))



