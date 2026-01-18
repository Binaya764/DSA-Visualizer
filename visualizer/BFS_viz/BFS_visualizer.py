
from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsScene
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsSimpleTextItem
)
from PySide6.QtGui import QBrush

import random
import math
from PySide6.QtCore import QPointF


class GraphGenerator:
    def __init__(self,node_count=8, extra_edges=3):
        self.node_count = node_count
        self.extra_edges = extra_edges


    def generate_graph(node_count, extra_edges):
        """
        Returns:
            graph: dict[int, list[int]]  (adjacency list)
        """
        graph = {i: [] for i in range(node_count)}

        # ---- Step 1: Spanning tree (ensures connectivity) ----
        for i in range(1, node_count):
            parent = random.randint(0, i - 1)
            graph[i].append(parent)
            graph[parent].append(i)

        # ---- Step 2: Add extra random edges ----
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
        """
        Returns:
            positions: dict[int, QPointF]
        """
        cx, cy = center
        positions = {}

        for i in range(node_count):
            angle = 2 * math.pi * i / node_count
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            positions[i] = QPointF(x, y)

        return positions

class BFSvisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

    def draw_graph_edges(self, graph, positions):
        pen = QPen(Qt.black, 2)

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


    def draw_graph_nodes(self, positions, radius=20):
        node_items = {}

        for node, pos in positions.items():
            circle = QGraphicsEllipseItem(
                pos.x() - radius,
                pos.y() - radius,
                radius * 2,
                radius * 2
            )
            circle.setBrush(QBrush(Qt.white))
            circle.setPen(QPen(Qt.black, 2))
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


