from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsEllipseItem,
    QGraphicsSimpleTextItem,
    QGraphicsLineItem,
)
from PySide6.QtGui import QPen, QColor, QPainter
from PySide6.QtCore import Qt, QTimer
import math


soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(76, 175, 80)
soft_red    = QColor(244, 67, 54)
soft_yellow = QColor(240, 200, 120)


# defining tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#step generation
def bst_insert_steps(root, value):
    steps = []
    current = root
    parent = None

    while current:
        steps.append(("visit", current))
        parent = current

        if value < current.value:
            current = current.left
        elif value > current.value:
            current = current.right
        else:
            steps.append(("duplicate", current))
            return steps

    steps.append(("insert", parent, value))
    return steps

def bst_delete_steps(root, value):
    steps = []
    parent = None
    current = root

    #Search
    while current and current.value != value:
        steps.append(("visit", current))
        parent = current
        if value < current.value:
            current = current.left
        else:
            current = current.right

    if not current:
        return steps  # value not found

    steps.append(("found", current))

    #  CASE 1: Leaf
    if not current.left and not current.right:
        steps.append(("remove_leaf", current, parent))
        return steps

    #  CASE 2: One child
    if not current.left or not current.right:
        child = current.left if current.left else current.right
        steps.append(("replace_child", current, parent, child))
        return steps

    #  CASE 3: Two children
    succ_parent = current
    successor = current.right

    while successor.left:
        steps.append(("visit", successor))
        succ_parent = successor
        successor = successor.left

    steps.append(("successor", successor))
    steps.append(("swap", current, successor))
    steps.append(("final_remove", successor, succ_parent))

    return steps

def bst_search_steps(root, value):
    steps = []
    current = root

    while current:
        steps.append(("visit", current))

        if value == current.value:
            steps.append(("found", current))
            return steps
        elif value < current.value:
            current = current.left
        else:
            current = current.right

    # If we exit loop, value not found
    steps.append(("not_found", value))
    return steps



class BST_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.node_radius = 20
        self.level_gap = 80

        self.nodes = {}            # TreeNode -> (circle, text)
        self.root = None
        self.steps = []
        self.step_index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_step)

        self.view.setRenderHint(QPainter.Antialiasing, True)
        self.view.setRenderHint(QPainter.TextAntialiasing, True)

    #Drawing tree
    def draw_tree(self, root):
        self.scene.clear()
        self.nodes.clear()
        self.root = root

        if not root:
            return

        self.draw_node(root, 0, 0, 200)

    def draw_node(self, node, x, y, spread):
        circle = QGraphicsEllipseItem(
            x - self.node_radius,
            y - self.node_radius,
            self.node_radius * 2,
            self.node_radius * 2,
        )
        circle.setBrush(soft_blue)
        circle.setPen(QPen(Qt.white, 2))

        text = QGraphicsSimpleTextItem(str(node.value))
        text.setBrush(Qt.white)
        text.setPos(x - 6, y - 10)

        self.scene.addItem(circle)
        self.scene.addItem(text)

        self.nodes[node] = (circle, text)

        if node.left:
            lx, ly = x - spread, y + self.level_gap
            self.draw_edge(x, y, lx, ly)
            self.draw_node(node.left, lx, ly, spread // 2)

        if node.right:
            rx, ry = x + spread, y + self.level_gap
            self.draw_edge(x, y, rx, ry)
            self.draw_node(node.right, rx, ry, spread // 2)

    def draw_edge(self, x1, y1, x2, y2):
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        if length == 0:
            return

        ux, uy = dx / length, dy / length
        start_x = x1 + ux * self.node_radius
        start_y = y1 + uy * self.node_radius
        end_x   = x2 - ux * self.node_radius
        end_y   = y2 - uy * self.node_radius

        line = QGraphicsLineItem(start_x, start_y, end_x, end_y)
        line.setPen(QPen(Qt.white, 2))
        self.scene.addItem(line)

    #animation part
    def animate_insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            self.draw_tree(self.root)
            return

        self.steps = bst_insert_steps(self.root, value)
        self.step_index = 0
        self.timer.start(300)

    def animate_delete(self, value):
        if not self.root:
            return

        self.steps = bst_delete_steps(self.root, value)
        self.step_index = 0
        self.timer.start(300)

    def animate_search(self,value):
        if not self.root:
            return
        self.steps= bst_search_steps(self.root,value)
        self.step_index=0
        self.timer.start(300)


    def next_step(self):
        if self.step_index >= len(self.steps):
            self.timer.stop()
            return

        # reset visuals
        for circle, _ in self.nodes.values():
            circle.setBrush(soft_blue)
            circle.setPen(QPen(Qt.white, 2))

        step = self.steps[self.step_index]
        action = step[0]

        if action == "visit":
            self.highlight(step[1], soft_yellow)

        elif action == "insert":
            parent, value = step[1], step[2]
            new_node = TreeNode(value)

            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

            self.draw_tree(self.root)
            self.highlight(new_node, soft_blue)

        elif action == "delete":
            parent, value = step[1], step[2]
            delete_node= TreeNode(value)
            self.draw_tree(self.root)

        elif action == "duplicate":
            self.highlight(step[1], soft_red)

        elif action == "found":
            self.highlight(step[1], soft_green)

        elif action == "remove_leaf":
            node, parent = step[1], step[2]

            if parent is None:
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None

            self.draw_tree(self.root)

        elif action == "replace_child":
            node, parent, child = step[1], step[2], step[3]

            if parent is None:
                self.root = child
            elif parent.left == node:
                parent.left = child
            else:
                parent.right = child

            self.draw_tree(self.root)

        elif action == "successor":
            self.highlight(step[1], QColor(186, 160, 255))  # purple

        elif action == "swap":
            node, succ = step[1], step[2]
            node.value, succ.value = succ.value, node.value
            self.draw_tree(self.root)

        elif action == "final_remove":
            succ, parent = step[1], step[2]

            if parent.left == succ:
                parent.left = succ.right
            else:
                parent.right = succ.right

            self.draw_tree(self.root)


        self.step_index += 1

    def highlight(self, node, color):
        if node not in self.nodes:
            return
        circle, _ = self.nodes[node]
        circle.setBrush(color)
        circle.setPen(QPen(Qt.yellow, 2))

    def clear(self):
        # Stop animation
        if self.timer.isActive():
            self.timer.stop()

        # Clear graphics
        self.scene.clear()

        # Clear data
        self.nodes.clear()
        self.root = None
        self.steps = []
        self.step_index = 0
