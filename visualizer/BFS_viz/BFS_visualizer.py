
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

class BFSvisualizer:
    def __init__(self, graphics_view,traversal_label):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.node_items = {}
        self.edge_items = {}
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

    def start_bfs(self, vertex):
        graph = self.graph
        self.traversal_path = []
        self.steps = bfs_fun(self,graph, vertex)
        self.step_index = 0
        self.queue = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_bfs_step)
        self.timer.start(1500)



    def animate_bfs_step(self):
        if self.step_index >= len(self.steps):
            self.timer.stop()
            return

        #action, node = self.steps[self.step_index]
        step = self.steps[self.step_index]

        action = step[0]

        if action == "enqueue":
            _, node = step
            self.queue.append(node)
            self.node_items[node].setBrush(soft_yellow)

        elif action == "dequeue":
            _, node = step
            if self.queue and self.queue[0] == node:
                self.queue.pop(0)

        elif action == "visit":
            _, node = step
            self.traversal_path.append(node)
            self.update_traversal_text()
            self.node_items[node].setBrush(soft_green)

        elif action == "edge":
            _, u, v = step
            edge = self.edge_items.get((u, v))
            if edge:
                edge.setPen(QPen(soft_yellow, 3))


        self.QueueVisualizerBFS.draw_queue(self.queue)
        self.step_index += 1

    def clear(self):
        self.scene.clear()
        self.node_count = 0
        self.node_items={}
        self.edge_items={}
        self.traversal_label.clear()


    def update_traversal_text(self):
        text =  " → ".join(map(str, self.traversal_path))
        self.traversal_label.setText(text)



class QueueVisualizerBFS:
    def __init__(self, graphics_view2):
        self.view = graphics_view2
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.blocks = []   # stores (rect, text)

    def draw_queue(self, queue):
        self.scene.clear()
        self.blocks.clear()

        width = 70
        height = 40
        spacing = 10

        x = 100
        base_y = 350   # FRONT position (fixed at bottom)

        # Draw queue blocks (bottom → top)
        for i, val in enumerate(queue):
            y = base_y - i * (height + spacing)

            rect = QGraphicsRectItem(QRectF(x, y, width, height))
            rect.setBrush(QBrush(Qt.darkCyan))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 25, y + 10)

            self.scene.addItem(rect)
            self.scene.addItem(text)
            self.blocks.append((rect, text))

        # FRONT label (always bottom)
        if queue:
            front_label = QGraphicsSimpleTextItem("FRONT")
            front_label.setBrush(Qt.yellow)
            front_label.setPos(x + width + 10, base_y+20)
            self.scene.addItem(front_label)

            # REAR label (topmost element)
            rear_y = base_y - (len(queue) - 1) * (height + spacing)
            rear_label = QGraphicsSimpleTextItem("REAR")
            rear_label.setBrush(Qt.yellow)
            rear_label.setPos(x + width + 10, rear_y)
            self.scene.addItem(rear_label)


    def highlight_front(self):
        if self.blocks:
            self.blocks[0][0].setBrush(QBrush(Qt.red))
